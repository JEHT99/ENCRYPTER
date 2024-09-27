import sqlite3
import os
#////////////////////////////////////////////////////////////////////////////////////////////////////
class DataBase:
    def __init__(self) -> None:
        self.dbName = "dataBase.db"
    #///////////////////////////////////////////////////////////////////////////////////////////////
    def createDb(self) -> bool:
        if os.path.isfile(self.dbName):
            return False

        conn = None
        try:
            conn = sqlite3.connect(self.dbName)
            c = conn.cursor()
            
            query ='''CREATE TABLE "tb_accounts" (
            "account_id" INTEGER,
            "website" TEXT NOT NULL,
            "email" TEXT NOT NULL,
            "password" TEXT NOT NULL,
            PRIMARY KEY("account_id" AUTOINCREMENT));'''
            
            c.execute(query)
            conn.close()
        except:
            if conn:
                conn.close()
                os.system(f"del {self.dbName}")
            return False
        
        return True
#////////////////////////////////////////////////////////////////////////////////////////////////////
