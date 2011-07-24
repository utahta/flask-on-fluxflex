from app.db.project import ProjectTable
from app.db import db_session

class ProjectModel(object):
    def get_entries(self):
        return db_session.query(ProjectTable).all()
    