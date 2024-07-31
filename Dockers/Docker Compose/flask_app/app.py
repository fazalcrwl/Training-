from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="db",  # Service name defined in docker-compose.yml
        database="mydatabase",
        user="myuser",
        password="mypassword"
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT name, phone FROM persons')
    persons = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', persons=persons)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Listen on all network interfaces
