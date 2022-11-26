from flask import render_template, request, redirect, url_for
from models import db, Project, app


@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/project/<id>')
def project_detail(id):
    projects = Project.query.all()
    project = Project.query.get_or_404(id)
    skill_list = project.skills.split(', ')
    return render_template('detail.html', project=project, projects=projects, skill_list=skill_list)


@app.route('/project/new', methods=['GET', 'POST'])
def new_project():
    projects = Project.query.all()
    if request.form:
        print(request.form)
        print(request.form['title'])
        new_project = Project(title=request.form['title'], completion_date=request.form['date'],
                              description=request.form['desc'], skills=request.form['skills'],
                              github=request.form['github'])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('project_detail', id=new_project.id))
    return render_template('projectform.html', projects=projects)


@app.route('/project/<id>/edit', methods=['GET', 'POST'])
def edit_project(id):
    projects = Project.query.all()
    project = Project.query.get_or_404(id)
    if request.form:
        project.title=request.form['title']
        project.completion_date=request.form['date']
        project.description=request.form['description']
        project.skills=request.form['skills']
        project.github=request.form['github']
        db.session.commit()
        return redirect(url_for('project_detail', id=project.id))

    return render_template('editproject.html', project=project, projects=projects)


@app.route('/delete_project/<id>')
def delete_project(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/about')
def about():
    projects = Project.query.all()
    return render_template('about.html', projects=projects)


@app.errorhandler(404)
def not_found(error):
    projects = Project.query.all()
    return render_template('404.html', msg=error, projects=projects)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')
