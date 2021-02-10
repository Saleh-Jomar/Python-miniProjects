#Saleh Jomar DU. Salugandang
#201500709
#HBC-TQR
facultynoname={}
studentnoname={}
liststudents=[]
studentname=[]
facultyname=[]
subjectcodes=[]
listcourse=[]
subjectlists=[]
facultylists=[]
listdept=[]
studsubdict={}
facsubdict={}
gradeddict={}
UPgradedict={1.00:[92, 93, 94, 95, 96, 97, 98, 99, 100],1.25:[88, 89, 90, 91],1.50:[84, 85, 86, 87],1.75:[80,81,82,83],2.00:[76,77,78,79],2.25:[72,73,74,75],2.50:[68,69,70,71],2.75:[64,65,66,67],3.00:[60,61,62,63],4.00:[56,57,58,59],5.00:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]}
def studentadd():
    lastname=raw_input("Enter last name: ")
    firstname=raw_input("Enter first name: ")
    middlename=raw_input("Enter middle name: ")
    suffix=raw_input("Enter suffix(space if none): ")
    while True:
        number=raw_input("Enter student number: ")
        if number in liststudents:
            print "That is already taken"
        else:
            break
    studentcourse=raw_input("Enter course: ") 
    studentsex=raw_input("Enter sex: ")
    studentbday=raw_input("Enter birth date: ")
    student=open("student.txt","ab")
    studentinfo=lastname+','+' '+firstname+' '+middlename+' '+suffix+'\n'+number+'\n'+studentcourse+'\n'+studentbday+'\n'+studentsex+'\n'+'\n'
    student.write(studentinfo)
    student.close()
    liststudents.append(number)
    listcourse.append(studentcourse)
    studentname.append(lastname + ' ' + firstname + ' ' + middlename+ ' '+ suffix)
    studentnoname[number]=lastname + ' ' + firstname + ' ' + middlename+ ' '+ suffix
def studentedit():
    while True:
        editname=raw_input("Enter student no.: ")
        if editname not in liststudents:
            print "That student does not exist"
        else:
            break
    student=open("student.txt")
    student.seek(0)
    studentinfos=student.readlines()
    student.close()
    a=raw_input("Enter student course: ")
    b=raw_input("Enter student birthdate: ")
    c=raw_input("Enter student sex: ")
    studentinfos[studentinfos.index(editname+'\n')+1]=a+'\n'
    studentinfos[studentinfos.index(editname+'\n')+2]=b+'\n'
    studentinfos[studentinfos.index(editname+'\n')+3]=c+'\n'
    student=open("student.txt","w")
    student.writelines(studentinfos)
    student.close()
def facultyadd():
    lastname=raw_input("Enter last name: ")
    firstname=raw_input("Enter first name: ")
    middlename=raw_input("Enter middle name: ")
    suffix=raw_input("Enter suffix(space if none): ")
    while True:
        number=raw_input("Enter faculty number: ")
        if number in facultylists:
            print "That is already taken"
        else:
            break
    college=raw_input("Enter college: ")
    department=raw_input("Enter department: ")
    facultysex=raw_input("Enter sex: ")
    facultybday=raw_input("Enter birth date: ")
    faculty=open("faculty.txt","ab")
    facultyinfo=lastname+','+' '+firstname+' '+middlename+' '+suffix+'\n'+number+'\n'+college+'\n'+department+'\n'+facultybday+'\n'+facultysex+'\n'+'\n'
    faculty.write(facultyinfo)
    faculty.close()
    facultylists.append(number)
    listdept.append(department)
    facultyname.append(lastname + ' ' + firstname + ' ' + middlename+ ' '+ suffix)
    facultynoname[number]=lastname + ' ' + firstname + ' ' + middlename+ ' '+ suffix
def facultyedit():
    while True:
        editname=raw_input("Enter faculty no.: ")
        if editname not in facultylists:
            print "That faculty does not exists"
        else:
            break
    faculty=open("faculty.txt")
    faculty.seek(0)
    facultyinfos=faculty.readlines()
    faculty.close()
    a=raw_input("Enter college: ")
    b=raw_input("Enter department: ") 
    c=raw_input("Enter faculty birthdate: ")
    d=raw_input("Enter faculty sex: ")
    facultyinfos[facultyinfos.index(editname+'\n')+1]=a+'\n'
    facultyinfos[facultyinfos.index(editname+'\n')+2]=b+'\n'
    facultyinfos[facultyinfos.index(editname+'\n')+3]=c+'\n'
    facultyinfos[facultyinfos.index(editname+'\n')+4]=d+'\n'
    faculty=open("faculty.txt","w")
    faculty.writelines(facultyinfos)
    faculty.close()
