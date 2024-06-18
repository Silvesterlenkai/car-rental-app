# models/CarTypeList.py
from db import conn, cursor

class CarTypeList:
    TABLE_NAME = "cartypelist"

    def __init__(self, name, seats, ratePerDay, gearType, id=None):
        self.id = id
        self.name = name
        self.seats = seats
        self.ratePerDay = ratePerDay
        self.gearType = gearType

    def save(self):
        sql = f"""
            INSERT INTO {self.TABLE_NAME} (name, seats, ratePerDay, gearType)
            VALUES (?, ?, ?, ?)
        """
        cursor.execute(sql, (self.name, self.seats, self.ratePerDay, self.gearType))
        conn.commit()
        self.id = cursor.lastrowid

        return self

    @classmethod
    def create_table(cls):
        sql = f"""
            CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                seats INTEGER NOT NULL,
                ratePerDay INTEGER NOT NULL,
                gearType TEXT NOT NULL
            )
        """
        cursor.execute(sql)
        conn.commit()

    @classmethod
    def find_all(cls):
        cursor.execute(f"SELECT * FROM {cls.TABLE_NAME}")
        rows = cursor.fetchall()
        return rows

CarTypeList.create_table()