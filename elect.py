print "Enter customer details"
print "name of the customer"
x= raw_input(str)
print "meter number"
z=raw_input(int)
print"Enter the units consumed"
y=raw_input(int)
units=int(y)f(units<=100):
	print 'Dear',name
	print "Your Meter Number is: ",meter_no
	print "You have Consumed %d units" % (units)
	print "Total Price is :", units*10
elif (units>100 and units<=200):
	units1=units-100
	price=(100*10)+(units1*12)
	print 'Dear',name
	print "Your Meter Number is: ",meter_no
	print "You have Consumed %d units" % (units)
	print "Total Price is :", price
elif (units>200 and units<=300):
	units1=units-200
	price=(100*10)+(100*12)+(units1*15)
	print 'Dear',name
	print "Your Meter Number is: ",meter_no
	print "You have Consumed %d units" % (units)
	print "Total Price is :", price
elif (units>300 and units<=400):
	units1=units-300
	price=(100*10)+(100*12)+(100*15)+(units1*20)
	print 'Dear',name
	print "Your Meter Number is: ",meter_no
	print "You have Consumed %d units" % (units)
	print "Total Price is :", price
elif (units>400 and units<=500):
	units1=units-400
	price=(100*10)+(100*12)+(100*15)+(100*20)+(units4*25)
	print 'Dear',name
	print "Your Meter Number is: ",meter_no
	print "You have Consumed %d units" % (units)
	print "Total Price is :", price
elif (units>500 and units<=1000):
	units1=units-500
	price=(100*10)+(100*12)+(100*15)+(100*20)+(100*25)+(units4*30)
	print 'Dear',name
	print "Your Meter Number is: ",meter_no
	print "You have Consu.0med %d units" % (units)
	print "Total Price is :", price
else:
	print 'Dear',name
	print "Your Meter Number is: ",meter_no
	print "You have Consumed %d units" % (units)
	print "Total Price is :", units*50