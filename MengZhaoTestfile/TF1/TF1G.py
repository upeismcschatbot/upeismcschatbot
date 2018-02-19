QN = open("TF1QN.txt",'r')
QT = open("TF1QT.txt",'r')
CN = open("TF1CN.txt",'r')
CT = open("TF1CT.txt",'r')
TF1 = open("TF1.txt",'w')

i = 1
e = []
h = []
g = []
r = []
for ee in QN:
    e.append(ee)
for hh in CN:
    h.append(hh)

for rr in QT:
    r.append(rr)
for gg in CT:
    g.append(gg)


    
for q in e:
    for cn in h:
        TF1.write("Q "+str(i)+": what is "+q[:-1]+" of " +cn[:-1]+ " ? ")
        TF1.write("\nA "+str(i)+": SELECT "+q[:-1]+" FROM TF1 WHERE CRS_NAME = "+cn[:-1]+"\n")
        TF1.write("\n")
        i += 1

for q in r:
    for ct in g:
        TF1.write("Q "+str(i)+": what is "+q[:-1]+" of " +cn[:-1]+ " ? ")
        TF1.write("\nA "+str(i)+": SELECT "+q[:-1]+" FROM TF1 WHERE CRS_TITLE = "+ct[:-1]+"\n")
        TF1.write("\n")
        i += 1


            



print("done")
QN.close()
CN.close()
QT.close()
CT.close()
TF1.close()
