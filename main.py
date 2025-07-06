from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Привет, малыш"}

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/projects/", response_model=schemas.Project)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    return crud.create_project(db=db, project=project)

@app.get("/projects/", response_model=List[schemas.Project])
def read_projects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    projects = crud.get_projects(db, skip=skip, limit=limit)
    return projects

@app.get("/projects/{project_id}", response_model=schemas.Project)
def read_project(project_id: int, db: Session = Depends(get_db)):
    db_project = crud.get_project(db, project_id=project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project

@app.put("/projects/{project_id}", response_model=schemas.Project)
def update_project(project_id: int, project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    db_project = crud.update_project(db, project_id=project_id, project=project)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project

@app.delete("/projects/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db)):
    db_project = crud.delete_project(db, project_id=project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"message": "Project deleted successfully"}

@app.post("/projects/{project_id}/vacancies/", response_model=schemas.Vacancy)
def create_vacancy_for_project(
    project_id: int, vacancy: schemas.VacancyCreate, db: Session = Depends(get_db)
):
    return crud.create_project_vacancy(db=db, vacancy=vacancy, project_id=project_id)

@app.get("/vacancies/", response_model=List[schemas.Vacancy])
def read_vacancies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    vacancies = crud.get_vacancies(db, skip=skip, limit=limit)
    return vacancies

@app.get("/projects/{project_id}/vacancies/", response_model=List[schemas.Vacancy])
def read_project_vacancies(project_id: int, db: Session = Depends(get_db)):
    vacancies = crud.get_project_vacancies(db, project_id=project_id)
    return vacancies

@app.put("/vacancies/{vacancy_id}", response_model=schemas.Vacancy)
def update_vacancy(vacancy_id: int, vacancy: schemas.VacancyCreate, db: Session = Depends(get_db)):
    db_vacancy = crud.update_vacancy(db, vacancy_id=vacancy_id, vacancy=vacancy)
    if db_vacancy is None:
        raise HTTPException(status_code=404, detail="Vacancy not found")
    return db_vacancy

@app.delete("/vacancies/{vacancy_id}")
def delete_vacancy(vacancy_id: int, db: Session = Depends(get_db)):
    db_vacancy = crud.delete_vacancy(db, vacancy_id=vacancy_id)
    if db_vacancy is None:
        raise HTTPException(status_code=404, detail="Vacancy not found")
    return {"message": "Vacancy deleted successfully"}