alg = input().split()
time = 0
loop = []
loopValue = 1

if alg[0] == "INICIO":
    for i in range(len(alg)):
        if alg[i] == "IO":
            time += 30*loopValue
        elif alg[i] == "MEM":
            time += 10*loopValue
        elif alg[i] == "PROCSUM":
            time += 1*loopValue
        elif alg[i] == "PROCMULT":
            time += 10*loopValue
        elif alg[i] == "LOOP":
            length = int(alg[i+1])
            loop.append(length)
            loopValue *= length
        elif alg[i] == "FIMLOOP":
            loopValue = int(loopValue/(loop.pop()))

print(time)
