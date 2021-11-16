"""
Project 9.1
Resources to manage a student's name and test scores.
Includes methods for comparisons and testing for equality.
"""

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name

    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]

    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)

    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)

    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name + "\nScores: " + \
               " ".join(map(str, self.scores))

    # Write method definitions here

    def __lt__(self, other):
        """Returns self < other, with respect
        to names."""
        return self.name < other.name

    def __ge__(self, other):
        """Returns self >= other, with respect
        to names."""
        return self.name >= other.name

    def __eq__(self, other):
        """Tests for equality."""
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.name == other.name

def main():
    """A simple test."""
    student = Student("Ken", 5)
    print(student)
    for i in range(1, 6):
        student.setScore(i, 100)
    print(student)

if __name__ == "__main__":
    main()
