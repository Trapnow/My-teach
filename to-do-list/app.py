from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_code = db.Column(db.String(100), nullable=False)
    telephone = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    level_secret = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Agent {self.name_code}>"


with app.app_context():
    db.create_all()


@app.route('/')
@app.route('/list_agents')
def get_agents():
    query = request.args.get('filter_text', '')

    if query:
        agents = Agent.query.filter(
            Agent.name_code.ilike(f'%{query}%')
        ).all()
    else:
        agents = Agent.query.all()

    has_agents = len(agents) > 0

    return render_template("list_agents.html", agents=agents, filter_text=query, has_agents=has_agents)


@app.route('/add', methods=['GET', 'POST'])
def add_agents():
    if request.method == 'POST':
        name_code = request.form['name_code']
        telephone = request.form['telephone']
        email = request.form['email']
        level_secret = request.form['level_secret']
        new_agent = Agent(name_code=name_code, telephone=telephone, email=email, level_secret=level_secret)
        db.session.add(new_agent)
        db.session.commit()
        return redirect(url_for('get_agents'))
    return render_template('list_agents.html')


@app.route('/delete/<int:id>')
def delete_agent(id):
    task = Agent.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('get_agents'))


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_agent(id):
    agent = Agent.query.get_or_404(id)  # Получаем задачу по ID
    if request.method == 'POST':
        new_name_code = request.form['name_code']
        new_telephone = request.form['telephone']
        new_email = request.form['email']
        new_level_secret = request.form['level_secret']
        agent.name_code = new_name_code
        agent.telephone = new_telephone
        agent.email = new_email
        agent.level_secret = new_level_secret
        db.session.commit()
        return redirect(url_for('get_agents'))
    return render_template('edit_agent.html', agent=agent)

@app.route('/clear-database', methods=['POST'])
def clear_database():
    if request.method == 'POST':
        confirm = request.form.get('confirm')
        if confirm == 'yes':
            # Удаляем все записи
            db.session.query(Agent).delete()
            db.session.commit()
    return redirect(url_for('get_agents'))


if __name__ == "__main__":
    app.run(debug=True)
