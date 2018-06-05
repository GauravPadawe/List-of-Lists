usa_univs = [ ['California Institute of Technology',2175,37704],
              ['Harvard',19627,39849],
              ['Massachusetts Institute of Technology',10566,40732],
              ['Princeton',7802,37000],
              ['Rice',5879,35551],
              ['Stanford',19535,40569],
              ['Yale',11701,40500]  ]

def total_enrollment(a):                     # Defining a procedure
	i = []                                   # Defining variable having empty list for storing total number of students
	j = []                                   # Defining variable having empty list for storing total number of fees (fees of individual university * number of students enrolled)
	final = []                               # Defining variable having empty list which will store final value (["total number of srudents", "total fees"])
	for x in a:                              # For x (individual value of a)
		#print (x[1])                                  # you can un-comment print to see what's happening in the block
		i.append(x[1])                       # Appending i[] with every x[1] value ,i.e, [2175, 19627, 10566, ...., ]
	for y in a:                              # For y (individual value of a)
		y = y[1] * y[2]                      # As given, total number of fees (fees of individual university * number of students enrolled) so y = y[1] * y[2]
		#print (y)                                     # you can un-comment print to see what's happening in the block
		j.append(y)                          # Appending j[] with every y value
	sum_i = sum(i)                           # sum_i will sum the values in i
	sum_j = sum(j)                           # sum_j will sum the values in j
	final.append(sum_i)                      # Appending sum_i and sum_j to final[]
	final.append(sum_j)
	return final                             # Returning final
	
print (total_enrollment(usa_univs))	