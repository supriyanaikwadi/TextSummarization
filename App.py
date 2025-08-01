
App.py
from flask import Flask, request,  jsonify, render_template, redirect, url_for,session, flash
from transformers import pipeline
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here' 

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'users.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    with app.app_context():
      db.create_all()

    

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        password = request.form['password']

        # Check if user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('User already exists! Please login.', 'error')
            return redirect(url_for('login'))

        new_user = User(fullname=fullname, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email, password=password).first()
        if user:
            session['user_id'] = user.id
            session['user_name'] = user.fullname
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials. Try again.', 'error')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', name=session['user_name'])
# Load the summarization model
summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base", framework="pt")

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data.get("text", "")

    if not text.strip():
        return jsonify({"summary": "No text provided."})
    
    try:
        result = summarizer(text, max_length=100, min_length=10, do_sample=False)
        return jsonify({"summary": result[0]["summary_text"]})
    except Exception as e:
        return jsonify({"summary": f"Error: {str(e)}"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Creates users.db with User table
    app.run(debug=True)



