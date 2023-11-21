# Student Class
class Student:
    def __init__(self, name, korean, math, english):
        # Constructor (initializer) for the Student class
        # Initializes the student with a name, Korean, Math, English scores
        self.name = name  # Student's name
        self.korean = korean  # Student's Korean score
        self.math = math  # Student's Math score
        self.english = english  # Student's English score

    def get_average(self):
        # Calculate and return the average of the student's scores
        return (self.korean + self.math + self.english) / 3

# Load the student's data 
def load_student_data(file_path):
    student_data = {}  # Generate an empty dictionary
    with open(file_path, 'r') as file: # Open the file with read mode
        lines = file.readlines()   # Read all lines of the file into a list # Read all lines of the file into a list
        for line in lines[1:]:  # Iterate over each line, excluding the header
            elements = line.strip().split(',')  # Split the line into elements using ','
            name = elements[0]    # Get the name from the elements
            scores = list(map(float, elements[1:]))   # Map the scores to float types
            # Create a Student object and store it in the dictionary
            student_data[name] = Student(name, *scores)  
    return student_data   # Return a dictionary of Student objects
