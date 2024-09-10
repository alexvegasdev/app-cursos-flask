import requests

class CourseService:
    BASE_URL = 'https://api-seminario-production.up.railway.app/api'
    END_POINT = '/courses'
    
    def get_course(self, course_id):
        response = requests.get(f"{self.BASE_URL}/courses/{course_id}")
        return response.json()

    def get_courses(self):
        courses = requests.get(self.BASE_URL + self.END_POINT)
        return courses.json()

    def add_course(self, course):
        return None

    def update_course(self, course_id, course):
        return None

    def delete_course(self, course_id):
        return None