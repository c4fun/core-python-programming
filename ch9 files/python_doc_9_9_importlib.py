__author__ = 'Richard'
import os
# 找到import的错误了，我忘记了scope的概念，搞得刚才的str_to_class的scope是用的全局中的scope，
# 而 return getattr(sys.modules[__name__], str) 在局部函数 parseFile中没有定义
# 所以返回的是全局中的import，局部再import什么模块都没有用

import importlib

AttributeName = '__doc__'
honor_list = {}
shame_list = {}

def parseFile(lib_directory):
    dir_file = os.listdir(lib_directory)
    print(dir_file)
    # loop to judge if the dir_file[i] is a .py file
    for i in range(len(dir_file)):

        filename, ext = os.path.splitext(dir_file[i])
        if ext == '.py':
            try:
                imported_module = importlib.import_module(filename)
                # if it has __doc__, then honor_list[module_name] = __doc__
                if imported_module.__doc__:
                    honor_list[dir_file[i]] = imported_module.__doc__

                # if it has not, then shame_list[module_name] = None
                else:
                    shame_list[dir_file[i]] = imported_module.__doc__
            except ImportError:
                print('{} has occured an import error'.format(dir_file[i]))
            except AttributeError:
                pass
                # print('{} has occured an attribute error'.format(filename))



def init():
    # TODO set the init dir as D:\Python34\Lib
    directory = 'D:\Python34\Lib'
    return directory
    pass

def output():
    print(honor_list)
    print(shame_list)
    print('There are %d items in the honor_list.'%(len(honor_list)))
    print('There are %d items in the shame_list.'%(len(shame_list)))

    fobj = open('lib docstring result.txt','w')
    fobj.write('There are {} items in the honor_list.{}'.format(len(honor_list),os.linesep))
    i = 1
    for key, value in honor_list.items():
        fobj.write('{:>3} {:^20} {} {}'.format(i, key, value, os.linesep))
        i += 1

    fobj.write('There are {} items in the shame_list.{}'.format(len(shame_list),os.linesep))
    i = 1
    for key, value in shame_list.items():
        fobj.write('{:>3} {:^20} {} {}'.format(i, key, value, os.linesep))
        i += 1
    fobj.close()


def main():
    lib_directory = init()
    os.chdir(lib_directory)
    print('{0}{1}{2:*<50}'.
          format('(O-O) ', 'Current directory is: ',os.getcwd()))
    parseFile(lib_directory)

if __name__ == '__main__':
    main()
    output()
