from SimpleTree import Formula
from Traces import lineToTrace, Trace
import numpy as np
def main():

   # f = Formula.convertTextToFormula("G[1,3](&(&(x0>30,x1<1700),&(x2>35,x3>7)))")
    f = Formula.convertTextToFormula("G[0,1](x2<0.05)")
    file1 = open('trajfull.txt', 'r')
    Lines = file1.readlines()
    # n is the number of the trajectories 
    # T is the number of time-steps
    n = 200
    T = 14
          
    data = np.empty([n, T])
    counter = 0
    for line in Lines:     
         #print(line)
 
         [trace, trace2,num] = lineToTrace(line) # convert the trajectory to T by n array. T is the number of the time steps, m is the dimemsion of the trajectiry 
         #print(trace2)
         for i in range(0,T):
             
             b = Trace(trace2).evaluateFormulaOnTraceSTL(f,i)  # evaluate the truth value of formula f at time a given time step
             data[counter,i]=b
         counter = counter+1
    print(data)        
   
   

    
   # line = file1.readline() # read the trajectory from the text file
   # [trace, trace2,num] = lineToTrace(line) # convert the trajectory to T by n array. T is the number of the time steps, n is the dimemsion of the trajectiry 
   # b = Trace(trace2).evaluateFormulaOnTraceSTL(f,0)  # evaluate the truth value of formula f at time a given time step
   # print(b)
        
# !(F[0,1](G[1,3](x1<6)))

# &(G[1,2](x1>4),|(x>2,x4<5))
#unary operators: G[1,3](x1<6)

# &(x0>9,x2<8)
# G[1,2](&(x0>9,x2<8))

#binary operatirs: U[1,3](F[2,3](x3f = Formula.convertTextToFormula("
                                
#binary_operators = ["&", "|", r"U\[\d,\d\]","->"]

#unary_operators = ["X", r"F\[\d,\d\]", r"G\[\d,\d\]", "!"]   

if __name__ == "__main__":
    main()



