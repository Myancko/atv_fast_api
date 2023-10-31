from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from db_config.sqlalchemy_connect import SessionFactory
from domain.request.gym import GymReq
from domain.data.sqlalchemy_models import Gym_Class
from repository.sqlalchemy.gym_class import Gym_repo

router = APIRouter()

def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()

@router.post("/gym/add")
def add_gym(req: GymReq, sess: Session = Depends(sess_db)):
    repo : Gym_repo = Gym_repo(sess)
    gym = Gym_Class (
        id = req.id,
        name = req.name,
        member_id = req.member_id,
        trainer_id = req.member_id,    
        approved_id = req.approved_id
    )
    result = repo.insert_gym(gym)
    if result == True:
        return gym
    else:
        print('aq')
        return JSONResponse(content={'message': 'erro in create gym'}, status_code=500)
    
@router.patch("/gym/update")
def update_gym(id: int, req: GymReq, sess: Session = Depends(sess_db)):

    #n funciona ;-;
    
    gym_dict = req.dict(exclude_unset=True)
    repo: Gym_repo = Gym_repo(sess)
    result = repo.update_gym(id, gym_dict)

    if result:
        return JSONResponse(content={'message': 'gym updated successfully'}, status_code=201)
    else:
        return JSONResponse(content={'message': 'error found on gym update'}, status_code=500)

@router.delete("/gym/delete/{id}")
async def delete_gym(id: int, sess: Session = Depends(sess_db)):
    repo: Gym_repo = Gym_repo(sess)
    result = repo.delete_gym(id)
    if result:
        return JSONResponse(content={'message': 'gym deleted successfully'}, status_code=201)
    else:
        return JSONResponse(content={'message': 'delete gym error'}, status_code=500)
    
@router.get("/gym/list")
async def list_login(sess: Session = Depends(sess_db)):
    repo: Gym_repo = Gym_repo(sess)
    result = repo.get_all_gym()
    return result