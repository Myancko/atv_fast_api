from fastapi import FastAPI
from api import admin, login, profile_Trainers, profile_member, gym_class,attendence


app = FastAPI()
app.include_router(admin.router)
app.include_router(login.router)
app.include_router(profile_Trainers.router)
app.include_router(profile_member.router)
app.include_router(gym_class.router)
app.include_router(attendence.router)
