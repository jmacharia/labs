student = {
    'name': 'Joel Macharia',
    'langs': ['Python', 'Ruby', 'Bash'],
    'age': 20
}

student_list = []

def add_student(student):
    '''
    adds a student to the list
    '''
    student_list.append(student)

def oldest_student(student_list):
    '''
    returns the oldest student in the list
    args -> list of student
    '''
    oldest = student_list[0]["age"]
    if (len(student_list) == 1):
        return student_list[0]
    else:
        for i in range(1, len(student_list)):
            if (oldest < student_list[i]["age"]):
                oldest = student_list[i]["age"]
        return student_list[i]
        

def student_lang(lang):
    '''
    returns a list containing names of students who know a particular language.
    args ->  lang
    '''
    known_lang = []
    for i in range(len(student_list)):
        for j in range(len(student_list[i]["langs"])):
            if (lang == student_list[i]["langs"][j]):
                known_lang.append(student_list[i]["name"])
    return known_lang

