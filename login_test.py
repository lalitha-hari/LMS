import pytest
from app import app
from bs4 import BeautifulSoup

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_login_page(client):
    response = client.get('/')
    soup = BeautifulSoup(response.data, 'html.parser')
    assert soup.title.string == "Login Page"

def test_process_student_login(client):
    response = client.post('/process_student_login', data=dict(username='testuser', userId='1', password='password'), follow_redirects=True)
    soup = BeautifulSoup(response.data, 'html.parser')
    assert soup.title.string == "User Dashboard"

def test_process_teacher_login(client):
    response = client.post('/process_teacher_login', data=dict(username='teacher', teacherId='24'), follow_redirects=True)
    soup = BeautifulSoup(response.data, 'html.parser')
    assert soup.title.string == "Teacher Dashboard"

def test_user_dashboard(client):
    response = client.get('/user_dashboard/1')
    soup = BeautifulSoup(response.data, 'html.parser')
    assert soup.title.string == "User Dashboard"

def test_teacher_dashboard(client):
    response = client.get('/teacher_dashboard/24')
    soup = BeautifulSoup(response.data, 'html.parser')
    assert soup.title.string == "Teacher Dashboard"

if __name__ == "__main__":
    pytest.main()
