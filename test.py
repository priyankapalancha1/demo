print "hello"
#a={'abc':'a','bcd':9,'c':1}
#print a['abc']
a=[1,3,5,7,9]
print a[1]
print len(a)
print str(a)
print type(a)
print max(a)
print min(a)
a.append(2)
print a
a.extend({1,2})
print a
a.index(3)
print a
a.insert(1,2)
print a
a.remove(3)
print a
a.reverse()
print a
a.sort()
print a
a.pop(2)
print a
print a[2:4]
a[2]=15
print a[2]
tup1 = ('phy','chem',1997,2000)
tup2 = ('math','bio',3,8)
print cmp(tup1,tup2)
print len(tup1)
print len(tup2)
print max(tup1)
print min(tup2)
dict = {'name':'zara','age': 7}
dict['age']=8;
print "dict['age']:",dict['age']
print len(dict)
print str(dict)
#print dict.copy()
print dict.fromkeys('abcdef')
print dict.has_key('jey')
print dict.items()
print dict.update(dict)
print dict.values()
print dict.setdefault('name','zgara')
print dict.keys()
print dict
print dict.get('name')
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print "Values inside the function: ", mylist
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print "Values outside the function: ", mylist
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist = [1,2,3,4]; # This would assig new reference in mylist
   print "Values inside the function: ", mylist
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print "Values outside the function: ", mylist
def printme( str ):
   "This prints a passed string into this function"
   print str
   return;

# Now you can call printme function
printme()
def printme( str ):
   "This prints a passed string into this function"
   print str
   return;

# Now you can call printme function
printme( str = "My string")
