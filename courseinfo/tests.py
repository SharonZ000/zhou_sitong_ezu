from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Period, Year, Semester, Course, Instructor, Student, Section, Registration


class CourseinfoTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="test", email="test@email.com",
            password="{iSchoolUI}"
        )

        cls.period = Period.objects.create(
            period_id="1",
            period_sequence="1",
            period_name="Spring",
        )

        cls.year = Year.objects.create(
            year_id="1",
            year=2023,
        )

        cls.semester = Semester.objects.create(
            semester_id="1",
            year=cls.year,
            period=cls.period,
        )

        cls.course = Course.objects.create(
            course_id="1",
            course_number="IS439",
            course_name="Web Development Using Application Frameworks",
        )

        cls.instructor = Instructor.objects.create(
            instructor_id="1",
            first_name="Kevin",
            last_name="Trainor",
        )

        cls.student = Student.objects.create(
            student_id="1",
            first_name="Sharon",
            last_name="Z",
        )

        cls.section = Section.objects.create(
            section_id="1",
            section_name="AUC",
            semester=cls.semester,
            course=cls.course,
            instructor=cls.instructor,
        )

        cls.registration = Registration.objects.create(
            registration_id="1",
            student=cls.student,
            section=cls.section,
        )

    def test_period_model(self):
        self.assertEqual(str(self.period.period_id), "1")
        self.assertEqual(str(self.period.period_sequence), "1")
        self.assertEqual(self.period.period_name, "Spring")

    def test_year_model(self):
        self.assertEqual(str(self.year.year_id), "1")
        self.assertEqual(self.year.year, 2023)

    def test_semester_model(self):
        self.assertEqual(str(self.semester.semester_id), "1")
        self.assertEqual(str(self.semester.year.year_id), "1")
        self.assertEqual(self.semester.year.year, 2021)
        self.assertEqual(str(self.semester.period.period_id), "1")
        self.assertEqual(str(self.semester.period.period_sequence), "1")
        self.assertEqual(self.semester.period.period_name, "Summer")
        self.assertEqual(self.semester.get_absolute_url(), "/semester/1/")

    def test_course_model(self):
        self.assertEqual(str(self.course.course_id), "1")
        self.assertEqual(str(self.course.course_number), "IS439")
        self.assertEqual(self.course.course_name, "Web Development Using Application Frameworks")
        self.assertEqual(self.course.get_absolute_url(), "/course/1/")

    def test_instructor_model(self):
        self.assertEqual(str(self.instructor.instructor_id), "1")
        self.assertEqual(self.instructor.first_name, "Kevin")
        self.assertEqual(self.instructor.last_name, "Trainor")
        self.assertEqual(self.instructor.get_absolute_url(), "/instructor/1/")

    def test_student_model(self):
        self.assertEqual(str(self.student.student_id), "1")
        self.assertEqual(self.student.first_name, "Sharon")
        self.assertEqual(self.student.last_name, "Z")
        self.assertEqual(self.student.get_absolute_url(), "/student/1/")

    def test_section_model(self):
        self.assertEqual(str(self.section.section_id), "1")
        self.assertEqual(self.section.section_name, "AUC")
        self.assertEqual(str(self.section.semester.semester_id), "1")
        self.assertEqual(str(self.section.semester.year.year_id), "1")
        self.assertEqual(self.section.semester.year.year, 2021)
        self.assertEqual(str(self.section.semester.period.period_id), "1")
        self.assertEqual(str(self.section.semester.period.period_sequence), "1")
        self.assertEqual(self.section.semester.period.period_name, "Summer")
        self.assertEqual(str(self.section.course.course_id), "1")
        self.assertEqual(str(self.section.course.course_number), "IS439")
        self.assertEqual(self.section.course.course_name, "Web Development Using Application Frameworks")
        self.assertEqual(str(self.section.instructor.instructor_id), "1")
        self.assertEqual(self.section.instructor.first_name, "Kevin")
        self.assertEqual(self.section.instructor.last_name, "Trainor")
        self.assertEqual(self.section.get_absolute_url(), "/section/1/")

    def test_registration_model(self):
        self.assertEqual(str(self.registration.registration_id), "1")
        self.assertEqual(str(self.registration.student.student_id), "1")
        self.assertEqual(self.registration.student.first_name, "Sharon")
        self.assertEqual(self.registration.student.last_name, "Z")
        self.assertEqual(str(self.registration.section.section_id), "1")
        self.assertEqual(self.registration.section.section_name, "AUC")
        self.assertEqual(str(self.registration.section.semester.semester_id), "1")
        self.assertEqual(str(self.registration.section.semester.year.year_id), "1")
        self.assertEqual(self.registration.section.semester.year.year, 2021)
        self.assertEqual(str(self.registration.section.semester.period.period_id), "1")
        self.assertEqual(str(self.registration.section.semester.period.period_sequence), "1")
        self.assertEqual(self.registration.section.semester.period.period_name, "Summer")
        self.assertEqual(str(self.registration.section.course.course_id), "1")
        self.assertEqual(str(self.registration.section.course.course_number), "IS439")
        self.assertEqual(self.registration.section.course.course_name, "Web Development Using Application Frameworks")
        self.assertEqual(str(self.registration.section.instructor.instructor_id), "1")
        self.assertEqual(self.registration.section.instructor.first_name, "Kevin")
        self.assertEqual(self.registration.section.instructor.last_name, "Trainor")
        self.assertEqual(self.registration.get_absolute_url(), "/registration/1/")

    def test_instructor_list_view(self):
        response = self.client.get("/instructor/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Trainor")
        self.assertTemplateUsed(response, "courseinfo/instructor_list.html")

    def test_instructor_detail_view(self):
        response = self.client.get("/instructor/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Trainor")
        self.assertTemplateUsed(response, "courseinfo/instructor_detail.html")

    def test_section_list_view(self):
        response = self.client.get("/section/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "AUC")
        self.assertTemplateUsed(response, "courseinfo/section_list.html")

    def test_section_detail_view(self):
        response = self.client.get("/section/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "AUC")
        self.assertTemplateUsed(response, "courseinfo/section_detail.html")

    def test_course_list_view(self):
        response = self.client.get("/course/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "IS439")
        self.assertTemplateUsed(response, "courseinfo/course_list.html")

    def test_course_detail_view(self):
        response = self.client.get("/course/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "IS439")
        self.assertTemplateUsed(response, "courseinfo/course_detail.html")

    def test_semester_list_view(self):
        response = self.client.get("/semester/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "1")
        self.assertTemplateUsed(response, "courseinfo/semester_list.html")

    def test_semester_detail_view(self):
        response = self.client.get("/course/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "IS439")
        self.assertTemplateUsed(response, "courseinfo/course_detail.html")

    def test_student_list_view(self):
        response = self.client.get("/student/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sharon")
        self.assertTemplateUsed(response, "courseinfo/student_list.html")

    def test_student_detail_view(self):
        response = self.client.get("/student/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sharon")
        self.assertTemplateUsed(response, "courseinfo/student_detail.html")

    def test_registration_list_view(self):
        response = self.client.get("/registration/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "1")
        self.assertTemplateUsed(response, "courseinfo/registration_list.html")

    def test_registration_detail_view(self):
        response = self.client.get("/registration/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "1")
        self.assertTemplateUsed(response, "courseinfo/registration_detail.html")