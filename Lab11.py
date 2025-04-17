import matplotlib.pyplot as plt
import numpy as np
import os

def print_menu():
    print('1. Student grade')
    print('2. Assignment statistics')
    print('3. Assignment graph\n')
    return input('Enter your selection: ')

def main():
    students = []
    studentIDs = []
    with open('data/students.txt', 'r') as file:
        for line in file:
            ID = line[0:3]
            name = line[3:]
            name = name.replace('\n', '')
            students.append(name)
            studentIDs.append(ID)

    assignmentWeight = []
    assignmentIDs = []
    assignmentNames = []
    with open('data/assignments.txt', 'r') as file:
        content = file.read().split('\n')
        content.pop(len(content) - 1)
        for i in range(0, len(content), 3):
            name = content[i]
            ID = content[i+1]
            weight = int(content[i+2])
            assignmentNames.append(name)
            assignmentIDs.append(ID)
            assignmentWeight.append(weight)

    submissionStudent = []
    submissionAssignment = []
    submissionScore = []
    for filename in os.listdir('data/submissions'):
        with open(f'data/submissions/{filename}', 'r') as file:
            content = file.read().split('|')
            submissionStudent.append(content[0])
            submissionAssignment.append(content[1])
            submissionScore.append(content[2])

    option = print_menu()

    if option == '1':
        studentName = input("What is the student's name: ")
        if studentName not in students:
            print('Student not found')
        else:
            studentID = studentIDs[students.index(studentName)]
            maxScore = 0
            studentScore = 0
            for i in range(0, len(submissionStudent)):
                if studentID == submissionStudent[i]:
                    score = submissionScore[i]
                    assignmentIndex = assignmentIDs.index(submissionAssignment[i])
                    weight = assignmentWeight[assignmentIndex]
                    maxScore += weight
                    studentScore += int(score) * int(weight)
            print(round(studentScore / maxScore))
    elif option == '2':
        assignmentName = input('What is the assignment name: ')
        if assignmentName not in assignmentNames:
            print('Assignment not found')
        else:
            assignmentID = assignmentIDs[assignmentNames.index(assignmentName)]
            assignmentScores = []
            for i in range(0, len(submissionAssignment)):
                if assignmentID == submissionAssignment[i]:
                    assignmentScores.append(int(submissionScore[i]))
            print('Mini:', min(assignmentScores))
            print('Avg', sum(assignmentScores) // len(assignmentScores))
            print('Max:', max(assignmentScores))
    elif option == '3':
        assignmentName = input('What is the assignment name: ')
        if assignmentName not in assignmentNames:
            print('Assignment not found')
        else:
            assignmentID = assignmentIDs[assignmentNames.index(assignmentName)]
            assignmentScores = []
            for i in range(0, len(submissionAssignment)):
                if assignmentID == submissionAssignment[i]:
                    assignmentScores.append(int(submissionScore[i]))
            fig, ax = plt.subplots()
            plt.hist(assignmentScores, bins=[50, 55, 60, 65, 70, 75, 80,85, 90, 95, 100])
            ax.set(xlim=(49, 101), xticks=np.arange(50, 101, 10),
                   ylim=(0, 10), yticks=np.arange(0, 9, 2))
            plt.show()

if __name__ == '__main__':
    main()