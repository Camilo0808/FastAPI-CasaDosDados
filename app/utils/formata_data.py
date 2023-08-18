import re
from datetime import datetime

def formata_data(input_date: str) -> str:
    # Verifica o formato da data e converte para o formato desejado
    if re.match(r'\d{2}/\d{2}/\d{4}', input_date):
        date_obj = datetime.strptime(input_date, '%d/%m/%Y')
        return date_obj.strftime('%Y-%m-%d')
    elif re.match(r'\d{4}/\d{2}/\d{2}', input_date):
        date_obj = datetime.strptime(input_date, '%Y/%m/%d')
        return date_obj.strftime('%Y-%m-%d')