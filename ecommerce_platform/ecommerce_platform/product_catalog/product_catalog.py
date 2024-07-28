from flask import Flask,redirect

app = Flask(__name__)

@app.route('/')
def index():
    
    return redirect('http://localhost:8000/dashboard/products', code=302)

@app.route('/add', methods=['GET', 'POST'])
def add():
    return 'add Form of Product'  # Placeholder response

@app.route('/remove ', methods=['GET', 'POST'])
def remove():
    return 'remove  Form of Product'  # Placeholder response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
