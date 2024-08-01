from flask import Flask, request, redirect, url_for, render_template
import sqlite3

app = Flask(__name__)

DATABASE = '/data/database.db'

def connect_db():
    return sqlite3.connect(DATABASE)

@app.route('/')
def index():
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT * FROM persons")
    persons = c.fetchall()
    conn.close()
    return render_template('index.html', persons=persons)

@app.route('/add', methods=['POST'])
def add_person():
    name = request.form['name']
    phone = request.form['phone']
    conn = connect_db()
    c = conn.cursor()
    c.execute("INSERT INTO persons (name, phone) VALUES (?, ?)", (name, phone))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
