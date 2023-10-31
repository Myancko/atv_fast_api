from pydantic import BaseModel
from datetime import date, time

class AttendanceMemberReq(BaseModel):
    id: int
    member_id: int
    timeout:time
    timein:time
    date_log:date