import json

def getNumberfromJsonFile():
    file = open("ListNumber.json", "r") 
    data = json.load(file)
    StrSequence = data["sequence"]
    TempSequence = StrSequence.split(",")
    TempSequence = [x.strip(' ') for x in TempSequence]
    return TempSequence

if __name__ == '__main__':
    EvenNumber = []
    NumberListSequence = getNumberfromJsonFile()
    for i in range(len(NumberListSequence)):
        ##print(NumberSequence[i])
        if(int(NumberListSequence[i]) % 2 == 0):
            ##print (NumberListSequence[i])
            EvenNumber.append(NumberListSequence[i])
    ##print(EvenNumber)
    str1 = ', '.join(EvenNumber)
    print ("The even numbers are "+str1)
    
