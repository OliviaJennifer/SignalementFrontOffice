import pyodbc
import psycopg2
class Connexion:
    def getConnexion(self):
        try:
            conn = psycopg2.connect(
            user = "postgres",
            password = "0809",
            host = "localhost",
            port = "5433",
            database = "databaseFournisseur"
        )
            return conn
        except Exception as e:
            print(e)