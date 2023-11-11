from sqlalchemy.orm import Session
from db.repository.jobs import create_new_job,retreive_job
from schemas.jobs import JobCreate
from tests.utils.user import create_random_owner


def test_retreive_job_by_id(db_session:Session):
    title="title"
    company="test comp"
    company_url="testcomp.com"
    location="USA,NY"
    description="foo bar"
    owner=create_random_owner(db=db_session)
    job_schema=JobCreate(title=title,company=company,company_url=company_url,location=location,description=description)
    Job=create_new_job(job=job_schema,db=db_session,owner_id=owner.id)
    retreived_job=retreive_job(id=Job.id,db=db_session)
    assert retreived_job.id==Job.id
    assert retreived_job.title==title

     