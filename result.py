from resultprocessing.student import student
from resultprocessing.subject import subject
from resultprocessing.menu import menu
import matplotlib.pyplot as plt
import numpy as np


result={}
while True:
    print("0-exit,1-add,2-search")
    option= int(input("Enter no of your desire work = "))
    if option == 0 :
        break
    if option ==1:
        st=student()
        physics=subject()
        chemistry=subject()
        math=subject()
        result[st.rollno]=[st,physics,chemistry,math]
        print('Added')
        continue
    if option == 2:
        rollno=int(input("Roll No = "))
        data=result.get(rollno)
        if data is None:
            print("not found")
            continue
        print("student ", data[0])
        print("subject 1 ", data[1])
        print("subject 2 ", data[2])
        print("subject 3 ", data[3])
        
        subjects = ["Physics", "Chemistry", "Math"]
        obtainmarks = [data[1].obtainmarks, data[2].obtainmarks, data[3].obtainmarks]

        # plt.bar(subjects, obtainmarks,color='yellow')
        plt.plot(subjects, obtainmarks,color='yellow')
        plt.xlabel("Subjects")
        plt.ylabel("Scores")
        plt.title(f"Student {rollno}'s Subject Scores")
        plt.show()
        continue

