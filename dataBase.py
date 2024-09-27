import crypto
import sqlite3
import os
import re
#////////////////////////////////////////////////////////////////////////////////////////////////////
reWebsite = "^([A-Z0-9]+\.)+[A-Z0-9]+$"
reEmail = "^[A-Z0-9\_\.\+\-]+@([A-Z0-9]+\.)+[A-Z0-9]+$"
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
    def addRecord(self, website:str, email:str, password:str, key:bytes)-> int:
        if self.connection == None:
            return 1
        
        website = str(website).upper()
        email = str(email).upper()
        password = crypto.encrypt_text(key,str(password)) 

        if(re.search(reWebsite, website) == None or
           re.search(reEmail, email) == None or str(type(key)) != "<class 'bytes'>"):
            return 2

        cur = (self.connection).cursor()
        try:
            cur.execute('''INSERT INTO tb_accounts(website, email, password) VALUES(?,?,?);''',
                        (website, email, password))
            (self.connection).commit()
        except:
            return 3
        
        return 0
    #////////////////////////////////////////////////////////////////////////////////////////////////
    def deleteRecord(self, target:int)-> int:
        if self.connection == None:
            return 1
        
        if str(type(target)) != "<class 'int'>":
            return 2
        
        cur = (self.connection).cursor()
        try:
            cur.execute('''DELETE FROM tb_accounts WHERE account_id=?;''', (target,))
            (self.connection).commit()
        except:
            return 3
        
        return 0
    #////////////////////////////////////////////////////////////////////////////////////////////////
    def updateRecord(self, target:int, website:str, email:str, password:str, key:bytes)-> int:
        if self.connection == None:
            return 1
        
        website = str(website).upper()
        email = str(email).upper()
        password = crypto.encrypt_text(key,str(password)) 

        if(re.search(reWebsite, website) == None or
           re.search(reEmail, email) == None or str(type(target)) != "<class 'int'>"
           or str(type(key)) != "<class 'bytes'>"):
            return 2
        
        cur = (self.connection).cursor()
        try:
            cur.execute('''UPDATE tb_accounts SET website=?, email=?, password=?
                        WHERE account_id=?;''',(website, email, password, target))
            (self.connection).commit()
        except:
            return 3
        
        return 0
    #////////////////////////////////////////////////////////////////////////////////////////////////
    def getRecords(self)-> list:
        if self.connection == None:
            return []
        
        cur = (self.connection).cursor()
        try:
            cur.execute('''SELECT * FROM tb_accounts;''')
            return cur.fetchall()
        except:
            return []
    #////////////////////////////////////////////////////////////////////////////////////////////////
    def getRecord(self, target)-> list:
        if self.connection == None:
            return []
        
        if str(type(target)) != "<class 'int'>":
            return 2
        
        cur = (self.connection).cursor()
        try:
            cur.execute('''SELECT * FROM tb_accounts WHERE account_id=?''', (target,))
            return cur.fetchall()
        except:
            return []
#////////////////////////////////////////////////////////////////////////////////////////////////////
'''exitCodes = {
    0: "Success",
    1: "Failed to connect with the data base",
    2: "Bad parameters",
    3: "Failed to execute query"
    }'''
#////////////////////////////////////////////////////////////////////////////////////////////////////