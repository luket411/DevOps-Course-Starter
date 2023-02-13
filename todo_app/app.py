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
        items = [f"#{item['id']} {item['status']} - {item['title']}" for item in get_items()]
        return render_template('index.html', items=items)

@app.route('/', methods=['POST'])
def create_item():
    add_item(request.form.get('title'))
    return redirect("/")
