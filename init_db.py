import sqlite3

# Connect to the database (creates students.db if it doesn't exist)
conn = sqlite3.connect('students.db')
cursor = conn.cursor()
import sqlite3
from flask import Flask, jsonify, request, render_template
app = Flask(__name__)
def get_db_connection():
conn = sqlite3.connect(&#39;students.db&#39;)
conn.row_factory = sqlite3.Row
return conn

# Create the students table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT NOT NULL,
    name TEXT NOT NULL,
    program TEXT NOT NULL,
    year INTEGER NOT NULL,
    section TEXT NOT NULL
)
''')

# Clear existing records
cursor.execute("DELETE FROM students")

# Sample student records
students = [
    ('24-00329', 'Eljhon Baxinela', 'BSIT', 3, 'A'),
    ('24-00328', 'Jaya Mekaela Almodiel', 'BSIT', 3, 'A'),
    ('24-00357', 'Mariel Alada', 'BSIT', 3, 'A')
]

# Insert the student records
cursor.executemany('''
INSERT INTO students (student_id, name, program, year, section)
VALUES (?, ?, ?, ?, ?)
''', students)

# Save and close the database
conn.commit()
conn.close()

print("Database created successfully.")