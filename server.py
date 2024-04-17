from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Define your routes
@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/process_student_login', methods=['POST'])
def process_student_login():
    # Extract student login credentials from the request
    username = request.form.get('username')
    userId = request.form.get('userId')
    password = request.form.get('password')
    user_id=1

    # Redirect to student dashboard
    return redirect(url_for('user_dashboard', user_id=userId))



@app.route('/process_teacher_login', methods=['POST'])
def process_teacher_login():
    # Extract teacher login credentials from the request
    username = request.form.get('username')
    teacherId = request.form.get('teacherId')
    teacher_id=24

    # Assuming validation of username and teacherId is done in frontend
    # Directly redirect to teacher dashboard
    return redirect(url_for('teacher_dashboard', teacher_id=teacherId))

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
