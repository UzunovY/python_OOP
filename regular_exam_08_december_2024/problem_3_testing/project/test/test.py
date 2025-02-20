from unittest import TestCase, main

from project.senior_student import SeniorStudent


class TestSeniorStudent(TestCase):

    def setUp(self):
        self.s_s = SeniorStudent("1234", "Jo", 1.1)

    def test_init_method_initializing_an_object_with_correct_data(self):
        self.assertEqual("1234", self.s_s.student_id)
        self.assertEqual("Jo", self.s_s.name)
        self.assertEqual(1.1, self.s_s.student_gpa)
        self.assertEqual(set(), self.s_s.colleges)

    def test_student_id_setter_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.s_s.student_id = "123 "
        self.assertEqual("Student ID must be at least 4 digits long!", str(ve.exception))

    def test_name_setter_with_empty_and_null_name_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.s_s.name = ""
        self.assertEqual("Student name cannot be null or empty!", str(ve.exception))
        with self.assertRaises(ValueError) as ve:
            self.s_s.name = "       "
        self.assertEqual("Student name cannot be null or empty!", str(ve.exception))

    def test_student_gpa_setter_with_value_equal_or_less_than_required_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.s_s.student_gpa = 1.0
        self.assertEqual("Student GPA must be more than 1.0!", str(ve.exception))
        with self.assertRaises(ValueError) as ve:
            self.s_s.student_gpa = 0.9
        self.assertEqual("Student GPA must be more than 1.0!", str(ve.exception))

    def test_apply_to_college_with_less_than_required_gpa(self):
        apply = self.s_s.apply_to_college(6.0, "SoftUni")
        self.assertEqual('Application failed!', apply)

    def test_apply_to_college_with_enough_gpa(self):
        apply = self.s_s.apply_to_college(1.1, "Div_Dyadovo")
        self.assertEqual({"DIV_DYADOVO"}, self.s_s.colleges)
        self.assertEqual("Jo successfully applied to Div_Dyadovo.", apply)

    def test_update_gpa_to_less_than_or_equal_to_required(self):
        self.assertEqual('The GPA has not been changed!', self.s_s.update_gpa(1.0))
        self.assertEqual('The GPA has not been changed!', self.s_s.update_gpa(0.9))

    def test_update_gpa_with_correct_amount_compared_with_required(self):
        update_gpa = self.s_s.update_gpa(2.5)
        self.assertEqual(2.5, self.s_s.student_gpa)
        self.assertEqual('Student GPA was successfully updated.', update_gpa)

    def test_equality_method_comparing_with_another_student_object(self):
        new_student = SeniorStudent("6545", "Mo", 1.1)
        self.assertEqual(True, self.s_s == new_student)
        new_student.student_gpa = 2.0
        self.assertEqual(False, self.s_s == new_student)


if __name__ == "__main__":
    main()
