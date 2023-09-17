from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def html_base():
    context = {'title': 'Base'}
    return render_template('base.html', static_folder="static", **context)

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


if __name__ == '__main__':
    app.run(debug=True)
