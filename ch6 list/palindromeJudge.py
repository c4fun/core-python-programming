def palindromeJudge(strToJudge):
    strlen = len(strToJudge)
    for i in range(strlen // 2):
        if strToJudge[i] != strToJudge[-(i+1)]:
            return False
    return True


if __name__ =='__main__':
    strToJudge=str(input("Input a string\n"))
    flag = palindromeJudge(strToJudge)
    if flag:
        print("%s is a palindrome"%strToJudge)
    else:
        print("%s is not a palindrome"%strToJudge)
 
