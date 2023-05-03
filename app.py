from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

to_do_list = []

@app.route('/')
def index():
    return render_template('index.html', to_do_list=to_do_list)

@app.route('/add', methods=['POST'])
def add():
    new_item = request.form['new_item']
    to_do_list.append(new_item)
    return redirect(url_for('index'))

@app.route('/complete', methods=['POST'])
def complete():
    index = int(request.form['index'])
    to_do_list.pop(index)
    return redirect(url_for('index'))

@app.route('/remove', methods=['POST'])
def remove():
    task = request.form['task']
    to_do_list.remove(task)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)