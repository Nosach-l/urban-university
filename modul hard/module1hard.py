grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
gpa_0 = sum(grades[0]) / len(grades[0])
gpa_1 = sum(grades[1]) / len(grades[1])
gpa_2 = sum(grades[2]) / len(grades[2])
gpa_3 = sum(grades[3]) / len(grades[3])
gpa_4 = sum(grades[4]) / len(grades[4])
list_ = list(students)
list_.sort()
gpa_registry = {list_[0]: gpa_0, list_[1]: gpa_1, list_[2]: gpa_2, list_[3]: gpa_3, list_[4]: gpa_4}
print(gpa_registry)
