from flask import Flask, render_template, request
from sqlalchemy import Column, Integer, String, Numeric, create_engine, text
import mysql.connector
app = Flask(__name__)
conn_str = 'mysql://root:Rangers1@localhost/exam'
engine = create_engine(conn_str, echo=True)
conn = engine.connect()


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/account', methods=["GET"])
def account():
    return render_template('account.html')


@app.route('/account', methods=["POST"])
def account_2():
    conn.execute(text("insert into accounts (password, first_name, last_name, account_type) values (:password, :fname, :lname, :type)"), request.form)
    conn.commit()
    return render_template('account.html')


@app.route('/teachers', methods=["GET"])
def teachers():
    teachers = conn.execute(text("select * from accounts where account_type = 'teacher';")).all()
    return render_template('teachers.html', teachers=teachers)


@app.route('/students', methods=["GET"])
def students():
    students = conn.execute(text("select * from accounts where account_type = 'student';")).all()
    return render_template('students.html', students=students)


@app.route('/tests', methods=["GET"])
def tests():
    return render_template('tests.html')


@app.route('/tests', methods=["POST"])
def tests_2():
    tests = conn.execute(text("select * from tests;")).all()
    return render_template('tests.html', tests=tests)


# all tests display/create/edit/delete page
# test take (form with all questions); student account


if __name__ == '__main__':
    app.run(debug=True)


