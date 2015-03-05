'''
ssDict = {'1':'one', '2':'two', '3':'three', '4':'four', '5': 'five',
          '6':'six', '7':'seven', '8':'eight', '9':'nine', '0': 'zero'}
'''



ZERO_TO_NINE = ['zero', 'one', 'two', 'three', 'four', 'five', 'six',
                'seven', 'eight', 'nine']
TEN_TO_NINETEEN = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
                   'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
TWENTY_TO_NINETY = ['twenty', 'thirty', 'forty', 'fifty', 'sixty',
                    'seventy', 'eighty', 'ninety']
dic0to9 = dict(zip([str(i) for i in list(range(10))],ZERO_TO_NINE));
dic10to19 = dict(zip([str(i) for i in list(range(10,20))],TEN_TO_NINETEEN));
dic20to90 = dict(zip([str(i) for i in list(range(2,10))],TWENTY_TO_NINETY));


def digitToStr(digit):
    digitStr = str(digit)
    strlen = len(digitStr)
    spellOutVersion = ""
    if strlen == 1:
        #只有个位时，直接按照0~9字典转出到spellOut
        spellOutVersion = dic0to9[digitStr[-1]] + spellOutVersion
    else:
        #有两位或者三位
        if ('10' <= digitStr[-2:] <= '19'):
            #判断倒数两位是否为10～19
            spellOutVersion = dic10to19[digitStr[-2:]] + spellOutVersion
        else:
            #1.最后一位mapping到ZeroToNine//0 does not map
            if not (digitStr[-1] == '0'):
                spellOutVersion = dic0to9[digitStr[-1]] + spellOutVersion
            #2.倒数第二位不为0时
            if not (digitStr[-2] == '0'):
                #2.1倒数第二位mapping到TwentyToNinety， 2.2 并加到spellOut前面
                tenStr = dic20to90[digitStr[-2]]
                tenStr = tenStr + '-' if not(digitStr[-1] == '0') else tenStr
                spellOutVersion = tenStr + spellOutVersion
        if strlen == 3:
            #有百位
            hundredStr = dic0to9[digitStr[-3]] + '-hundred'
            if spellOutVersion != "":
                #如果十位，个位不为空才有and
                hundredStr += ' and '
            spellOutVersion = hundredStr+ spellOutVersion

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
                #todo: 健壮性检查
                #1.数字的范围
                #2.格式（开头0，小数）
                outputSpelling(digitToStr(digit))
            except ValueError:
                print("Not a digit instance, input 0~1000")
                continue

        
