from flask import blueprint, render_template

main = blueprint('main', __name__)

@main.route('/')
def index():
    return 'hello world'

@main.route('/')
def profile():
    return 'profile here! '