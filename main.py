from flask import Flask, request
import flask
import pyvibe as pv
import pycob as cob
import uuid
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    page = pv.Page('Home')

    with page.add_card() as card:
        card.add_header('Enter some data')
        with card.add_form(action="/save", method="POST") as form:
            form.add_formtext(label="Name", name="name", placeholder="Enter your name")
            form.add_formtextarea(label="Message", name="message", placeholder="Enter your message")
            form.add_formsubmit(label="Save")

    return page.to_html()

@app.route('/save', methods=['POST'])
def save():
    name = flask.request.form.get('name')
    message = flask.request.form.get('message')

    id = uuid.uuid4().hex
    cob.store_dict('messages', id, {'id': id, 'name': name, 'message': message})

    page = pv.Page('Saved')
    page.add_header('Your message has been saved')
    page.add_text('PyVibe is used for illustration purposes. You can use any HTML templating engine you like.')
    page.add_code('import pycob as cob', header="Import pycob")
    page.add_code('''cob.store_dict('messages', uuid.uuid4().hex, {'name': name, 'message': message})''', header="Store dictionary")        
    page.add_link('View messages', '/list')

    return page.to_html()

@app.route('/list')
def list():
    messages = cob.list_objects('messages')

    page = pv.Page('Messages')
    page.add_header('Messages')
    page.add_code('import pycob as cob', header="Import pycob")
    page.add_code('''messages = cob.list_objects('messages')''', header="List objects")

    action_buttons = [
        pv.Rowaction(label='Delete', url='/delete?id={id}', open_in_new_window=False)
    ]

    page.add_pandastable(pd.DataFrame(messages), action_buttons=action_buttons)
    page.add_link('Add message', '/')

    return page.to_html()


@app.route('/delete')
def delete():
    id = flask.request.args.get('id')
    cob.delete_dict('messages', id)

    page = pv.Page('Deleted')
    page.add_header('Your message has been deleted')
    page.add_code('import pycob as cob', header="Import pycob")
    page.add_code('''cob.delete_dict('messages', id)''', header="Delete dictionary")
    page.add_link('View messages', '/list')

    return page.to_html()

if __name__ == '__main__':
    app.run(debug=True)
