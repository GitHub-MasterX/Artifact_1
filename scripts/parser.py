import re
single=[]
data= [[],[],[],[]] # 0 = normal, 1 = cpu anomal, 2 = i/o anomal, 3 = memory anomaly
files=[['.txt.2975','.txt.2976','.txt.2977','.txt.2978','.txt.2979'], #normal multis
       ['_cpu.3270','_cpu.3275','_cpu.3276','_cpu.3277'],             #cpu stressed syscalls
       ['_io.2827'],                                                  #i/o stressed syscalls   
       ['_mem.2810']                                                  #memory stressed syscalls
       ]
SYSCALL_RE = re.compile(r'^([a-zA-Z_][a-zA-Z0-9_]*)\(')
with open("../data/normal/single.txt",'r',encoding="utf-8") as file:
    for line in file:   
        if '<unfinished' in line or 'resumed>' in line:
            continue
        m=SYSCALL_RE.match(line)
        if m:
            single.append(m.group(1))
for k in range(4):
    for i in files[k]:
        with open(f"../data/normal/multi{i}",'r',encoding="utf-8") as file:
            for line in file:
                if '<unfinished' in line or 'ressumed>' in line:
                    continue
                m=SYSCALL_RE.match(line)
                if m:
                    data[k].append(m.group(1))
    with open("data_structures.py","a") as fool:
        fool.write(f"\narr{k}={data[k]}")
