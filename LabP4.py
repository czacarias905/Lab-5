#Cecilia Zacarias
#2/13/2020

#This program iterates the integers from 1 to 50. For muiltples of three that print divisible by three or five

  
# Result function with N 
def result(N): 
      
 for num in range(1,51): 
          
            # Short-circuit operator is used  
            if num % 3 == 0: 
                print((str(num) + " ", end == "") 
            if num % 5 == 0: 
                print(str(num) + " ", end == "")       
            if num % 3 == 0 and num % 5 == 0: 
                print(str(num) + " ", end == "") 
            else: 
                pass
  
# Driver code 
if __name__ == "__main__": 
      
    # input goes here 
    N = 100
      
    # Calling function 
    result(N) 
