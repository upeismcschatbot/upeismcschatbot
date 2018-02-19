QN = open("TF2QN.txt",'r')
QT = open("TF2QT.txt",'r')
CN = open("TF2CN.txt",'r')
CT = open("TF2CT.txt",'r')
S = open("TF2S.txt",'r')
TF1 = open("TF2.txt",'w')

TS = open("TS.txt",'r')
NS = open("NS.txt",'r')
i = 1
e = []
h = []
g = []
r = []
p = []
o = []
f = []
for ee in QN:
    e.append(ee)
for hh in CN:
    h.append(hh)

for rr in QT:
    r.append(rr)
for gg in CT:
    g.append(gg)

for pp in S:
    p.append(pp)




for oo in TS:
    o.append(oo)
for ff in NS:
    f.append(ff)
    
for q in e:
    for cn in h:
        TF1.write("Q "+str(i)+": what is "+q[:-1]+" of " +cn[:-1]+ " ? ")
        TF1.write("\nA "+str(i)+": SELECT "+q[:-1]+" FROM course_section_details_from_colleague WHERE Section Name = "+cn[:-1]+";\n")
        TF1.write("\n")
        i += 1

for q in r:
    for ct in g:
        TF1.write("Q "+str(i)+": what is "+q[:-1]+" of " +cn[:-1]+ " ? ")
        TF1.write("\SELECT "+q[:-1]+" FROM course_section_details_from_colleague WHERE Short Title = "+ct[:-1]+";\n")
        TF1.write("\n")
        i += 1

for f in e:
    for cn in h:
        for s in p:
            TF1.write("Q "+str(i)+": what is "+q[:-1]+" of " +cn[:-1]+ " at "+s+" ? ")
            TF1.write("\nSELECT "+q[:-1]+" FROM course_section_details_from_colleague WHERE Section Name = "+cn[:-1]+" , Term = "+s+";\n")
            TF1.write("\n")
            i += 1

for o in r:
    for ct in h:
        for s in p:
            TF1.write("Q "+str(i)+": what is "+q[:-1]+" of " +ct[:-1]+ " at "+s+" ? ")
            TF1.write("\nSELECT "+q[:-1]+" FROM course_section_details_from_colleague WHERE Short Title = "+ct[:-1]+" , Term = "+s+";\n")
            TF1.write("\n")
            i += 1
            



print("done")
QN.close()
CN.close()
QT.close()
CT.close()
S.close()
TF1.close()
