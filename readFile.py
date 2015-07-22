import os
import subprocess

rootDir = '/Users/xieguobi/Documents/CoCo/BaBa-iOS_bug_fix/CoCo'
resourceDir = '/Users/xieguobi/Documents/CoCo/BaBa-iOS_bug_fix/Resources/en.lproj/Localizable.strings'

#find folders
def goalFile(path):
    files = []
    for dirName, subdirList, fileList in os.walk(path):  
                                    for fname in fileList: 
                                            if fname.endswith('.m'):
                                               path = '%s/%s' % (dirName,fname)
                                               files.append(path)
                                            if fname.endswith('.h'):
                                               path = '%s/%s' % (dirName,fname)
                                               files.append(path)
                                            if fname.endswith('.mm'):
                                               path = '%s/%s' % (dirName,fname)
                                               files.append(path)
    return files                                           

#find keyWords
def keyWords(path):
    keyArray = []
    f = open(path,'r')
    s = f.read()
    if '{' in s:
        s = s.replace('{',"")
    if '}' in s:
        s = s.replace('}',"")
    splitStr = s.split(';')
    for x in range(len(splitStr)):
        subStr = splitStr[x].split('=')
        keyWord = subStr[0]
        keyWord = keyWord.replace('\n\t',"")
        keyWord = keyWord.replace(" ","")
        keyArray.append(keyWord)
    f.close()
    return keyArray

#print(keyWords(resourceDir))

#search keyWord in path
def search(keys,paths):
    print("below are not used keys:\t")
    for key_word in keys:
                isMatched = 0
                for path in paths:
                    #print("grep %s %s" %(key,path))
                    if subprocess.call("grep -w -q '%s' %s" %(key_word,path), shell=True) == 0:
                        isMatched = 1
                        #print('%s is used in %s' % (key_word,path))
                        break
                if isMatched == 0:
                    print(key_word)
    print('search finished!!')

search(keyWords(resourceDir),goalFile(rootDir))