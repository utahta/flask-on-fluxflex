from flask import Module, render_template
from app.model.project import ProjectModel

project = Module(__name__)

@project.route('/')
def index():
    model = ProjectModel()
    return render_template('project.html', model=model)

