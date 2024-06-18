from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CarInfoModel(BaseModel):
    user_id : int
    fullName: str
    date:datetime
    emailAddress = str
    phoneNo = int
    pickupAddress = str
    pickupDate = str
    pickupTime = str
    dropOffAddress = str
    dropOffDate = str
    dropOffTime = str 

class CarTypeListModel(BaseModel):
    user_id: int
    seats: str
    date: datetime
    ratePerDay: int
    gearType: str

class UserModel(BaseModel):
    user_id: int
    fullName: str
    date: datetime
    emailAddress: str
    phoneNo: int



