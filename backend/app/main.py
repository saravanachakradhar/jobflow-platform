from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="JobFlow API")

class Application(BaseModel):
    job_id: int
    applicant_name: str
    applicant_email: str

applications = []
application_counter = 1


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "jobflow-backend"
    }


jobs = [
    {
        "id": 1,
        "title": "DevOps Engineer",
        "company": "TechCorp",
        "location": "Bangalore",
        "status": "open"
    },
    {
        "id": 2,
        "title": "Cloud Engineer",
        "company": "CloudWorks",
        "location": "Hyderabad",
        "status": "open"
    },
    {
        "id": 3,
        "title": "Platform Engineer",
        "company": "DataSystems",
        "location": "Pune",
        "status": "open"
    }
]


@app.get("/jobs/{job_id}")
def get_job(job_id: int):
    jobs = [
        {
            "id": 1,
            "title": "DevOps Engineer",
            "company": "TechCorp",
            "location": "Bangalore",
            "status": "open"
        },
        {
            "id": 2,
            "title": "Cloud Engineer",
            "company": "CloudWorks",
            "location": "Hyderabad",
            "status": "open"
        },
        {
            "id": 3,
            "title": "Platform Engineer",
            "company": "DataSystems",
            "location": "Pune",
            "status": "open"
        }
    ]

    for job in jobs:
        if job["id"] == job_id:
            return job

    return {"error": "Job not found"}

@app.post("/applications")
def create_application(application: Application):
    global application_counter

    new_application = {
        "application_id": application_counter,
        "job_id": application.job_id,
        "applicant_name": application.applicant_name,
        "applicant_email": application.applicant_email,
        "status": "submitted"
    }

    applications.append(new_application)

    application_counter += 1

    return new_application

@app.get("/applications")
def get_applications():
    return applications

@app.put("/applications/{application_id}")
def update_application_status(application_id: int, status: str):

    for application in applications:
        if application["application_id"] == application_id:
            application["status"] = status
            return application

    return {"error": "Application not found"}