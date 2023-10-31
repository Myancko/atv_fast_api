from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from db_config.sqlalchemy_connect import SessionFactory
from domain.request.members import ProfileMembersReq
from domain.data.sqlalchemy_models import Profile_Members
from repository.sqlalchemy.profile_member import Pro_members

router = APIRouter()


def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()


@router.post("/member/add")
def add_member(req: ProfileMembersReq, sess: Session = Depends(sess_db)):
    repo: Pro_members = Pro_members(sess)
    
    member = Profile_Members(id=req.id,    
                      firstname=req.firstname, 
                      lastname=req.lastname, 
                      age=req.age,
                      height=req.height,
                      weight=req.weight,
                      membership_type=req.membership_type,
                      trainer_id=req.trainer_id)

    result = repo.insert_member(member)
    if result == True:
        return member
    else:
        return JSONResponse(content={'message': 'create member problem found'}, status_code=500)

@router.patch("/member/update")
def update_member(id: int, req: ProfileMembersReq, sess: Session = Depends(sess_db)):

    gym_dict = req.dict(exclude_unset=True)
    repo: Pro_members = Pro_members(sess)
    result = repo.update_member(id, gym_dict)

    if result:
        return JSONResponse(content={'message': 'member updated successfully'}, status_code=201)
    else:
        return JSONResponse(content={'message': 'error found on member update'}, status_code=500)

@router.delete("/member/delete/{id}")
async def delete_member(id: int, sess: Session = Depends(sess_db)):
    repo: Pro_members = Pro_members(sess)
    result = repo.delete_member(id)
    if result:
        return JSONResponse(content={'message': 'member deleted successfully'}, status_code=201)
    else:
        return JSONResponse(content={'message': 'delete member error found'}, status_code=500)

@router.get("/member/list")
async def list_member(sess: Session = Depends(sess_db)):
    repo: Pro_members = Pro_members(sess)
    result = repo.get_all_members()
    return result