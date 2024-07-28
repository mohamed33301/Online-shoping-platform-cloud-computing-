from flask import Flask, request, jsonify, render_template ,redirect
import psycopg2


DB_NAME = "productDb"
DB_USER = "admin"
DB_PASSWORD = "admin1234"
DB_HOST = "localhost"

app = Flask(__name__)

# Function to get database connection
def get_connection():
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
    return conn

@app.route('/')
def index():
    
    return redirect('http://localhost:8000/', code=302)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
