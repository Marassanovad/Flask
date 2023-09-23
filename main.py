from flask import Flask, render_template, make_response, request, session, redirect, url_for


app = Flask(__name__)
app.secret_key ='5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'

# @app.route('/')
# def html_base():
#     context = {'title': 'Base'}
#     return render_template('base.html', static_folder="static", **context)

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


@app.route('/')
def index():
    name = request.cookies.get('name')
    if name:
        return render_template('hello_user.html', name=name, title='Account')
    else:
        return redirect('/login')
@app.route('/login/', methods=['GET', 'POST'])
def login():
    context = {'title': 'Login'}
    name = request.cookies.get('name')
    if name:
        return render_template('hello_user.html', name=name, title='Account')
    else:
        if request.method == 'POST':
            name = request.form.get('name')
            email = request.form.get('email')
            response = make_response(redirect("/"))
            response.set_cookie('name', name)
            response.set_cookie('email', email)
            return response
        return render_template('login.html', **context)
@app.route('/logout/')
def logout():
    response = make_response(redirect("/"))
    response.delete_cookie('name')
    response.delete_cookie('email')
    return response


if __name__ == '__main__':
    app.run(debug=True)
