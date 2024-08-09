import random
num = [1,2,3]
new_list = [n+1 for n in num]

name = "Test123"
new_list = [letter for letter in name]

range_list = [numx*2 for numx in range(1,5)]
# print(range_list)

names =['aaa' , 'bbb' , 'ccc' , 'ddd' , 'eee' , 'fff' , 'gggsdf sdfgg']
short_names = [(names).title() +' x' for names in names if len(names) > 6]
# print(short_names)
students = [
    'beth', 'john', 'mike', 'anna', 'jane', 'mark', 'lucy', 'paul', 'kate', 
    'jack', 'lisa', 'tom', 'emma', 'adam', 'eva'
]

# Membuat dictionary dengan nilai acak untuk setiap siswa
passed_students = {student: random.randint(25, 100) for student in students}


pass_students = {student:score for (student,score) in passed_students.items() if score > 70}

student_dict = {
    'student' : ['angela' , 'james' , 'lily'],
    'score' : [56,77,90]
}

import pandas as pd

student_data_frame = pd.DataFrame(student_dict)

for (key,val) in student_data_frame.iterrows():
    print(key)