import os
import sqlite3

from flask import Flask, render_template, request, redirect, url_for, flash, session
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
# config pro https nasazení 
# app.config['SESSION_COOKIE_SECURE'] = True
# app.config['SESSION_COOKIE_HTTPONLY'] = True


# App routing
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        connection = sqlite3.connect('dochazka.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users WHERE login_name = ? AND user_password = ?', (username, password))
        user = cursor.fetchone()

        if user is not None:
            session['user_id'] = user[0]
            return redirect(url_for('user_profile', user_id=user[0]))
        else:
            flash('Nesprávné uživatelské jméno nebo heslo.')            
    return render_template('login.html')

@app.route('/user/<int:user_id>')
def user_profile(user_id):
    if 'user_id' not in session or session['user_id'] != user_id:
        return "Neautorizovaný přístup!!", 403

    connection = sqlite3.connect('dochazka.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    if user is None:
        return "Uživatel neexistuje, obraťte se na správce systému", 404
    return render_template('user_profile.html', user=user) 

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/user_list')
def users():
    connection = sqlite3.connect('dochazka.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    return render_template('user_list.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)