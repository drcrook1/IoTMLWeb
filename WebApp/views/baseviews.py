from flask import render_template, url_for, Blueprint, redirect, flash, request, current_app, send_from_directory

baseviews = Blueprint('baseviews', __name__)

@baseviews.route('/')
@baseviews.route('/index')
def index():
    return render_template('index.html')
