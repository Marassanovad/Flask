from flask import Flask, render_template, make_response, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.session import Session
from flask_wtf.csrf import CSRFProtect
from sqlalchemy.future import engine

from form import RegistrationForm, LoginForm
from models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///account.db'
db.init_app(app)
# app.config['SECRET_KEY'] = 'mysecretkey'
# app.secret_key ='5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'
csrf = CSRFProtect(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.route('/main/')
def main_page():
    context = {'title': 'Main'}
    return render_template('main.html', static_folder="static", **context)


@app.route('/man/')
def man_page():
    context = {'title': 'Man'}
    return render_template('man.html', static_folder="static", **context)


@app.route('/woman/')
def woman_page():
    context = {'title': 'Woman'}
    return render_template('woman.html', static_folder="static", **context)


@app.route('/kid/')
def kids_page():
    context = {'title': 'Kid'}
    return render_template('kid.html', static_folder="static", **context)


@app.route('/accesories/')
def accesories_page():
    context = {'title': 'Accesories'}
    return render_template('accesories.html', static_folder="static", **context)


@app.errorhandler(404)
def page_not_found(e):
    # logger.warning(e)

    context = {'title': 'Page not found =(', 'url': "/main", }
    return render_template('404.html', **context), 404


@app.route('/account/')
def account():
    name = session.get('username')
    if name:
        return render_template('hello_user.html', name=name, title='Account')
    else:
        return redirect('/login')



# @app.route('/login_cookie/', methods=['GET', 'POST'])
# def login_cookie():
#     context = {'title': 'Login'}
#     name = request.cookies.get('name')
#     if name:
#         return render_template('hello_user.html', name=name, title='Account')
#     else:
#         if request.method == 'POST':
#             name = request.form.get('name')
#             email = request.form.get('email')
#             response = make_response(redirect("/"))
#             response.set_cookie('name', name)
#             response.set_cookie('email', email)
#             return response
#         return render_template('login_cookie.html', **context)
# @app.route('/logout_cookie/')
# def logout_cookie():
#     response = make_response(redirect("/"))
#     response.delete_cookie('name')
#     response.delete_cookie('email')
#     return response

# @app.route('/account/')
# def account():
#     name = request.cookies.get('name')
#     if name:
#         return render_template('hello_user.html', name=name, title='Account')
#     else:
#         return redirect('/login')
@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if email == user.email and check_password_hash(user.password, password):
            response = make_response()
            response.set_cookie('name', user.name)
            response.set_cookie('email', email)
            return render_template('hello_user.html', name=user.name, title='Account')
    return render_template('login.html', form=form)


@app.route('/logout/')
def logout():
    response = make_response(redirect("/login"))
    response.delete_cookie('name')
    response.delete_cookie('email')
    return response


@app.cli.command("add-user")
@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        user = User(
            email=form.email.data,
            name=form.name.data,
            surname=form.surname.data,
            password=generate_password_hash(form.password.data)
        )
        db.session.add(user)
        db.session.commit()
        session['username'] = form.name.data
        return redirect(url_for('account'))
    return render_template('register.html', form=form)


@app.route('/users/')
def all_users():
    users = User.query.all()
    context = {'users': users}
    return render_template('users.html', **context)


@app.cli.command("del-user")
def del_user():
    user = User.query.filter_by(name='dash').first()
    db.session.delete(user)
    db.session.commit()


if __name__ == '__main__':
    app.run(debug=True)
