# models/Users.py
from db import conn, cursor

class User:
    TABLE_NAME = "users"

    def __init__(self, fullName, emailAddress, phoneNo, id=None):
        self.id = id
        self.fullName = fullName
        self.emailAddress = emailAddress
        self.phoneNo = phoneNo
        

    def save(self):
        sql = f"""
            INSERT INTO {self.TABLE_NAME} (fullName, emailAddress, phoneNo)
            VALUES (?, ?, ?, ?)
        """
        cursor.execute(sql, (self.fullName, self.emailAddress, self.phoneNo))
        conn.commit()
        self.id = cursor.lastrowid

        return self

    @classmethod
    def create_table(cls):
        sql = f"""
            CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fullName TEXT NOT NULL,
                emailAddress TEXT NOT NULL UNIQUE,
                phoneNo INTEGER NOT NULL,
            )
        """
        cursor.execute(sql)
        conn.commit()

    @classmethod
    def find_by_fullName_and_emailAddress(cls, fullName, emailAddress):
        sql = f"SELECT * FROM {cls.TABLE_NAME} WHERE fullName = ? AND emailAddress = ?"
        cursor.execute(sql, (fullName, emailAddress))
        user = cursor.fetchone()
        return user

User.create_table()