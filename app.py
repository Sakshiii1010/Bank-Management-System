from flask import Flask, render_template, request, redirect, url_for
import database  # Your existing database file

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        success = database.create_user(username, password)
        if success:
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if database.authenticate(username, password):
            return redirect(url_for('dashboard', user=username))
    return render_template('login.html')

@app.route('/dashboard/<user>')
def dashboard(user):
    balance = database.check_balance(user)
    return render_template('dashboard.html', username=user, balance=balance)

if __name__ == '__main__':
    app.run(debug=True)
