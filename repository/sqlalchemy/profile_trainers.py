from typing import Dict, Any
from sqlalchemy.orm import Session
from domain.data.sqlalchemy_models import Signup, Login, Attendance_Member, Profile_Trainers
from sqlalchemy import desc


class Pro_trainers:

    def __init__(self, sess:Session):
        self.sess:Session = sess


    def insert_trainer(self, traine: Profile_Trainers) -> bool: 
        print('entrou')
        try:
            print('test>>', traine.id)
            self.sess.add(traine)
            self.sess.commit()
            print(traine.id)
        except: 
            print('erro')
            return False 

        return True

    def update_trainer(self, id:int, details:Dict[str, Any]) -> bool: 

       try:
            self.sess.query(Profile_Trainers).filter(Profile_Trainers.id == id).update(details)     
            self.sess.commit() 
           
       except: 
           return False 

       return True

    def delete_trainer(self, id:int) -> bool: 
        try:
            trainer = self.sess.query(Profile_Trainers).filter(Profile_Trainers.id == id).delete()
            self.sess.commit()
          
        except: 
            return False 

        return True

    def get_all_trainers(self):
        return self.sess.query(Profile_Trainers).all() 
