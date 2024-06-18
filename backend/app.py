
from pydantic import BaseModel
from models.CarInfo import CarInfo
from models. CarTypeList import CarTypeList
from models. Users import User
from db import cursor, conn



class CarInfoModel(BaseModel):
    user_id : int
    fullName: str
    emailAddress = str
    phoneNo = int
    pickupAddress = str
    pickupDate = str
    pickupTime = str
    dropOffAddress = str
    dropOffDate = str
    dropOffTime = str 

    
def save_CarInfo(carinfo_data: CarInfoModel):
    carinfo = CarInfo(
        name=carinfo_data.user_id,
        fullName=carinfo_data.fullName ,
        emailAddress=carinfo_data.emailAddress,
        phoneNo=carinfo_data.phoneNo,
        pickupAddress=carinfo_data.pickupAddress,
        pickupDate=carinfo_data.pickupDate,
        pickupTime=carinfo_data.pickupTime,
        dropOffAddress=carinfo_data.dropOffAddress,
        dropOffDate=carinfo_data.dropOffDate,
        dropOffTime=carinfo_data.dropOffTime
    )
    CarInfo.save()
    return {"message": "CarInfo saved successfully"}


def get_CarInfo():
    sql = "SELECT * FROM CarInfo"
    rows = cursor.execute(sql).fetchall()
    orders = [
        {
            "user_id": row[0],
            "fullName": row[1],
            "emailAddress": row[2],
            "phoneNo": row[3],
            "pickupAddress": row[4],
            "pickupDate": row[5],
            "pickupTime":row[6],
            "dropOffAddress":row[7],
            "dropOffDate":row[8],
            "dropOffTime":row[9]
        }
        for row in rows
    ]
    return CarInfo


def delete_CarInfo(CarInfo_id: int):
    sql = "DELETE FROM orders WHERE id = ?"
    cursor.execute(sql, (CarInfo_id,))
    conn.commit()
    return {"message": "CarInfo deleted successfully"}