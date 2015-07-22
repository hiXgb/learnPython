import os  

def function():
	print('aa')
	for x in xrange(1,10):
		print(x)
		if x == 5:
			return



function()


for dirName, subdirList, fileList in os.walk(rootDir):  
    	for fname in fileList: 
     		path = '%s/%s' % (dirName,fname)
     		if subprocess.call("grep \"%s\" %s" %(keyWord,path), shell=True) == 0:
          		print('%s is used!!! path is %s' % (keyWord,path))
          		return


