from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    status = Column(String)

    vacancies = relationship("Vacancy", back_populates="project")

class Vacancy(Base):
    __tablename__ = "vacancies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    requirements = Column(String)
    status = Column(String)
    project_id = Column(Integer, ForeignKey("projects.id"))

    project = relationship("Project", back_populates="vacancies")