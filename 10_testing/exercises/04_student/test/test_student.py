from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.student = Student("Test Student", {"Math": []})

    def test_init_correct_initialization_with_existing_course(self):
        self.assertEqual("Test Student", self.student.name)
        self.assertEqual({"Math": []}, self.student.courses)

    def test_init_correct_initialization_without_existing_courses(self):
        student = Student("New Student")
        self.assertEqual("Test Student", self.student.name)
        self.assertEqual({}, student.courses)

    def test_enroll_student_with_existing_course(self):
        enroll = self.student.enroll("Math", [1], "N")
        self.assertEqual({"Math": [1]}, self.student.courses)
        self.assertEqual("Course already added. Notes have been updated.", enroll)

    def test_enroll_student_with_a_new_course(self):
        enroll = self.student.enroll("Music", [1], "Y")
        self.assertEqual({"Math": [], "Music": [1]}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", enroll)
        new_enroll = self.student.enroll("Test", [1, 2])
        self.assertEqual({"Math": [], "Music": [1], "Test": [1, 2]}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", new_enroll)

    def test_enroll_student_to_a_new_course_without_notes(self):
        enroll = self.student.enroll("Music", [1], "N")
        self.assertEqual({"Math": [], "Music": []}, self.student.courses)
        self.assertEqual("Course has been added.", enroll)

    def test_add_notes_to_an_existing_course(self):
        self.assertEqual({"Math": []}, self.student.courses)
        add_note = self.student.add_notes("Math", 1)
        self.assertEqual({"Math": [1]}, self.student.courses)
        self.assertEqual("Notes have been updated", add_note)

    def test_add_notes_to_not_existing_course_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Music", 1)

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_when_course_exists(self):
        leave_course = self.student.leave_course("Math")
        self.assertEqual({}, self.student.courses)
        self.assertEqual("Course has been removed", leave_course)

    def test_leave_course_when_course_does_not_exists_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Music")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()
