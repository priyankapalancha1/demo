name= raw_input("Please enter Customer Name : ")
meter_no=raw_input("Please Enter Meter Number : ")
units=int(raw_input("Please Enter Units Cousumed : "))
if(units<100):
     amt=units*10
     print "your total bill is",amt
elif(units>100 & units<=200):
    amt=(100*10)+((units-100)*12)
    print "your total bill is",amt
elif(units>200 & units<=300):
    amt=(100*10)+(100*12)+((units-200)*15)
    print "your total bill is",amt
elif(units>300 & units<=400):
    amt=(100*10)+(100*12)+(100*15)+((units-300)*20)
    print "your total bill is",amt
elif(units>400 & units<=500):
    amt=(100*10)+(100*12)+(100*15)+(100*20)+((units-400)*25)
    print "your total bill is",amt
elif(units>500 & units<=1000):
    amt=(100*10)+(100*12)+(100*15)+(100*20)+(100*25)+((units-500)*30)
    print "your total bill is",amt
else:
	print "Dear:", x
	print "your meter number:",z
	print "you have consumed %d units" % y
	print "total:",total*50

 
 




