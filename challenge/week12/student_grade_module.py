from Student import *   # import Student Class and load_student_data function

# Main function
def main():
    file_path = 'student.csv'

    # Save student grades to dictionaries
    student_data = load_student_data(file_path)

    # Print out the average score of each student's grade
    print("-----학생들의 평균 점수-----")
    for name, student in student_data.items():   # Get the student's name and object using a 'for' statement
        average_score = student.get_average()  # Calculate the average score for each student
        print(f"{name}의 평균 점수는 {average_score} 입니다.")
        
    # Save average scores to a file (average.txt)
    with open('average.txt', 'w') as output_file:   # Create a file 'average.txt' with write mode
        output_file.write("-----학생들의 평균 점수-----\n")
        for name, student in student_data.items():   # Get the student's name and object using a 'for' statement
            average_score = student.get_average()   # Calculate the average score 
            output_file.write(f"{name}의 평균 점수는 {average_score} 입니다.\n")    # Write the average score to 'average.txt'

# Call the main function
if __name__ == "__main__":
    main()

