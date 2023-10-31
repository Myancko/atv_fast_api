from typing import Dict, Any
from sqlalchemy.orm import Session
from domain.data.sqlalchemy_models import Signup, Login, Profile_Members, Attendance_Member
from sqlalchemy import desc


class Pro_members:

    def __init__(self, sess:Session):
        self.sess:Session = sess


    def insert_member(self, member: Profile_Members) -> bool: 
        print('entrou')
        try:
            print('test>>', member.id)
            self.sess.add(member)
            self.sess.commit()
            print(member.id)
        except: 
            print('erro')
            return False 

        return True

    def update_member(self, id:int, details:Dict[str, Any]) -> bool: 

       try:
            self.sess.query(Profile_Members).filter(Profile_Members.id == id).update(details)     
            self.sess.commit() 
           
       except: 
           return False 

       return True

    def delete_member(self, id:int) -> bool: 
        try:
            member = self.sess.query(Profile_Members).filter(Profile_Members.id == id).delete()
            self.sess.commit()
          
        except: 
            return False 

        return True

    def get_all_members(self):
        return self.sess.query(Profile_Members).all() 