def subjectadd():
    while True:
        subjectno=raw_input("Enter subject number: ")
        if subjectno in subjectlists:
            print "That is already taken"
        else:
            break
    subjectcode=raw_input("Enter subject code: ")
    subjecttitle=raw_input("Enter subject title: ")
    effectivityyear=raw_input("Enter effectivity year: ")
    status=raw_input("Enter status: ")
    subject=open("subject.txt","ab")
    subjectinfo=subjectno+'\n'+subjectcode+'\n'+subjecttitle+'\n'+effectivityyear+'\n'+status+'\n'+'\n'
    subject.write(subjectinfo)
    subject.close()
    subjectlists.append(subjectno)
    subjectcodes.append(subjectcode)
def subjectedit():
    while True:
        editsubject=raw_input("Enter subject number: ")
        if editsubject not in subjectlists:
            print "The subject does not exist"
        else:
            break
    subject=open("subject.txt")
    subject.seek(0)
    subjectinfos=subject.readlines()
    subject.close()
    a=raw_input("Enter subject number: ")
    b=raw_input("Enter subject code: ")
    c=raw_input("Enter subject title: ")
    d=raw_input("Enter effectivity year: ")
    e=raw_input("Enter status: ")
    subjectinfos[subjectinfos.index(editsubject+'\n')]=a+'\n'
    subjectinfos[subjectinfos.index(editsubject+'\n')+1]=b+'\n'   
    subjectinfos[subjectinfos.index(editsubject+'\n')+2]=c+'\n'
    subjectinfos[subjectinfos.index(editsubject+'\n')+3]=d+'\n'
    subjectinfos[subjectinfos.index(editsubject+'\n')+4]=e+'\n'
    subject=open("subject.txt","w")
    subject.writelines(subjectinfos)
    subject.close()
def subjectstudentenlist():
    stop=1
    while True:
        a=raw_input("Enter subject number: ")
        if a not in subjectlists:
            print "That is not in the list of subjects"
        else:
            break
    if studsubdict.has_key(a)== True:
        while stop!=0:
            b=raw_input("Enter student number: ")
            if b+'\n' in studsubdict[a]:
                print "The student is already enlisted"
            elif b not in liststudents:
                print "The student does not exist"
            else:
                studsubdict[a].append(b+'\n')
                subject_student=open("subject_student.txt")
                subject_student.seek(0)
                subject_studentinfos=subject_student.readlines()
                subject_student.close()
                subject_studentinfos.insert(subject_studentinfos.index(a+'\n')+1,b+'\n')
                subject_student=open("subject_student.txt","w")
                subject_student.writelines(subject_studentinfos)
                subject_student.close()
            stop=input("Would you like to still enlist ?(1 or 0): ")
    else:
        c=[]
        while stop!=0:
            b=raw_input("Enter student number: ")
            if b+'\n' in c:
                print "That student is already enlisted"
            elif b not in liststudents:
                print "That student does not exist"
            else:
                c.append(b+'\n')
            stop=input("Would you like to still enlist?(1 or 0): ")
        studsubdict[a]=c
        subject_student=open("subject_student.txt","ab")
        subject_student.write(a+'\n')
        subject_student.writelines(c)
        subject_student.close
def subjectstudentremove():
    while True:
        a=raw_input("Enter subject number: ")
        if a not in subjectlists:
            print "That is not in the list of subjects"
        elif studsubdict.has_key(a) == False:
            print "There is no one enlisted in that class"
        else:
            break
    while True:
        b=raw_input("Enter student number: ")
        if b+'\n' not in studsubdict[a]:
            print "The student is not enlisted in this class"
        elif b+'\n' in gradeddict[a]:
            print "The student is already graded"
        else:
            studsubdict[a].remove(b+'\n')
            break
    subject_student=open("subject_student.txt")
    subject_student.seek(0)
    subject_studentinfos=subject_student.readlines()
    subject_student.close()
    subject_studentinfos.remove(b+'\n')
    subject_student=open("subject_student.txt","w")
    subject_student.writelines(subject_studentinfos)
    subject_student.close()
