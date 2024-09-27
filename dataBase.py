import sqlite3
import os
import re
#////////////////////////////////////////////////////////////////////////////////////////////////////
class DataBase:
    def __init__(self) -> None:
        self.dbName = "dataBase.db"
        self.connection = self.__startConn()
    #////////////////////////////////////////////////////////////////////////////////////////////////
    def __del__(self) -> None:
        self.__endConn()
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
    def addRecord(self, website:str, email:str, password:str, key:str)-> int:
        '''exitCodes = {
            0: "Success",
            1: "Failed to connect with the data base",
            2: "Bad parameters",
            3: "Failed to execute query"
        }'''

        if self.connection == None:
            return 1
        
        website = str(website).upper()
        email = str(email).upper()
        password = str(password)
    
        reWebsite = "^([A-Z0-9]+\.)+[A-Z0-9]+$"
        reEmail = "^[A-Z0-9\_\.\+\-]+@([A-Z0-9]+\.)+[A-Z0-9]+$"

        if re.search(reWebsite, website) == None or re.search(reEmail, email) == None:
            return 2

        cur = (self.connection).cursor()
        try:
            cur.execute('''INSERT INTO tb_accounts(website, email, password) VALUES(?,?,?);''',
                        (website, email, password))
            (self.connection).commit()
        except:
            return 3
        
        return 0
#////////////////////////////////////////////////////////////////////////////////////////////////////
x = DataBase()
print(x.addrecord("facebookcom","jeht99@outlook.com", "NEW99"))
