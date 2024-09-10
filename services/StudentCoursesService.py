import requests

class StudentCoursesService:
    BASE_URL = 'https://api-seminario-production.up.railway.app/api'
    
    @classmethod
    def get_courses_by_student(cls, student_id):
        response = requests.get(f"{cls.BASE_URL}/students/{student_id}/courses")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None
