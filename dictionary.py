student_data = {'id1':
                {'name' : 'Valt',
                 'class' : 'v',
                 'subject_integration': ['English, Math, Science']
                },
               'id2':
               {'name' : 'Shu',
                 'class' : 'v',
                 'subject_integration': ['English, Math, Science']
                },
                 'id3':
               {'name' : 'aiger',
                 'class' : 'v',
                 'subject_integration': ['English, Math, Science']
                },
                 'id4':
               {'name' : 'Rantaro',
                 'class' : 'v',
                 'subject_integration': ['English, Math, Science']
                }
}

result = {}
for key,value in student_data.items():
    if value not in result.values():
        result[key] = value
        
print(result)
                
                

               
                
