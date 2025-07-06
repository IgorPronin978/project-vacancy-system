from sqlalchemy.orm import Session
from . import models, schemas

def create_project(db: Session, project: schemas.ProjectCreate):
    db_project = models.Project(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def get_projects(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Project).offset(skip).limit(limit).all()

def get_project(db: Session, project_id: int):
    return db.query(models.Project).filter(models.Project.id == project_id).first()

def update_project(db: Session, project_id: int, project: schemas.ProjectCreate):
    db_project = get_project(db, project_id=project_id)
    if db_project:
        for key, value in project.dict().items():
            setattr(db_project, key, value)
        db.commit()
        db.refresh(db_project)
    return db_project

def delete_project(db: Session, project_id: int):
    db_project = get_project(db, project_id=project_id)
    if db_project:
        db.delete(db_project)
        db.commit()
    return db_project

def create_project_vacancy(db: Session, vacancy: schemas.VacancyCreate, project_id: int):
    db_vacancy = models.Vacancy(**vacancy.dict(), project_id=project_id)
    db.add(db_vacancy)
    db.commit()
    db.refresh(db_vacancy)
    return db_vacancy

def get_vacancies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Vacancy).offset(skip).limit(limit).all()

def get_project_vacancies(db: Session, project_id: int):
    return db.query(models.Vacancy).filter(models.Vacancy.project_id == project_id).all()

def update_vacancy(db: Session, vacancy_id: int, vacancy: schemas.VacancyCreate):
    db_vacancy = db.query(models.Vacancy).filter(models.Vacancy.id == vacancy_id).first()
    if db_vacancy:
        for key, value in vacancy.dict().items():
            setattr(db_vacancy, key, value)
        db.commit()
        db.refresh(db_vacancy)
    return db_vacancy

def delete_vacancy(db: Session, vacancy_id: int):
    db_vacancy = db.query(models.Vacancy).filter(models.Vacancy.id == vacancy_id).first()
    if db_vacancy:
        db.delete(db_vacancy)
        db.commit()
    return db_vacancy