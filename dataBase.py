from werkzeug.security import generate_password_hash
import sqlite3
import os
#////////////////////////////////////////////////////////////////////////////////////////////////////
class DataBase:
    def __init__(self) -> None:
        self.dbName = "dataBase.db"
        self.connection = self.__startConn()
    #////////////////////////////////////////////////////////////////////////////////////////////////
    def __del__(self) -> None:
        self.__endConn()
    #////////////////////////////////////////////////////////////////////////////////////////////////
    def __createDb(self) -> bool:
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
        except:
            platforms = {"nt": "del", "posix": "rm"} #Windows and Linux
            if conn:
                conn.close()
                os.system(f"{platforms[os.name]} {self.dbName}")
            return False
        
        return True
    #////////////////////////////////////////////////////////////////////////////////////////////////
    def __startConn(self)-> object:
        if (os.path.isfile(self.dbName) == False and
            self.__createDb() == False):
            return None
        
        try:
            conn = sqlite3.connect(self.dbName)
        except:
            return None
        return conn
    #////////////////////////////////////////////////////////////////////////////////////////////////
    def __endConn(self)-> None:
        if self.connection != None:
            (self.connection).close()
        self.connection == None
    #////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////////
