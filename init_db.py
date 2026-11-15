
import sqlite3
import sqlite3

# Connect to database
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Create students table
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

# Delete previous records
cursor.execute("DELETE FROM students")

# Student records
students = [
    ('2024-00111', 'Jm Abordaje', 'BSIT', 3, 'A'),
    ('2024-00286', 'Necole Andrea Aloro', 'BSIT', 3, 'A'),
    ('2024-00179', 'John Michel Bautista', 'BSIT', 3, 'A')
]

# Insert records
cursor.executemany('''
INSERT INTO students (student_id, name, program, year, section)
VALUES (?, ?, ?, ?, ?)
''', students)

# Save and close
conn.commit()
conn.close()

print("Database created successfully!")
print("3 student records inserted successfully!")
