from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# PostgreSQL configurations
DB_HOST = 'localhost'
DB_NAME = 'lms'
DB_USER = 'username'
DB_PASSWORD = 'lalithahari'

# Define your routes and functions
@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/process_student_login', methods=['POST'])
def process_student_login():
    # Extract student login credentials from the request
    data = request.json
    username = data.get('username')
    password = data.get('password')
    userId = data.get('userId')

    # Your student login authentication code here
    # You might want to validate the credentials against your database

    # Assuming authentication is successful, redirect to student dashboard
    return jsonify(success=True)

@app.route('/process_teacher_login', methods=['POST'])
def process_teacher_login():
    # Extract teacher login credentials from the request
    data = request.json
    username = data.get('username')
    password = data.get('password')
    teacherId = data.get('teacherId')

    # Your teacher login authentication code here
    # You might want to validate the credentials against your database

    # Assuming authentication is successful, redirect to teacher dashboard
    return jsonify(success=True)

@app.route('/user_dashboard/<int:user_id>')
def user_dashboard(user_id):
    # Render the user dashboard template with the user_id
    return render_template('user_dashboard.html', user_id=user_id)

@app.route('/teacher_dashboard/<int:teacher_id>')
def teacher_dashboard(teacher_id):
    # Render the teacher dashboard template with the teacher_id
    return render_template('teacher_dashboard.html', teacher_id=teacher_id)

if __name__ == '__main__':
    app.run(debug=True)
