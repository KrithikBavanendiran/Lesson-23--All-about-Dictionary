student_data={'id1':
    {'name':['Sara'],
     'grade':['V'],
     'subject_integration':['english','maths','science']},
    'id2':
        {'name':['David'],
     'grade':['V'],
     'subject_integration':['english','maths','science']},
    'id3':
        {'name':['Sara'],
     'grade':['V'],
     'subject_integration':['english','maths','science']},
     'id4':
         {'name':['Surya'],
     'grade':['V'],
     'subject_integration':['english','maths','science']}
     }
result={}
for key, value in student_data.items():
    if value not in result.values():
        result[key]=value
print(result)