import sys
import numpy as np

def sumfactorial(inp):

    
    fact=np.math.factorial(inp)                                      #gets factorial using numpy
    
    sum = 0                                                       #variable for sum of digits
    
    while fact:                                                    #loop to sum factorial digits
        sum, fact = np.add(sum, np.mod(fact,10)), fact//10
        #sum, fact = sum + fact % 10 , fact//10                              #this is faster, does not use numpy though
        #sum, fact = np.add(sum, np.mod(fact,10)), np.floor_divide(fact,10)  #"np.floor_divide" not giving correct value, for input of 100

    return(sum)



if __name__ == "__main__":    
    
    try:                                                        #checks for valid input arguments
        sys.argv[1].isdigit()                               
        print(sumfactorial(int(sys.argv[1])))
    except ValueError:
        print("please enter a non-negative integer")
    except IndexError:
        print("please include your input as an argument")

    