def subjectfacultyassign():
    while True:
        a=raw_input("Enter faculty number: ")
        if a not in facultylists:
            print "The entered faculty number is not in the list"
        else:
            break
    if facsubdict.has_key(a)== True:
        while stop!=0:
            b=raw_input("Enter subject number: ")
            if b+'\n' in facsubdict[a]:
                print "The course is already being handled by the faculty"
            elif b not in facultylists:
                print "The faculty does not exist"
            else:
                facsubdict[a].append(b+'\n')
                subject_faculty=open("subject_faculty.txt")
                subject_faculty.seek(0)
                subject_facultyinfos=subject_faculty.readlines()
                subject_faculty.close()
                subject_facultyinfos.insert(subject_facultyinfos.index(a+'\n')+1,b+'\n')
                subject_faculty=open("subject_faculty.txt","w")
                subject_faculty.writelines(subject_facultyinfos)
                subject_faculty.close()
            stop=input("Would you like to still assign ?(1 or 0): ")
    else:
        c=[]
        stop=1
        while stop!=0:
            b=raw_input("Enter subject number: ")
            if b+'\n' in c:
                print "That course is already being handled by the faculty"
            if b not in facultylists:
                print "That faculty does not exist"
            else:
                c.append(b+'\n')
            stop=input("Would you like to still assign?(1 or 0): ")
        facsubdict[a]=c
        subject_faculty=open("subject_faculty.txt","ab")
        subject_faculty.write(a+'\n')
        subject_faculty.writelines(c)
        subject_faculty.close
def subjectfacultyremove():
    while True:
        a=raw_input("Enter faculty number: ")
        if a not in facultylists:
            print "The entered faculty number is not in the list"
        elif facsubdict.has_key(a) == False:
            print "There are no subjects being handled by the faculty"
        else:
            break
    while True:
        b=raw_input("Enter subject number: ")
        if b+'\n' not in facsubdict[a]:
            print "The subject is not being handled by the faculty"
        else:
            studsubdict[a].remove(b+'\n')
            break
    subject_faculty=open("subject_faculty.txt")
    subject_faculty.seek(0)
    subject_facultyinfos=subject_faculty.readlines()
    subject_faculty.close()
    subject_facultyinfos.remove(b+'\n')
    subject_faculty=open("subject_faculty.txt","w")
    subject_faculty.writelines(subject_facultyinfos)
    subject_faculty.close()
def assigngrade():
    c=[]
    z=0
    while True:
        a=raw_input("Enter subject number: ")
        if a not in subjectlists:
            print "That is not in the list of subjects"
        elif studsubdict.has_key(a) == False:
            print "There is no one enlisted in that class" 
        else:
            break
    for i in range(len(studsubdict[a])):
        if studsubdict[a][z]  not in gradedict[a]:
            b=input("Enter grade for" + " " + studsubdict[a][z] )
            for keys in UPgradedict:
                if b in UPgradedict[keys]:
                    d=keys
            c.append(studsubdict[a][z])
            subject_student=open("subject_student.txt")
            subject_student.seek(0)
            subject_studentinfos=subject_student.readlines()
            subject_student.close()
            subject_studentinfos[subject_studentinfos.index(studsubdict[a][z])]=str(d)+ " " + studsubdict[a][z]
            subject_student=open("subject_student.txt","w")
            subject_student.writelines(subject_studentinfos)
            subject_student.close()
            gradeddict[a]=c
        else:
            z=z+1
        
def totalnumberstudent(a):
    print  str(len(a))
def studentcountpercourse(b):
    from collections import Counter
    a=Counter(b)
    for keys in a:
        print keys + ":" + str(a[keys])
def maletofemale():
    student=open("student.txt")
    student.seek(0)
    studentinfos=student.read()
    student.close()
    a=studentinfos.count('Male')+studentinfos.count('Male'.lower())+studentinfos.count('Male'.upper())
    b=studentinfos.cound('Female')+studentinfos.cound('Female'.lower())+studentinfos.cound('Female'.upper())
    print "The number of male students are: " + str(a)
    print "The numbe of female students are: " + str(b)
def subjecttostudentfaculty(a):
    for keys in a:
        print keys+ ":" + str(len(a[keys]))
def reportgeneration():
    print "The number of students under courses: "
    studentcountpercourse(listcourse)
    print "The total number of studends: "
    totalnumberstudent(liststudents)
    print "Total number of faculty per department: "
    studentcountpercourse(listdept)
    print "The total number of faculty: "
    totalnumberstudent(facultylists)
    maletofemale()
    print "No. of students enlisted in a subject: "
    subjecttostudentfaculty(studsubdict)
    print "No. of courses handled by a faculty member: "
    subjecttostudentfaculty(facsubdict)
