# Worksheet 1.3: Task 3

# Your code for the overall grade classification

# ask for filename of the student file

# open the file

# read in the data, and for each student calculate their average grade and classification



# write out this calculated data in the format without a header:
#      student_id,average_grade,classification - replace this with actual value
#      The average grade should be given to 2 decimal places
#      this can be achieved by using the following in an fstring: {variable_name:.2f}


# write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

# You can compare your output files with the 4 example files in example_outfiles folder

filename = input("Enter student filename: ")

try:
    with open(filename, "r") as file:
        data = file.readlines()

    results = []
        



    for row in data[1:]:
           student = row.strip().split(",")
           student_id = student[0]
           grades = student[1:]
           print(student_id, grades)



           grade_values = [float(grade) for grade in grades]
           average = sum(grade_values) / len(grade_values)
           print(student_id, f"{average:.2f}")


           if average >= 70:
               classiification = "Distiction"
           elif average >= 50:
               classiification = "Pass"
           else:
               classiification = "Fail"


               

               results.append(f"{student_id}, {average:.2f}, {classiification}\n")


    output_filename = filename[:-4] + "_out.csv"

    with open(output_filename, "w") as output:
                output.writelines(results)

except FileNotFoundError:
      print("File not found")










