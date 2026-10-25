
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/student')
def get_student():
    return jsonify({
        "student_id": "24-00329",
        "name": "Eljhon Baxinela",
        "program": "BSIT",
        "year": 3,
        "section": "A"
    })


@app.route('/hello')
def say_hello():
    name = request.args.get('name', 'Student').strip()

    if not name:
        name = 'Student'

    return jsonify({
        "message": f"Hello, {name}!"
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

@app.route(&#39;/students&#39;)
def get_students():
conn = get_db_connection()
students = conn.execute(&#39;SELECT * FROM students&#39;).fetchall()
conn.close()
return jsonify([dict(student) for student in students])
