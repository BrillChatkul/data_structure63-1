def odd_even(Qtput):
    QuestionList = Qtput.split(',')
    if(QuestionList[0] == 'L'):
        inputStringList = QuestionList[1].split()
        outputList = []
        for s in range(len(inputStringList)):
            if(QuestionList[2] == 'Odd' and s%2==0):
                outputList.append(inputStringList[s])
            elif(QuestionList[2] == 'Even' and s%2 == 1):
                outputList.append(inputStringList[s])
        return outputList
    elif QuestionList[0] == 'S':
        inputString = QuestionList[1]
        outputList = ''
        for s in range(len(inputString)):
            if(QuestionList[2] == 'Odd' and s%2==0):
                outputList += inputString[s]
            elif(QuestionList[2] == 'Even' and s%2 == 1):
                outputList += inputString[s]
        return str(outputList)
    
        



print('*** Odd Even ***')
Qinput = input('Enter Input : ')
print(odd_even(Qinput))

