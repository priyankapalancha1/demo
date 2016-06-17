#def printinfo( name, age ):
  # "This prints a passed info into this function"
  # print "Name: ", name
  # print "Age ", age
  # return;

# Now you can call printinfo function
#printinfo( age=50, name="miki" )
def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print "Name: ", name
   print "Age ", age
   return;
# Now you can call printinfo function
printinfo( age=50, name="miki" )
printinfo( name="miki" )


sum = lambda arg1, arg2: arg1 + arg2;
# Now you can call sum as a function
print "Value of total : ", sum( 10, 20 )
print "Value of total : ", sum( 20, 20 )


def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2
   print "Inside the function : ", total
   return total;


total=0;
# Now you can call sum function
total = sum( 10, 20 );
print "Outside the function : ", total 
def sum( arg1, arg2 ):
   total = arg1 + arg2; # Here total is local variable.
   print "Inside the function local total : ", total
   return total;

sum( 10, 20 );
print "Outside the function global total : ", total 


print "Python is really a great language,", "isn't it?"
str = raw_input("Enter your input: ");
print "Received input is : ", str

#str = input("Enter your input: ");
#print "Received input is : ", str

fo = open("foo.txt", "wb")
print "Name of the file: ", fo.name
print "Closed or not : ", fo.closed
print "Opening mode : ", fo.mode
print "Softspace flag : ", fo.softspace

