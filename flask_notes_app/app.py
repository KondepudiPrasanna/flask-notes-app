from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Store notes in a list
notes = []

@app.route('/')
def home():
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['POST'])
def add_note():
    """ Add a new note """
    note = request.form.get('note')
    if note:
        notes.append(note)
    return redirect('/')

@app.route('/delete/<int:index>')
def delete_note(index):
    """ Delete a selected note """
    if 0 <= index < len(notes):
        notes.pop(index)
    return redirect('/')

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_note(index):
    """ Edit an existing note """
    if request.method == 'POST':
        updated_note = request.form.get('note')
        if updated_note:
            notes[index] = updated_note
        return redirect('/')
    return render_template('edit.html', note=notes[index], index=index)

if __name__ == '__main__':
    app.run(debug=True)
