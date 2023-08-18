from app.utils.formata_data import formata_data
from datetime import datetime
import pandas as pd
import requests


class RelatorioPesquisaAvancada:
    def __init__(self):
        self.url = "https://api.casadosdados.com.br/v2/public/cnpj/search"
        self.headers = {
            "content-type": "application/json; charset=UTF-8",
            "user-agent": "insomnia/2023.4.0"
        }


    async def gerar_relatorio(self, records:list) -> bool:
        try:
            if len(records) == 0:
                return False
            excel = pd.DataFrame.from_records(records)
            excel = excel.drop(["versao", "cnpj_raiz"], axis=1)
            excel["data_consulta"] = datetime.now().strftime('%d/%m/%Y')
            file_path = "relatorio_empresas.xlsx"
            excel.to_excel(file_path, index=False)
            return file_path
        except Exception as error:
            print(error)
            return False


    async def buscar_cnpjs(self, filtros: dict) -> bool or str:
        try:
            razao_social = [filtros.get("razao_social")]  if filtros.get("razao_social") else []
            cep = [filtros.get("cep")]  if filtros.get("cep") else []
            ddd = [filtros.get("ddd")]  if filtros.get("ddd") else []

            capital_social_de = filtros.get("capital_social_de") if filtros.get("capital_social_de") != "" else None
            capital_social_ate = filtros.get("capital_social_ate") if filtros.get("capital_social_de") != "" else None
            data_abertura_de = formata_data(filtros.get("data_abertura_de")) if filtros.get("data_abertura_de") != "" else None
            data_abertura_ate = formata_data(filtros.get("data_abertura_ate")) if filtros.get("data_abertura_ate") != "" else None
            situacao_cadastral = filtros.get("situacao_cadastral") if filtros.get("situacao_cadastral") != "" else None

            atividade_principal = [filtros.get("atividade_principal")]  if filtros.get("atividade_principal") else []
            estado = [filtros.get("estado")]  if filtros.get("estado") else []
            municipio = [filtros.get("municipio").upper()] if filtros.get("municipio") else []
            natureza_juridica = [filtros.get("natureza_juridica")] if filtros.get("natureza_juridica") else []

            lista_empresas = []

            for integer in range(24): # Limite de 25 páginas (1 mil linhas do Excel) podendo ser aumentado...
                json = {
                    "query": {
                        "termo": razao_social,
                        "atividade_principal": atividade_principal,
                        "natureza_juridica": natureza_juridica,
                        "uf": estado,
                        "municipio": municipio,
                        "situacao_cadastral": situacao_cadastral,
                        "cep": cep,
                        "ddd": ddd
                    },
                    "range_query": {
                        "data_abertura": {
                            "lte": data_abertura_ate,
                            "gte": data_abertura_de
                        },
                        "capital_social": {
                            "lte": capital_social_de,
                            "gte": capital_social_ate
                        }
                    },
                    "extras": {
                        "somente_mei": False,
                        "excluir_mei": False,
                        "com_email": True,
                        "incluir_atividade_secundaria": True,
                        "com_contato_telefonico": True,
                        "somente_fixo": False,
                        "somente_celular": False,
                        "somente_matriz": False,
                        "somente_filial": False
                    },
                    "page": integer
                }

                response = requests.post(url=self.url, headers=self.headers, json=json)

                if response.status_code == 200:
                    response = response.json()
                    if response.get("data", {}).get("cnpj") is not None:
                        lista_empresas.extend(response["data"]["cnpj"])
                    # Caso o retorno seja vazio antes de atingir o limite de páginas, encerra o loop e gera o relatório Excel
                    else:
                        path_file = await self.gerar_relatorio(lista_empresas)
                        return path_file

            # Caso o limite de páginas seja atingido, para o loop e gera o relatório .xlsx
            path_file = await self.gerar_relatorio(lista_empresas)
            return path_file
        except Exception as error:
            print(error)
            return False