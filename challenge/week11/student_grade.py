class Student:
    def __init__(self, name, korean, math, english):
        # Constructor (initializer) for the Student class
        # Initializes the student with a name, Korean, Math, English scores
        self.name = name        # Student's name
        self.korean = korean    # Student's Korean score
        self.math = math        # Student's Math score
        self.english = english  # Student's English score

    def get_average(self):
        # Calculate and return the average of the student's scores
        return (self.korean + self.math + self.english) / 3

# Load the student's data 
def load_student_data(file_path):
    student_data = {}  # Generate an empty dictionary
    with open(file_path, 'r') as file:  # Open the file with read mode
        lines = file.readlines()  # Read all lines of the file into a list
        for line in lines[1:]:  # Iterate over each line, excluding the header
            elements = line.strip().split(',')   # Split the line into elements using ','
            name = elements[0]   # Get the name from the elements
            scores = list(map(float, elements[1:]))  # Map the scores to float types
            # Create a Student object and store it in the dictionary
            student_data[name] = Student(name, *scores)
    return student_data   # Return a dictionary of Student objects

# Receive a list of numbers and return the average
def get_average(numbers):
    return sum(numbers) / len(numbers)   # Calculate the average

# Main function
def main():
    file_path = 'student.csv'

    # Save student grades to dictionaries
    student_data = load_student_data(file_path)

    # Print out the average score of each student's grade
    print("-----학생들의 평균 점수-----")
    for name, student in student_data.items():  # Get the student's name and object using a 'for' statement
        average_score = student.get_average()  # Calculate the average score for each student
        print(f"{name}의 평균 점수는 {average_score} 입니다.")

    # Save average scores to a file (average.txt)
    with open('average.txt', 'w') as output_file:  # Create a file 'average.txt' with write mode
        output_file.write("-----학생들의 평균 점수-----\n")
        for name, student in student_data.items():  # Get the student's name and object using a 'for' statement
            average_score = student.get_average()  # Calculate the average score 
            output_file.write(f"{name}의 평균 점수는 {average_score} 입니다.\n")  # Write the average score to 'average.txt'

# Call the main function
if __name__ == "__main__":
    main()

