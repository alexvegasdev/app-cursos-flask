import requests

class StudentService:
    BASE_URL = 'https://api-seminario-production.up.railway.app/api'
    END_POINT = '/students'
    
    def get_student(self, student_title):
        return None

    def get_students(self):
        students = requests.get(self.BASE_URL + self.END_POINT)
        return students.json()

    def add_student(self, student):
        return None

    def update_student(self, student_id, student):
        return None

    def delete_student(self, student_id):
        return None