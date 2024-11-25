from flask import blueprint, render_tempalte

auth = blueprint('auth', __name__)

@auth.route('/signup')
def signup():
    return "page for sign up"

@auth.route('/login')
def login():
    return "page for login"

if __name__ == "main":
    app.run(debug=True)