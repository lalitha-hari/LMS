import unittest
from app import app
from bs4 import BeautifulSoup

class TestFlaskApp(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_login_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.data, 'html.parser')
        self.assertIsNotNone(soup.find('form', id='login-form'))
    
    def test_process_student_login_correct_id(self):
        response = self.app.post('/process_student_login', data=dict(
            username='student_user',
            userId='1',
            password='password'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.data, 'html.parser')
        self.assertIsNotNone(soup.find('h1', text='User Dashboard'))
    
    def test_process_teacher_login_correct_id(self):
        response = self.app.post('/process_teacher_login', data=dict(
            username='teacher_user',
            teacherId='24',
            password='password'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.data, 'html.parser')
        self.assertIsNotNone(soup.find('h1', text='Teacher Dashboard'))

if __name__ == '__main__':
    unittest.main()
