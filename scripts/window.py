# here the sequence breaking and window will be formed
from data_structures import *
wind=list(map(int, input().split()))
sc=[arr0,arr1,arr2,arr3]
se=[[],[],[],[]]

def mismatch(x):
    return round(sum(1 for w in x if w not in nms)/len(x),3)
def coverage(x):
    return round(sum(1 for w in x if w in nms)/len(x),3)

for t in wind:
    for i in range(4):
        al=len(sc[i])
        for k in range(al-t+1):
            se[i].append(tuple(sc[i][k:k+t]))        

    nms=set(se[0])       # the base sequences (normal syscall set)
    cpu_ano=se[1]        # the sequences under cpu stress
    IO_ano=se[2]         # the sequences under Input/Output stress
    mem_ano=se[3]        # the sequences under memory stress

    mis_rate_cpu, cov_cpu = mismatch(cpu_ano), coverage(cpu_ano)
    mis_rate_IO, cov_IO = mismatch(IO_ano), coverage(IO_ano)
    mis_rate_mem, cov_mem = mismatch(mem_ano), coverage(mem_ano)
    
    with open("../results/results.csv","a") as result:
        result.write(f"\n{t},cpu,{mis_rate_cpu},{cov_cpu}")
        result.write(f"\n{t},I/O,{mis_rate_IO},{cov_IO}")
        result.write(f"\n{t},mem,{mis_rate_mem},{cov_mem}")


# k, condition, mismatch_rate, coverage
