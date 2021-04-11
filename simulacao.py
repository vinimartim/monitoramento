import random
from time import sleep
from datetime import datetime
from Conexao.Conexao import Conexao

while True:
    con = Conexao()
    sql = f"update alarmes set porta_bercario = {random.randint(0,1)}, porta_vestiario_m = {random.randint(0,1)}, porta_vestiario_f = {random.randint(0,1)}, porta_rpa_escada = {random.randint(0,1)}, porta_rpa_clc1 = {random.randint(0,1)} where id = 1;"
    con.executa_dml(sql)
    sleep(30)