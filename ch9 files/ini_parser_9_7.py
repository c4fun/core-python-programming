___author__ = 'Richard'
import  re

big_dict = {}

def inputFilename():
    filename = ''
    try:
        while filename == '':
            filename = input('Open an ini file: ')
        return filename
    except IOError:
        print('Wrong file name. input again')

def ini_parser(f):
    """if the line is like ['big_dict_key'], then new a sub dict"""
    for eachLine in f:
        # print(eachLine)
        if re.match(r'.*\[.*\]',eachLine):
            # big_dict_key = eachLine.strip()[1:-1]
            # big_dict_key = eachLine[mtc.start()+1:mtc.end()-1]
            big_dict_key = eachLine[eachLine.find('[')+1:eachLine.find(']')]

            print(big_dict_key)
            big_dict[big_dict_key] = {}
            continue
        if re.match(r'.*\=.*', eachLine):
            stripped_line = eachLine.strip()
            pos_of_equal = stripped_line.find('=')
            # print(pos_of_equal)
            value = str(stripped_line[:pos_of_equal])
            key = str(stripped_line[pos_of_equal+1:])
            big_dict[big_dict_key][value] = key


def iteratorMethod():
    'suitable for big files'
    # filename = inputFilename()
    filename = 'shuangping_Sogou.ini'
    fobj = open(filename, 'r', encoding='utf-8')
    ini_parser(fobj)
    fobj.close()

if __name__ == '__main__':
    iteratorMethod()
    print(big_dict)