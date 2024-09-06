from SimpleTree import Formula
from Traces import lineToTrace, Trace
import numpy as np
import pandas as pd
import csv
def main():
    # f = Formula.convertTextToFormula("G[1,3](&(&(x0>30,x1<1700),&(x2>35,x3>7)))")
    # m = ['Current_Gear', 'Fuel_consumption', 'Accelerator_Pedal_value',
    # 'Throttle_position_signal', 'Engine_speed', 'Engine_soacking_time', 'Torque_of_friction']
    f = [None]*10
    # f = Formula.convertTextToFormula("G[0,12](&(x2<64.45,&(x0<2,x0>0)))")

    f[0] = Formula.convertTextToFormula("&(G[0,11](x2<64.45),G[0,12](&(x0<2,x0>0)))")
    f[1] = Formula.convertTextToFormula("&(G[0,11](x2<64.45),G[0,12](&(x0<2,x0>0)))")
    f[2] = Formula.convertTextToFormula("&(G[0,11](x2<64.45),G[0,12](&(x0<2,x0>0)))")
    f[3] = Formula.convertTextToFormula("&(G[0,11](x2<64.45),G[0,12](&(x0<2,x0>0)))")
    f[4] = Formula.convertTextToFormula("&(G[0,11](x2<64.45),G[0,12](&(x0<2,x0>0)))")
    f[5] = Formula.convertTextToFormula("&(G[0,11](x2<64.45),G[0,12](&(x0<2,x0>0)))")
    f[6] = Formula.convertTextToFormula("G[15,19](x1>380.95)")
    f[7] = Formula.convertTextToFormula("G[15,19](x3<6.7901)")
    f[8] = Formula.convertTextToFormula("G[15,19](x4<691.54)")
    f[9] = Formula.convertTextToFormula("G[15,19](x5<0)")

    s = 'outputcd.csv'
    file1 = open('trajforcd.txt', 'r')
    Lines = file1.readlines()
    # n is the number of the trajectories
    # T is the number of time-steps
    n = 44
    T = 1400
    m = 10
    data = [[[0 for _ in range(T)] for _ in range(n)] for _ in range(m)]
    counter = 0
    for line in Lines:
        # print(line)
        # convert the trajectory to T by n array. T is the number of the time steps, m is the dimemsion of the trajectiry
        [trace, trace2, num] = lineToTrace(line)
        # print(trace2)
        for i in range(0, T):
            for j in range(0, m):
                b = Trace(trace2).evaluateFormulaOnTraceSTL(f[j], i)  # evaluate the truth value of formula f at time a given time step
                data[j][counter][i] = b
        counter = counter+1

    #print(data)
    excel_writer = pd.ExcelWriter('output.xlsx', engine='openpyxl')

    # Iterate through the depth of the 3D array
    for depth_idx, array_2d in enumerate(data):
        # Convert each 2D array into a DataFrame
        df = pd.DataFrame(array_2d)

        # Write the DataFrame to a separate sheet with a specific name
        sheet_name = f'Sheet{depth_idx + 1}'  # Naming the sheets Sheet1, Sheet2, ...
        df.to_excel(excel_writer, sheet_name=sheet_name, index=False, header=False)

    # Save the Excel file
    excel_writer.close()



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



