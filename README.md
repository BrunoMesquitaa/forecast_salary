# Forecast Brazilian Salary API Documentation

The Forecast Brazilian Salary API is a powerful tool that allows users to predict salaries based on various factors and parameters. This documentation provides a comprehensive guide on how to use the API effectively.

> Using as basis: 
>
>> Framework FastAPI:
>>> Documentation: https://fastapi.tiangolo.com
>>>
>>> Source code: https://github.com/tiangolo/fastapi
>>
>> xgboost:
>>> Documentation: https://xgboost.readthedocs.io/en/stable/index.html
>>>
>>> Source code: https://github.com/dmlc/xgboost/blob/36eb41c960483c8b52b44082663c99e6a0de440a/doc/index.rst
>
> Data:
>
>> caged-microdados_movimentacao: https://basedosdados.org/dataset/562b56a3-0b01-4735-a049-eeac5681f056?table=2245875f-d1ef-490d-be29-4f8fb2191335
>> it's necessary download
>> dictionary to help in the request: https://storage.googleapis.com/basedosdados-dev/auxiliary_files/br_me_caged/microdados_movimentacao/auxiliary_files.zip
---

## Running the Project:
> ### Local:
>
> I recommend using a virtualenv.
>
> Installation of packages:
>```console
> poetry install
> ```
> or
>```console
> pip install --no-cache-dir --upgrade -r requirements.txt
> ```
>
> Run:
> ```console
> uvicorn forecast_salary.main:app --reload
> ```
> 
> Documentation :point_down:
>> http://127.0.0.1:8000/docs
>>
>> http://127.0.0.1:8000/redoc
> ---

## Table of Contents

1. [Introduction](#introduction)
2. [Endpoint](#endpoint)
3. [Request Format](#request-format)
4. [Response Format](#response-format)
5. [Example Usage](#example-usage)
6. [Conclusion](#conclusion)

## Introduction

The Forecast Brazilian Salary API utilizes advanced machine learning algorithms to analyze historical salary data and predict future salary trends. It takes into account various factors such as location, education level, age, working hours, race, gender, disability, employment type, establishment size, occupation, and category to generate accurate salary forecasts.

## Endpoint

The base URL for accessing the Forecast Brazilian Salary API is:

```
http://127.0.0.1:8000/docs
```

## Request Format

To make a Brazilian salary forecast request, send a POST request to the `/model_xg` endpoint. The request payload should be in JSON format and include the necessary parameters. The following parameters are required:

- `id_municipio`: The municipality ID where the job is based.
- `grau_instrucao`: The education level of the job seeker.
- `idade`: The age of the job seeker.
- `horas_contratuais`: The number of contracted working hours.
- `raca_cor`: The race/ethnicity of the job seeker.
- `sexo`: The gender of the job seeker.
- `tipo_deficiencia`: The disability status of the job seeker.
- `indicador_trabalho_intermitente`: The indicator for intermittent work.
- `tamanho_estabelecimento_janeiro`: The size of the establishment in January.
- `indicador_aprendiz`: The indicator for apprenticeship.
- `cnae_2_subclasse`: The economic activity classification (CNAE 2nd subclass).
- `cbo_2002`: The occupation code (CBO 2002).
- `categoria`: The job category.

Additional optional parameters may be available, depending on the specific requirements of the API. Please refer to the API documentation for more details.

## Response Format

The response from the Brazilian Forecast Salary API is returned in JSON format and contains the predicted salary information. The response will include the following fields:

- `valor`: The predicted salary for the specified parameters.
- `valor_min` and `valor_max`: The confidence interval of the predicted salary.

## Example Usage

### Request

```console
curl -X 'POST' \
  'http://127.0.0.1:8000/model_xg/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id_municipio": 355030,
  "grau_instrucao": 5,
  "idade": 23,
  "horas_contratuais": 44,
  "raca_cor": 3,
  "sexo": 1,
  "cbo_2002": 317110
}'
```

### Response

```json
{
  "valor": 1995.44,
  "valor_min": 1779.96,
  "valor_max": 2210.92
}
```

### Conclusion

To determine whether a regression model is good or not, we need to consider multiple factors and evaluate its performance based on specific criteria. Here are some points to consider when assessing the quality of the XGBRegressor model:

1. R-Squared Score: The R-Squared score measures the proportion of the variance in the dependent variable that can be explained by the independent variables. In this case, the R-Squared score is 0.7725690283347872, which indicates that approximately 77.3% of the variance in the target variable is accounted for by the model. Generally, a higher R-Squared score suggests a better fit, but the significance of the score can vary depending on the context and domain.

2. Mean Absolute Error (MAE): The MAE represents the average absolute difference between the predicted and actual values. The lower the MAE, the better the model's performance. In this case, the MAE is 309.863753261293, which indicates that, on average, the model's predictions deviate by approximately 309.86 units from the actual values.

3. Root Mean Squared Error (RMSE): The RMSE measures the square root of the average squared difference between the predicted and actual values. Similar to MAE, a lower RMSE indicates better accuracy. Here, the RMSE is 1072.5310400483004, which means that, on average, the model's predictions deviate by approximately 1072.53 units from the actual values.

4. Mean Absolute Percentage Error (MAPE): The MAPE represents the average percentage difference between the predicted and actual values. A lower MAPE suggests better accuracy. In this case, the MAPE is 0.10798620922958303, indicating an average percentage deviation of approximately 10.8% between the predicted and actual values.

5. Median Absolute Percentage Error (MDAPE): The MDAPE is similar to MAPE but uses the median instead of the mean. It provides a robust measure of the model's performance, especially when dealing with outliers. Here, the MDAPE is 0.052778250889449936, which implies that the median percentage deviation between predicted and actual values is approximately 5.3%.

6. Explained Variance Deviation (EVD): The EVD indicates the proportion of the variance in the target variable that is explained by the model. A higher value suggests better explanatory power. In this case, the EVD is 0.6487956761151695, indicating that approximately 64.9% of the variance in the target variable is explained by the model.

Based on these metrics, the XGBRegressor model seems to have reasonable performance. The R-Squared score is relatively high, indicating a good fit to the data. The MAE, RMSE, MAPE, and MDAPE values are also within acceptable ranges, suggesting that the model's predictions are reasonably close to the actual values. However, it's essential to compare these metrics with domain-specific requirements and other competing models to have a comprehensive evaluation of the model's goodness.