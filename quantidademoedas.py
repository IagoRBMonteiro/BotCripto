import pandas as pd
import os 
import time 
from binance.client import Client
from binance.enums import *

api_key = os.getenv("KEY_BINANCE")
secret_key = os.getenv("SECRET_BINANCE")

cliente_binance = Client(api_key, secret_key)



symbol_info = cliente_binance.get_symbol_info('XRPBRL') # -> Insira aqui o nome do ativo que deseja operar


lot_size_filter = next(f for f in symbol_info['filters'] if f['filterType'] == 'LOT_SIZE')

min_qty = float(lot_size_filter['minQty']) # -> Quantidade mínima que a corretora aceita
max_qty = float(lot_size_filter['maxQty']) # -> Quantidade máxima que a corretora aceita

step_size = float(lot_size_filter['stepSize'])

print(f'\n\nA quantidade mínima operável é de: {min_qty} | A quantidade máxima operável é de: {max_qty}\n\n')