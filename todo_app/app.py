from flask import Flask
from flask import render_template, request, redirect

from todo_app.flask_config import Config
from todo_app.data.session_items import get_items, add_item

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
