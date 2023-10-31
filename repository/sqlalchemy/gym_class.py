from typing import Dict, Any
from sqlalchemy.orm import Session
from domain.data.sqlalchemy_models import Signup, Login, Profile_Members, Attendance_Member, Gym_Class
from sqlalchemy import desc

class Gym_repo:

    def __init__(self, sess:Session):
        self.sess:Session = sess

    def insert_gym (self, gym : Gym_Class) -> bool:

        try:

            self.sess.add(gym)
            self.sess.commit()
            print(gym.id)
            
        except:

            return False

        return True
    
    def update_gym(self, id:int, details:Dict[str, Any]) -> bool: 

       try:
            self.sess.query(Gym_Class).filter(Gym_Class.id == id).update(details)
            print('ok')
            self.sess.commit() 
           
       except: 
           return False 

       return True
   
    def delete_gym(self, id:int) -> bool: 
        try:
           gym = self.sess.query(Gym_Class).filter(Gym_Class.id == id).delete()
           self.sess.commit()
          
        except: 
            return False 
        return True
    
    def get_all_gym(self):
        return self.sess.query(Gym_Class).all() 
    
    def get_gym(self, id:int): 
        return self.sess.query(Gym_Class).filter(Gym_Class.id == id).one_or_none()