#python中这两个dict应该有更好的方式生成的
dsDict = {1:'one', 2:'two', 3:'three', 4:'four', 5: 'five',
          6:'six', 7:'seven', 8:'eight', 9:'nine', 0: 'zero'}

ssDict = {'1':'one', '2':'two', '3':'three', '4':'four', '5': 'five',
          '6':'six', '7':'seven', '8':'eight', '9':'nine', '0': 'zero'}

def digitToStr(digit):
    digitStr = str(digit)
    strlen = len(digitStr)
    spellOutVersion = ""
    for i in range(strlen):
        if i != 0:
            spellOutVersion += '-'
        spellOutVersion += ssDict[digitStr[i]]
    return spellOutVersion

def outputSpelling(s):
    print(s)

if __name__ == '__main__':
    while True:
        sInput = input("Please input a figure in the digital form, such as 69\n")
        if sInput == '':
            print("The program ends here")
            break;
        else:
            try:
                digit = int(sInput)
                outputSpelling(digitToStr(digit))
            except ValueError:
                print("Not a digit instance, input 0~1000")
                continue

        
