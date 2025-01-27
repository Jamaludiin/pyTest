import pytest
from student_grade import StudentGrade

class TestStudentGrade:
    @pytest.fixture
    def student(self):
        return StudentGrade()
    
    def test_initial_score(self, student):
        assert student.get_score() == 0
    
    def test_set_and_get_score(self, student):
        student.set_score(85)
        assert student.get_score() == 85
    
    @pytest.mark.parametrize("score,expected_grade", [
        (95, 'A'),
        (85, 'B'),
        (75, 'C'),
        (65, 'D'),
        (55, 'F'),
        (90, 'A'),
        (80, 'B'),
        (70, 'C'),
        (60, 'D'),
        (0, 'F')
    ])
    def test_grade_calculation(self, student, score, expected_grade):
        student.set_score(score)
        assert student.get_grade() == expected_grade