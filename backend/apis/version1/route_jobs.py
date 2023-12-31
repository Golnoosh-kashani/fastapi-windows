from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from db.session import get_db
from db.models.jobs import Job
from schemas.jobs import JobCreate,ShowJob
from db.repository.jobs import create_new_job,retreive_job,list_jobs,update_job_by_id,delete_job_by_id
from typing import List
from db.models.users import User
from apis.version1.route_login import get_current_user_from_token
router=APIRouter()

@router.post("/create-job",response_model=ShowJob)
def create_job(job:JobCreate,db:Session=Depends(get_db),current_user:User=Depends(get_current_user_from_token)):
        job=create_new_job(job=job,db=db,owner_id=current_user.id)
        return job

@router.get("/get/{id}",response_model=ShowJob)
def retreive_job_by_id(id:int,db:Session=Depends(get_db)):
        job=retreive_job(id=id,db=db)
        if not job :
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"job with id {id}does not exist")
        return job
        
@router.get("/all",response_model=List[ShowJob])
def retreive_all_jobs(db:Session=Depends(get_db)):
        jobs=list_jobs(db=db)
        return jobs

@router.put("/update/{id}")
def update_job(id:int,job:JobCreate,db:Session=Depends(get_db),current_user:User=Depends(get_current_user_from_token)):
        job=retreive_job(id=id,db=db)
        if not job:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Job with {id} does not exist")
        print(job.owner_id,current_user.id,current_user.id)
        if job.owner_id== current_user.id or current_user.is_superuser:
                update_job_by_id(id=id,db=db,owner_id=current_user.id)
                return{"msg":"sucssesfully deleted the job"}
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"You are not permitted!!!!")


@router.delete("/delete/{id}")
def delete_job(id:int,db:Session=Depends(get_db),current_user:User=Depends(get_current_user_from_token)):
        job=retreive_job(id=id,db=db)
        if not job:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Job with {id} does not exist")
        print(job.owner_id,current_user.id,current_user.id)
        if job.owner_id== current_user.id or current_user.is_superuser:
                delete_job_by_id(id=id,db=db,owner_id=current_user.id)
                return{"msg":"sucssesfully deleted the job"}
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"You are not permitted!!!!")



        


