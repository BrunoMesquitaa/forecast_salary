from functools import lru_cache
from fastapi import HTTPException

import pandas as pd
import math
import numpy as np
import pandas as pd
from datetime import datetime

from sklearn.model_selection import train_test_split
import sklearn.metrics as metrics
import xgboost as xg
from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()

__n__ = 100
__cols__ = ['cnae_2_subclasse', 'cbo_2002', 'categoria', 'id_municipio', #'sigla_uf',
            'grau_instrucao', 'idade', 'horas_contratuais', 'raca_cor', 'sexo',
            'tipo_deficiencia', 'indicador_trabalho_intermitente', 'salario_mensal',
            'tamanho_estabelecimento_janeiro', 'indicador_aprendiz'] 

xgb_r = xg.XGBRegressor(objective='reg:squarederror', n_estimators=__n__,
                        seed=0, max_depth=500, eta=0.01, subsample=1,
                        colsample_bytree=0.75, learning_rate=0.1)

models = [xgb_r]

pd.set_option('display.float_format', lambda x: '%.2f' % x)

@lru_cache(maxsize=1280)
def data_model():
    df = pd.read_csv("forecast_salary/data/caged.csv",
                     sep=',', low_memory=False)
    # df = df[df['sigla_uf'] == 'SP']
    # df = df[df['id_municipio'] == 355030]
    df['sigla_uf'] = df['sigla_uf'].astype('category').cat.codes
    
    df = df[df['cnae_2_subclasse'] != 9999999]
    df = df[df['cbo_2002'] != 999999]
    df = df[df['categoria'] != 999]

    df = df[df['saldo_movimentacao'] == 1]
    df = df[df['tipo_deficiencia'] != 9]

    df = df[df['indicador_trabalho_intermitente'] != 9]
    df = df[df['indicador_aprendiz'] != 9]

    df['grau_instrucao'] = df['grau_instrucao'].replace([80], 12)
    df = df[df['grau_instrucao'] != 99]

    df['sexo'] = df['sexo'].replace([3], 2)
    df = df[df['sexo'] != 9]

    df = df[df['raca_cor'] < 6]

    df = df[df['tamanho_estabelecimento_janeiro'] != 99]

    df = df[df['salario_mensal'] >= 1000]
    df = df[df['salario_mensal'] <= 50_000]

    df['salario_mensal']  = df['salario_mensal']

    df = df[__cols__]
    df = df.dropna()
    df.to_csv('out.csv')
    print(df.describe(include='all'))
    return df


def model_xgboost(n_mod):

    df = data_model()

    df = df[__cols__]

    x = df[[ c for c in __cols__ if c != 'salario_mensal']].to_numpy()
    target = np.log(df['salario_mensal'].to_numpy())
    
    x_train, x_test, target_train, target_test = train_test_split(
        x, target, test_size=0.7, random_state=1
    )

    print("=" * 40)

    print("regression model:", models[n_mod].__class__.__name__)

    m_rk = models[n_mod]
    m_rk.fit(x_train, target_train)

    print("RK score (R-Squared): ", m_rk.score(x_test, target_test))

    pred = math.e**m_rk.predict(x_test)
    target_test = math.e**target_test
    rmse = np.sqrt(np.sum(np.square(target_test - pred))/len(target_test))
    mae = metrics.mean_absolute_error(target_test, pred)
    mape = metrics.mean_absolute_percentage_error(target_test, pred)
    mdape = np.median((np.abs(np.subtract(target_test, pred)/ target_test)))
    evs = metrics.explained_variance_score(target_test, pred)

    print("Results by calculation:", m_rk.__class__.__name__)
    print("MAE:", mae)
    print("RMSE:", rmse)
    print("MAPE:", mape)
    print("MDAPE:", mdape)
    print("EVD:", evs)

    print("=" * 40)

    return m_rk, mape


async def model_predict(data: dict, model) -> float:


    predict_list = np.array([[data.cnae_2_subclasse, data.cbo_2002, data.categoria, data.id_municipio,
                              data.grau_instrucao, data.idade, data.horas_contratuais, data.raca_cor, data.sexo,
                              data.tipo_deficiencia, data.indicador_trabalho_intermitente, 
                              data.tamanho_estabelecimento_janeiro, data.indicador_aprendiz
                            ]])

    value = model.predict(predict_list)[0]
    value = (math.e**value)

    return round(value, ndigits=2)
