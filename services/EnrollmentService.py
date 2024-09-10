import requests

class EnrollmentService:
    BASE_URL = 'https://api-seminario-production.up.railway.app/api'
    END_POINT = ''
    
    def get_enrollments_by_course(self):
        return None

    def get_enrollments_by_student(self, student_id):
        return None

    def enroll_student_in_course(self, student_id, course_id):
        return None
    
    def enroll_student(self, course_id, student_id):
        # Realizar la solicitud POST para inscribir al estudiante en el curso
        response = requests.post(
            f"{self.BASE_URL}/courses/{course_id}/students",
            json={'student_id': student_id}
        )
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None