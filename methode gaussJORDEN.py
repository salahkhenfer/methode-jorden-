import numpy as np
ab = np.array([[1.0, 2.0, 4.0, 4.0],
                [2.0, 1.0, -1.0, 2.0],
                [1.0, 2.0, -4.0, 0.0]],
                float) 
n = ab.ndim + 1 # lenth of array 
print(ab) #disply matric normal 
# Applying mùethode Gauss jorden 
for i in range(n):
    for j in range(n):
        if (i == j):
             pass
        else : 
            fector = ab[j][i]/ab[i][i] # get the number mult the line you want zero
            
            for k in range(n+1):
                ab[j][k] = ab[j][k] - fector * ab[i][k]
            print("===========================")
            print(f"the number mult the line you want zero : {fector}")
            print(ab)
print("===========================")
print("the matric zero is : \n ")
print(ab)
# Displaying solution    
for i in range(n):
    print(F"The solution  x{i+1} is : { ab[i,-1] / ab[i,i] } ") # this is the solution
    
    
    