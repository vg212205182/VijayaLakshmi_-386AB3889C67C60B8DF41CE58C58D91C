class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  #Sort the list of students in descending order of cgpa
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  return sorted_students


#Example usage:
student = [
    Student("Shri", "A123", 7.8),
    Student("Dharsh", "A124", 9.9),
    Student("Rakshan", "A125", 9.3),
    Student("Mewahh", "A126", 8.9),
]

sorted_students = sort_students(student)

# Print the sorted list of students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
                                                     student.roll_number,
                                                     student.cgpa))