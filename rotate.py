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
	  
	def rotate(org_list):   
	    lenth=org_list.__len__()        
	    width=org_list[0].__len__()     
	    new_matrix=list()              
	  
	    for i in range(0,width):  
	        newline=[]  
	        for j in range(lenth-1,-1,-1):  
	            newline.append(org_list[j][i])  
	        new_matrix.append(newline)   
	    return new_matrix  
	  
  
	print rotate(origin) 
	os.system('clear')
