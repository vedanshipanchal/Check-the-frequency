student_data = {

'stu1': {'name':'Tasheen', 'grade':5, 'id':1,  'subject':["Eng","python"]},
'stu2': {'name':'Vedanshi', 'grade':5, 'id':2,  'subject':["Eng","python"]},
'stu3': {'name':'Chiamalite', 'grade':5, 'id':3,  'subject':["Eng","python"]},
'stu4': {'name':'Vedanshi', 'grade':5, 'id':2,  'subject':["Eng","python"]},

}

result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value
print(result)