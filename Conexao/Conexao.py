import mysql.connector

class Conexao():
    def __init__(self, host="localhost", user="root", password="root", db="monitoramento"):
        self.host = host
        self.user = user
        self.password = password
        self.db = db

    def conecta(self):
        self.con = mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.db)
        self.cur = self.con.cursor()

    def desconecta(self):
        self.con.close()
    
    def executa_dql(self, sql):
        self.conecta()
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result

    def executa_dml(self, sql):
        self.conecta()
        self.cur.execute(sql)
        self.con.commit()