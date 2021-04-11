import threading
from time import sleep
import pygame
import random
from datetime import datetime
from Conexao.Conexao import Conexao

pygame.mixer.init()
lock = threading.Lock()

delay_alarme = 60
delay_verificacao = 5

def checa_porta(id):
    sql = "select * from alarmes;"

    con = Conexao()
    result = con.executa_dql(sql)
    con.desconecta()
  
    if result[0][id] == 1:
        return True
    else:
        return False

def alarme(nome_porta, id):
    con = Conexao()
    while True:
        if checa_porta(id) == True:
            status_porta = 1
        else:
            status_porta = 0

        # sql = f"insert into log_monitoramento (data_log, nome_porta, status_porta) values (now(), '{nome_porta}', {status_porta});"
        # con.executa_dml(sql)

        if status_porta == 1:
            sleep(delay_alarme)

            if checa_porta(id) == True:
                print(f"Porta {nome_porta} aberta")

                lock.acquire()
                pygame.mixer.music.load(f"audios/{nome_porta}.mp3")     
                pygame.mixer.music.play()
                sleep(5)
                lock.release()

        sleep(delay_verificacao)

# Uma thread para cada porta
a = threading.Thread(target=alarme, args=("bercario",0,), daemon=True).start()
b = threading.Thread(target=alarme, args=("vestiario_m",1,), daemon=True).start()
c = threading.Thread(target=alarme, args=("vestiario_f",2,), daemon=True).start()
d = threading.Thread(target=alarme, args=("escada",3,), daemon=True).start()
e = threading.Thread(target=alarme, args=("clinica",4,), daemon=True).start()

print("Quantidade de threads:", threading.active_count())

# Para poder parar a execução das threads com CTRL+C 
# As threads devem ser daemon para dar certo (daemon=True)
while True:
    sleep(2)