def listcheck(a):
    print a
def subjectinfo():
    a=input("Enter subject number: ")
    subject=open("subject.txt")
    subject.seek(0)
    subjectinfos=subject.readlines()
    subject.close()
    for i in range(5):
        print subjectinfos[subjectinfos.index(a)+i]-'\n'
def studentsinsubject():
    a=raw_input("Enter subject number: ")
    print "The students under this subject are: "
    for i in range(len(studsubdict[a])):
        print studentnoname[studsubdict[a][i]]
def subjectinstudent():
    a=raw_input("Enter the faculty number: ")
    print "The subject handled by this faculty member are: "
    for i in range(len(facsubdict[a])):
        print facsubdict[a][i]
def mainfunction():
    go=1
    while go!=0:
        c='1'
        a=raw_input("Choose from functionalities: Student Demographics, Faculty Demographics, Subject Info, Enlistment, Faculty Subject, Grading, Report Generation, Other Functionalities: ")
        if a=="Student Demographics" or a=="Student Demographics".lower() :
            while c=='1':
                b=raw_input("Choose from edit and add: ")
                if b == 'add':
                    studentadd()
                    c=raw_input("Wish to use this function again? (Enter 1 if yes and 0 if no): ")  
                elif len(liststudents)==0:
                    print "No students currently in list"
                else:
                    studentedit()
                    c=raw_input("Wish to use this function again? (Enter 1 if yes and 0 if no): ")
                    
        elif a== 'Faculty Demographics' or a== "Faculty Demographics".lower():
            while c=='1':
                b=raw_input("Choose from edit and add: ")
                if b== 'add' :
                    facultyadd()
                    c=raw_input("Wish to use this function again? (Enter 1 if yes and 0 if no): ")
                elif len(facultylists)==0:
                    print "No faculty currently in list"
                else:
                    facultyedit()
                    c=raw_input("Wish to use this function again? (Enter 1 if yes and 0 if no): ")
                
        elif a== 'Subject Info' or a== 'Subject Info'.lower() :
            while c=='1':
                b=raw_input("Choose from edit and add: ")
                if b== 'add' :
                    subjectadd()
                    c=raw_input("Wish to use this function again? (Enter 1 if yes and 0 if no): ")
                elif len(subjectlists)==0:
                    print "No subject currently in list"
                else:
                    subjectedit()
                    c=raw_input("Wish to use this function again? (Enter 1 if yes and 0 if no): ")           
        elif a== 'Enlistment' or a== 'Enlistment'.lower():
            b=raw_input("Choose from enlisting or removing a student: ")
            if len(subjectlists)==0:
                print "No subjects available"
            elif b== 'enlisting':
                subjectstudentenlist()
            elif len(studsubdict)==0:
                print "No students currently enrolled"
            else:
                subjectstudentremove()
        elif a== 'Faculty Subject' or a=='Faculty Subject'.lower():
            b=raw_input("Choose from assigning or removing: ")
            if len(facultylists)==0:
                "No faculty currently in list"
            elif b== 'assigning':
                subjectfacultyenlist()
            elif len(facsubdict)==0:
                "No faculty currenlty assignend"
            else:
                subjectfacultyremove()
        elif a== 'Grading'or a== 'Grading'.lower():
            if len(studsubdict)==0:
                print "Not yet available for grading"
            else:
                assigngrade()
        elif a== 'Report Generation' or a== 'Report Generation'.lower():
            reportgeneration()
        elif a== 'Other Functionalities'or a== 'Other Functionalities'.lower():
            while c==1:
                b=input("Enter 1 : View list of students , 2 : View list of faculty members , 3: View list of subjects , 4 : View subject info, 5 :View list of all students enlisted in a subject, 6:View list of subject - assigned faculty pair ") 
                if b==1:
                    listcheck(studentname)
                elif b==2:
                    listcheck(facultyname)
                elif b==3:
                    listcheck(subjectcodes)
                elif b==4:
                    subjectinfo()
                elif b==5:
                    studentsinsubject()
                elif b==6:
                    subjectinstudent()
                c=raw_input("Wish to use this function again? (Enter 1 if yes and 0 if no): ")
       
        go=input("Would you like to continue? Enter 1 if yes and 0 if no: ")
mainfunction()
