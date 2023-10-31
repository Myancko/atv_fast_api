from typing import Dict, Any
from sqlalchemy.orm import Session
from domain.data.sqlalchemy_models import Signup, Login, Profile_Members, Attendance_Member
from sqlalchemy import desc


class AttendenceRepository: 
    
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
    def insert_attendence(self, attendence: Attendance_Member) -> bool: 
        try:
            self.sess.add(attendence)
            self.sess.commit()
    
        except: 
            return False 
        return True
    
    def update_attendence(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
             self.sess.query(Attendance_Member).filter(Attendance_Member.id == id).update(details)     
             self.sess.commit() 
           
       except: 
           return False 
       return True
   
    def delete_attendence(self, id:int) -> bool: 
        try:
           signup = self.sess.query(Attendance_Member).filter(Attendance_Member.id == id).delete()
           self.sess.commit()
          
        except: 
            return False 
        return True
    
    def get_all_attendence(self):
        return self.sess.query(Attendance_Member).all() 
    
    def get_attendence(self, id:int): 
        return self.sess.query(Attendance_Member).filter(Attendance_Member.id == id).one_or_none()