def convertIntToIPAddress(ipInt):
    ipAddr = ['000','000','000','000']
    ipsection = -1
    while (ipInt > 0) and (ipsection >= -4):
        ipAddr[ipsection] = str(ipInt % 256)
        ipInt = ipInt >> 8
        ipsection -= 1
    return ipAddr

if __name__ =='__main__':
    try:
        ipInt = int(input('Please input an integer'))
    except ValueError:
        print("Wrong Input!")
    print(convertIntToIPAddress(ipInt))
