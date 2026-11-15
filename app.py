

from flask import Flask, jsonify, request, render_template
import sqlite3

app = Flask(__name__)

DATABASE = "students.db"


# Database connection
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# Home page
@app.route('/')
def home():
    return render_template('index.html')


# Get individual student information
@app.route('/student')
def get_student():
    return jsonify({
        "student_id": "24-00329",
        "name": "Eljhon Baxinela",
        "program": "BSIT",
        "year": 3,
        "section": "A"
    })


# Hello endpoint
@app.route('/hello')
def say_hello():
    name = request.args.get('name', 'Student').strip()

    if not name:
        name = 'Student'

    return jsonify({
        "message": f"Hello, {name}!"
    })


# Get all students
@app.route('/students')
def get_students():
    conn = get_db_connection()

    students = conn.execute(
        'SELECT * FROM students'
    ).fetchall()

    conn.close()

    return jsonify([dict(student) for student in students])


# Get student by ID
@app.route('/students/<int:id>')
def get_student_by_id(id):
    conn = get_db_connection()

    student = conn.execute(
        'SELECT * FROM students WHERE id = ?',
        (id,)
    ).fetchone()

    conn.close()

    if student is None:
        return jsonify({
            "error": "Student not found"
        }), 404

    return jsonify(dict(student))


# Get students by section
@app.route('/students/section/<section>')
def get_students_by_section(section):
    conn = get_db_connection()

    

    conn.close()

    return jsonify([dict(student) for student in students])


# Run Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
