import os

n=1
while n==1:

	a=[1,0,0]  
	b=[1,0,0]  
	c=[1,1,1]
  
	print(a)
	print(b)
	print(c)

	os.system('clear')
	 
	origin=[a,b,c] 
	  
	def rotate(org_list):    # according the matrix line and squeue take a reverse  
	    lenth=org_list.__len__()        #get the lenth of the list  
	    width=org_list[0].__len__()     #get the width of the list  
	    new_matrix=list()               #create a new empty list  
	  
	    for i in range(0,width):  
	        newline=[]  # empty the list  
	        for j in range(lenth-1,-1,-1):  
	            newline.append(org_list[j][i])  
	        new_matrix.append(newline) # add the new list into the target 2 dimension list  
	    return new_matrix  
	  
  
	print rotate(origin) 
	os.system('clear')
