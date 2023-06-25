from pydantic import BaseModel, validator


class Payload(BaseModel):
    
    # sigla_uf
    id_municipio: int
    grau_instrucao: int
    idade: int
    horas_contratuais: int
    raca_cor: int
    sexo: int
    tipo_deficiencia: int = None
    indicador_trabalho_intermitente: int = None
    tamanho_estabelecimento_janeiro: int = None
    indicador_aprendiz: int = None
    cnae_2_subclasse: int = None
    cbo_2002: int = None
    categoria: int = None
    
    # @validator('bairro', always=True)
    # def bairro_validator(cls, b, values):

    #     try:
    #         if b is None:
    #             return get_bairro(values['lat'], values['lon'],
    #                               "~/GitHub/MIM/dados/shp/DISTRITO_MUNICIPAL_SP_SMDUPolygon.shp")
    #         else:
    #             if valid_bairros(b.upper()):
    #                 return b.upper()
    #     except:
    #         raise ValueError('Error Bairro')
