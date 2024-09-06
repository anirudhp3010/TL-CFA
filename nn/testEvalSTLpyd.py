from SimpleTree import Formula
from Traces import lineToTrace, Trace
import numpy as np
import csv
def main():
    #x1- bingen
    #x2- count
    #x3- year
    #x4- avgsal
    #x5- lifeexp

    #"G[0,1](&(&(x0>30,x1>1700),&(x2>35,x3>7)))"
    #"G[2,3](x4>10000)"
    #"G[0,1](x1<441)"
    #"G[0,1](x3<96)"
    #"G[2,3](x4>85)"
    #"['bingen','count','year','avgsal','lifeexp']"
    #"x1>433774"
    #"G[2,2](x3>97650)"
    #"G[3,4](x4>85)"
    #"G[1,1](x0>0.5)"
    '''
    First case study
     x0>avg - protected
    #x>avg all zeros
    G[2,2] x2> avg - salary
    G[3,4] x3> avg- life exp
    '''
    f = Formula.convertTextToFormula("x4>215000")
    s='outputcon.csv'
    file1 = open('ds1_n (1).txt', 'r')
    Lines = file1.readlines()
    # n is the number of the trajectories 
    n = 408
    T = 14
          
    data = np.empty([n,T])
    counter = 0


    for line in Lines:     
         #print(line)

         [trace, trace2,num] = lineToTrace(line) # convert the trajectory to T by n array. T is the number of the time steps, n is the dimemsion of the trajectiry 
         
         for i in range(0,T):
             
             b = Trace(trace2).evaluateFormulaOnTraceSTL(f,i)  # evaluate the truth value of formula f at time a given time step
             data[counter,i]=b

         counter = counter+1
    #rint(data)
    with open(s, 'w', newline='') as csvfile:
        # Create a CSV writer object
        writer = csv.writer(csvfile)
        for row in data:
            writer.writerow(row)
        
   
   

    
   # line = file1.readline() # read the trajectory from the text file
   # [trace, trace2,num] = lineToTrace(line) # convert the trajectory to T by n array. T is the number of the time steps, n is the dimemsion of the trajectiry 
   # b = Trace(trace2).evaluateFormulaOnTraceSTL(f,0)  # evaluate the truth value of formula f at time a given time step
   # print(b)
        
# !(F[0,1](G[1,3](x1<6)))

#unary operators: G[1,3](x1<6)

#binary operatirs: U[1,3](F[2,3](x3f = Formula.convertTextToFormula("
                                
#binary_operators = ["&", "|", r"U\[\d,\d\]","->"]

#unary_operators = ["X", r"F\[\d,\d\]", r"G\[\d,\d\]", "!"]   

if __name__ == "__main__":
    main()



