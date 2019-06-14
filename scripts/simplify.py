import sys

if len(sys.argv)!=2:
    exit(-1)

file = sys.argv[1]
count = 0
with open(file) as f:
    for line in f.readlines():
        if '>' not in line:
            print(line.upper().replace('\n','').replace('N',''),end='')
        else:
            if count>=32:
                break
            count+=1
            print('\n',end='')
print("Total blocks",count,file=sys.stderr)