# models/CarInfo.py
from db import conn, cursor

class CarInfo:
    TABLE_NAME = "carinfo"

    def __init__(self, fullName, emailAddress, phoneNo, pickupAddress, pickupDate, pickupTime, dropOffAddress, dropOffDate, dropOffTime, id=None):
        self.id = id
        self.name = fullName
        self.emailAddress = emailAddress
        self.phoneNo = phoneNo
        self.pickupAddress = pickupAddress
        self.pickupDate = pickupDate
        self.pickupTime = pickupTime
        self.dropOffAddress = dropOffAddress
        self.dropOffDate = dropOffDate
        self.dropOffTime = dropOffTime

    def save(self):
        sql = f"""
            INSERT INTO {self.TABLE_NAME} (fullName, emailAddress, phoneNo, pickupAddress ,pickupDate ,pickupTime ,dropOffAddress ,dropoffDate ,dropOffTime)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(sql, (self.fullName, self.emailAddress, self.phoneNo, self.pickupAddress, self.pickupDate, self.pickupTime, self.dropOffAddress, self.dropOffDate, self.dropOffTime))
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
                pickupAddress TEXT NOT NULL UNIQUE,
                pickupDate TEXT NOT NULL UNIQUE,
                pickupTime TEXT NOT NULL UNIQUE,
                dropOffAddress TEXT NOT NULL UNIQUE,
                dropOffDate TEXT NOT NULL UNIQUE,
                dropOffTime TEXT NOT NULL UNIQUE
                
            )
        """
        cursor.execute(sql)
        conn.commit()

    @classmethod
    def find_all(cls):
        cursor.execute(f"SELECT * FROM {cls.TABLE_NAME}")
        rows = cursor.fetchall()
        return rows

CarInfo.create_table()