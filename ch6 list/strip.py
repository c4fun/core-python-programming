def strip(s):
    if not isinstance(s, str):
        return "Not a String instance!"
    strlen = len(s)
    leadingFlag = True
    trailingFlag = True
    i = 0
    j = 0
    startLetterPos = 0
    endLetterPos = 0
    while i < strlen:
        if s[i] != ' ':
            leadingFlag = False
            startLetterPos = i
            break
        i +=1
        
    while j < strlen:
        if s[-(j+1)] != ' ':
            trailingFlag = False
            endLetterPos = j
            break;
        j +=1

    if (startLetterPos == strlen): return ''
    elif (startLetterPos == 0 and endLetterPos == 0): return s
    elif (startLetterPos > 0 and endLetterPos == 0):
        return s[startLetterPos:]
    elif (startLetterPos == 0 and endLetterPos > 0):
        return s[:-endLetterPos]
    elif (startLetterPos > 0 and endLetterPos > 0):
        return s[startLetterPos:-endLetterPos]
    else:
        return('what the fuck')

if __name__ =='__main__':
    strToJudge=str(input("Input a string\n"))
    s = strip(strToJudge)
    print(s)
    print(len(s))
