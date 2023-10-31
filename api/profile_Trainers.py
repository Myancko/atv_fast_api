from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from db_config.sqlalchemy_connect import SessionFactory
from domain.request.trainers import ProfileTrainersReq
from domain.data.sqlalchemy_models import Profile_Trainers
from repository.sqlalchemy.profile_trainers import Pro_trainers

router = APIRouter()


def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()


@router.post("/trainers/add")
def add_trainer(req: ProfileTrainersReq, sess: Session = Depends(sess_db)):
    repo: Pro_trainers = Pro_trainers(sess)
    
    trainer = Profile_Trainers(id=req.id,    
                      firstname=req.firstname, 
                      lastname=req.lastname, 
                      age=req.age,
                      position=req.position,
                      tenure=req.tenure,
                      shift=req.shift)

    result = repo.insert_trainer(trainer)
    if result == True:
        return trainer
    else:
        return JSONResponse(content={'message': 'create trainer problem found'}, status_code=500)

@router.patch("/trainers/update")
def update_trainer(id: int, req: ProfileTrainersReq, sess: Session = Depends(sess_db)):

    traine_dict = req.dict(exclude_unset=True)
    repo: Pro_trainers = Pro_trainers(sess)
    result = repo.update_trainer(id, traine_dict)

    if result:
        return JSONResponse(content={'message': 'Trainer updated successfully'}, status_code=201)
    else:
        return JSONResponse(content={'message': 'error found on trainer update'}, status_code=500)

@router.delete("/trainers/delete/{id}")
async def delete_trainer(id: int, sess: Session = Depends(sess_db)):
    repo: Pro_trainers = Pro_trainers(sess)
    result = repo.delete_trainer(id)
    if result:
        return JSONResponse(content={'message': 'trainer deleted successfully'}, status_code=201)
    else:
        return JSONResponse(content={'message': 'delete trainer error found'}, status_code=500)

@router.get("/trainers/list")
async def list_login(sess: Session = Depends(sess_db)):
    repo: Pro_trainers = Pro_trainers(sess)
    result = repo.get_all_trainers()
    return result