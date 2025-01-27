class StudentGrade:
    """
    A class to calculate student grades based on scores.
    
    Score criteria:
    - Score >= 90 -> "A"
    - Score >= 80 -> "B"
    - Score >= 70 -> "C"
    - Score >= 60 -> "D"
    - Score < 60  -> "F"
    """
    
    def __init__(self):
        self._score = 0
        self._grade = 'A'
    
    def set_score(self, score: int) -> None:
        """Set the student's score."""
        self._score = score
    
    def get_score(self) -> int:
        """Get the student's score."""
        return self._score
    
    def get_grade(self) -> str:
        """Calculate and return the student's grade based on their score."""
        if self._score >= 90:
            self._grade = 'A'
        elif self._score >= 80:
            self._grade = 'B'
        elif self._score >= 70:
            self._grade = 'C'
        elif self._score >= 60:
            self._grade = 'D'
        else:
            self._grade = 'F'
        
        return self._grade


if __name__ == "__main__":
    # Example usage
    student_grade = StudentGrade()
    student_grade.set_score(95)
    print(student_grade.get_grade())  # Output: A