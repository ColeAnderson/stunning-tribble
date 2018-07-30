
real = []
hypo = []

freal = open("realSites.txt", "r")
for i in freal:
    real.append(i)
freal.close()

fhypo=open("outCoUkActualValidWp.txt")
for i in fhypo:
    s = str(i)
    hypo.append(s.lower())
fhypo.close()
length = len(hypo)

count = 0
frequency = 0
while(count < length):
    if real[count]==hypo[count]:
        frequency = frequency+1
    else:
        # print(hypo[count])
        print("Real : "+str(real[count])+"Hypo : "+str(hypo[count])+"\n----------\n")
    count = count+1

print("\n\n-----------------------\n\n")
print("frequency = "+str(frequency))

