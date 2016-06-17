#i changed the commands
read = open('file.txt','r+')
lines = read.readlines()
dict1 ={}
for line in lines:
	sline = line.split(':')
	dict1[sline[0]]=sline[1]

x=raw_input("Please Enter your word : ")
if x in dict1.keys():
      print dict1[x]
else:
	  print "word not found"