import statistics as st

import pandas as pd


def promoter(meanScore):
    '''
This function accepts the average score of all 4 subjects for a student and computes promotion status. It returns the promotion status of the student
    '''
    if meanScore >= 60:
        pStatus = 'Promote'
    elif meanScore >= 40:
        pStatus = 'Repeat'
    else:
        pStatus = 'Expel'
    return pStatus


# grade calculator
def gradeCalc(studrec):
    '''
    This function accepts the student record consisting of name and score for all 4 subjects in a list
    for a student and computes average score and calls the promoter function to get promote status
    It returns the average score and promote status of the student
    '''
    name = studrec[0]
    ch = studrec[1]
    ph = studrec[2]
    bi = studrec[3]
    ma = studrec[4]
    avgScore = st.mean([ch,ph,bi,ma])  # (ch + ph + bi + ma)/4
    pStat = promoter(avgScore)
    return [avgScore, pStat]


# function to compute grade for subjects

def grader(studrec):
    '''
    This function accepts the student record consisting of name and score for all 4 subjects in a list
    for a student and computes asubject-wise grade and pass/fail status
    It returns the grade and status of the student
    '''

    name = studrec[0]
    subjScores = studrec[1:]  # studrec[1:5]
    subGrade = []
    for score in subjScores:
        if score > 85:
            grade = 'A'
            status = 'Pass'
        elif score >= 75:
            grade = 'B'
            status = 'Pass'
        elif score >= 60:
            grade = 'C'
            status = 'Pass'
        elif score >= 50:
            grade = 'D'
            status = 'Pass'
        else:
            grade = 'F'
            status = 'Fail'
        subGrade.append([grade, status])
    return subGrade


# Scorecard generator
def scoreCard(studrec, studRes, grades):
    '''
    This function accepts the student record consisting of name and score for all 4 subjects in a list
    for a student  as well as other inputs
    It returns the passlist of the student
    '''
    name = studrec[0]
    subsScore = studrec[1:]
    avgScore = studRes[0]
    pStatus = studRes[1]

    passList = []
    tempList = []
    for sScore, vals in zip(subsScore, grades):
        tempList.extend([sScore, vals[0], vals[1]])
    passList.append(name)
    passList.extend(tempList)
    passList.extend(studRes)
    return passList


# MAIN FUNCTION
def gradeComput2(studList, chemScore, phyScore, bioScore, mathScore):
    '''
    This function accepts the student record consisting of name and score for all 4 subjects in a list
    for a student and computes the students scorecard
    It returns the scorecard of the student
    '''
    resBoard = []
    for name, chem, phy, bio, math in zip(studList, chemScore, phyScore, bioScore, mathScore):
        # print(name, chem, phy,bio,math)
        studrec = [name, chem, phy, bio, math]
        studRes = gradeCalc(studrec)
        grades = grader(studrec)
        # print(name, chem, phy,bio,math)
        # print(grades)
        # print(f'average score of {name} is {studRes}')
        scoreboard = scoreCard(studrec, studRes, grades)
        # print(scoreboard)
        resBoard.append(scoreboard)
    return resBoard


def scorcardGenerator():
    print('Please note that the order of student names MUST be maintained in the score entries!')
    studList = input('provide student names seperated by comma  ')  # ['chidi','chris','niyi','elfreda','toyeen','julius', 'Tamunosaki']
    chem = input('provide scores for Chem seperated by comma  ')  # [45,56,36,78,87,47,89]
    phy = input('provide scores for Phy seperated by comma  ')  # [65,77,87,45,87,66,86]
    bio = input('provide scores for Bio seperated by comma  ')  # [78,75,79,49,67,54,79]
    math = input('provide scores for Math seperated by comma  ')  # [84,70,51,27,53,81,90]

    # '''print(studList)
    # print(chem)
    # print(phy)
    # print(bio)
    # print(math)
    # '''
    # Converting user input into usable lists

    studList = studList.split(',')
    chemParts = chem.split(',')
    phyParts = phy.split(',')
    bioParts = bio.split(',')
    mathParts = math.split(',')

    # '''print(studList)
    # print(chemParts)
    # print(phyParts)
    # print(bioParts)
    # print(mathParts)'''

    chem = [float(x) for x in chemParts]  # list comprehension
    phy = [float(x) for x in phyParts]  # list comprehension
    bio = [float(x) for x in bioParts]  # list comprehension
    math = [float(x) for x in mathParts]  # list comprehension

    # '''print(studList)
    # print(chem)
    # print(phy)
    # print(bio)
    # print(math)'''

    scoreBoard = gradeComput2(studList, chem, phy, bio, math)
    # print(scoreBoard)

    cols = ['Name', 'ChemScore', 'ChemGrade', 'ChemStatus',
            'PhyScore', 'PhyGrade', 'PhyStatus',
            'BioScore', 'BioGrade', 'BioStatus',
            'MathScore', 'MathGrade', 'MathStatus',
            'Avg Score', 'PromotionStatus']
    resdf = pd.DataFrame(scoreBoard, columns = cols)

    return resdf