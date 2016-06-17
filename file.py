
#fo = open("foo.txt", "wb")
#print "Name of the file: ", fo.name

# Close opend file
#fo.close()

fo = open("foo.txt", "wb")
fo.write( "Python is a great language.\nYeah its great!!\n");

# Close opend file
fo.close()

fo = open("foo.txt", "r+")
str = fo.read(10);
print "Read String is : ", str
# Close opend file
fo.close()


# Open a file
fo = open("foo.txt", "r+")
str = fo.read(10);
print "Read String is : ", str

# Check current position
position = fo.tell();
print "Current file position : ", position

# Reposition pointer at the beginning once again
position = fo.seek(5, 0);
str = fo.read(10);
print "Again read String is : ", str
# Close opend file
fo.close()