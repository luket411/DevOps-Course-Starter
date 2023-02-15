from flask import Flask
from flask import render_template, request, redirect

from dotenv import load_dotenv

from todo_app.flask_config import Config
from todo_app.data.trello_items import get_items, add_item

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/', methods=['GET'])
def index():
    all_items = get_items()
    open_items = [item for item in all_items if item['status'] == "To Do"]
    completed_items = [item for item in all_items if item['status'] == "Done"]
    return render_template('index.html', open_items=open_items, complete_items=completed_items)

@app.route('/', methods=['POST'])
def create_item():
    add_item(request.form.get('title'))
    return redirect("/")
