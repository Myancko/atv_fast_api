from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from db_config.sqlalchemy_connect import SessionFactory
from domain.request.attendance import AttendanceMemberReq
from domain.data.sqlalchemy_models import Attendance_Member
from repository.sqlalchemy.attendence import AttendenceRepository


router = APIRouter()


def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()


@router.post("/attendence/add")
def add_attendence(req: AttendanceMemberReq, sess: Session = Depends(sess_db)):
    repo: AttendenceRepository = AttendenceRepository(sess)
    attendence = Attendance_Member(id=req.id, 
                                   member_id=req.member_id, 
                                   timeout=req.timeout, 
                                   timein=req.timein,
                                   date_log=req.date_log)
    
    result = repo.insert_attendence(attendence)
    if result == True:
        return attendence
    else:
        return JSONResponse(content={'message': 'create attendence problem encountered'}, status_code=500)


@router.patch("/attendence/update")
def update_attendence(id: int, req: AttendanceMemberReq, sess: Session = Depends(sess_db)):
    attendence_dict = req.dict(exclude_unset=True)
    repo: AttendenceRepository = AttendenceRepository(sess)
    result = repo.update_attendence(id, attendence_dict)
    if result:
        return JSONResponse(content={'message': 'attendence updated successfully'}, status_code=201)
    else:
        return JSONResponse(content={'message': 'update attendence error'}, status_code=500)


@router.delete("/attendence/delete/{id}")
def delete_attendence(id: int, sess: Session = Depends(sess_db)):
    repo: AttendenceRepository = AttendenceRepository(sess)
    result = repo.delete_attendence(id)
    if result:
        return JSONResponse(content={'message': 'attendence deleted successfully'}, status_code=201)
    else:
        return JSONResponse(content={'message': 'delete attendence error'}, status_code=500)


@router.get("/attendence/list")
def list_attendence(sess: Session = Depends(sess_db)):
    repo: AttendenceRepository = AttendenceRepository(sess)
    result = repo.get_all_attendence()
    return result


@router.get("/attendence/get/{id}")
def get_attendence(id: int, sess: Session = Depends(sess_db)):
    repo: AttendenceRepository = AttendenceRepository(sess)
    result = repo.get_attendence(id)
    return result
