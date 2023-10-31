from pydantic import BaseModel
from datetime import date

class GymReq(BaseModel): 
    id : int 
    name: str 
    member_id: int 
    trainer_id: int
    user_type: int
    approved_id : int
        
    class Config:
        orm_mode = True
        