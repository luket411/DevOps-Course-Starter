from flask import Flask
from flask import render_template, request, redirect

from os import environ

from todo_app.flask_config import Config
from todo_app.data.trello_interface import get_items, add_item, change_ticket_list
from todo_app.data.ViewModel import ViewModel


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    @app.route('/', methods=['GET'])
    def index():
        view_model = ViewModel(get_items())
        prod_flag = "" if "IS_PROD" in environ else "Development"
        return render_template('index.html', view_model=view_model, prod_flag=prod_flag)

    @app.route('/', methods=['POST'])
    def create_item():
        add_item(request.form.get('title'))
        return redirect("/")

    @app.route('/complete-item/<id>')
    def complete_item(id):
        change_ticket_list(id, "Done")
        return redirect("/")

    @app.route('/reopen-item/<id>')
    def reopen_item(id):
        change_ticket_list(id, "Doing")
        return redirect("/")

    return app
