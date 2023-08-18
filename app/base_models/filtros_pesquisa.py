from typing import Optional

from pydantic import BaseModel


class FiltrosRelatorio(BaseModel):
    razao_social: Optional[str]
    bairro: Optional[str]
    cep: Optional[str]
    ddd: Optional[str]
    capital_social_de: Optional[str]
    capital_social_ate: Optional[str]
    situacao_cadastral: Optional[str]
    data_abertura_de: Optional[str]
    data_abertura_ate:Optional[str]
    atividade_principal: Optional[str]
    estado: Optional[str]
    municipio: Optional[str]
    natureza_juridica: Optional[str]