from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.repository.jobs import (
    create_new_job,
    delete_job_by_id,
    retrieve_job,
    list_jobs,
    update_job_by_id,
)
from db.session import get_db
from schemas.jobs import JobCreate, ShowJob

router = APIRouter()


@router.post('/create-job', response_model=ShowJob)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    owner_id = 1
    job = create_new_job(job, db, owner_id)
    return job


@router.get('/get/{id}', response_model=ShowJob)
def retrieve_job_by_id(id: int, db: Session = Depends(get_db)):
    job = retrieve_job(id=id, db=db)
    print(job)
    if job is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Job with id {id} does not exist',
        )
    return job


@router.get('/all', response_model=List[ShowJob])
def retrieve_all_jobs(db: Session = Depends(get_db)):
    jobs = list_jobs(db=db)
    print(jobs)
    return jobs


@router.put('/update/{id}')
def update_job(id: int, job: JobCreate, db: Session = Depends(get_db)):
    owner_id = 1
    message = update_job_by_id(id=id, job=job, db=db, owner_id=owner_id)
    if not message:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Job with id {id} doest not exist',
        )
    return {'detail': 'Successfully updated the data'}


@router.delete('/delete/{id}')
def delete_job(id: int, db: Session = Depends(get_db)):
    owner_id = 1
    message = delete_job_by_id(id=id, db=db, owner_id=owner_id)
    if not message:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Job with id {id} doest not exist',
        )
    return {'detail': f'Successfully deleted the job with id {id}'}
