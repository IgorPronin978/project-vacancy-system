# schemas.py
from pydantic import BaseModel
from typing import Optional

class ProjectBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[str] = None

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int

    class Config:
        from_attributes = True

class VacancyBase(BaseModel):
    title: str
    description: Optional[str] = None
    requirements: Optional[str] = None
    status: Optional[str] = None

class VacancyCreate(VacancyBase):
    pass

class Vacancy(VacancyBase):
    id: int
    project_id: int

    class Config:
        from_attributes = True