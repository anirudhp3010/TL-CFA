from SimpleTree import Formula
from Traces import Time


def main():

    f = Formula.convertTextToFormula("G[2,4](x0>1)")
    t = Time()
    sat_best = t.Sat_Best_Time(f)
    sat_worst = t.Sat_Worst_Time(f)
    vio_best = t.Vio_Best_Time(f)
    vio_worst = t.Vio_Worst_Time(f)
        
    print(sat_best)
    print(sat_worst)
    print(vio_best)
    print(vio_worst)

if __name__ == "__main__":
    main()
