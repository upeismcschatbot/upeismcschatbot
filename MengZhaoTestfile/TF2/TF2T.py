import MySQLdb
db = MySQLdb.connect("137.149.157.4","chatbot_readonly","gitRdone12358","chatbot" )
cursor = db.cursor()

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
        TF1.write("Q "+str(i)+": what is "+q[:-2]+" of " +cn[:-1]+ "?\n")
        cursor.execute("SELECT `"+q[:-2]+"` FROM course_section_details_from_colleague WHERE `Short Title` = \""+cn[:-1]+"\";")
        data = cursor.fetchone()
	TF1.write(str(data))
        TF1.write("\n")
        i += 1

for q in r:
    for ct in g:
        TF1.write("Q "+str(i)+": what is "+q[:-2]+" of " +ct[1:-1]+ "?\n")
        cursor.execute("SELECT `"+q[:-2]+"` FROM course_section_details_from_colleague WHERE `Section Name` = \""+ct[1:-1]+"\";")
        data = cursor.fetchone()
        TF1.write(str(data))
        TF1.write("\n")
        i += 1

for f in e:
    for cn in h:
        for s in p:
            TF1.write("Q "+str(i)+": what is "+f[1:-2]+" of " +cn[:-1]+ " at "+s[:-1]+"?\n")
            cursor.execute("SELECT `"+f[1:-2]+"` FROM course_section_details_from_1colleague WHERE `Short Title` = \""+cn[:-1]+"\" , Term = "+s[:-1]+";")
            data = cursor.fetchone()
            TF1.write(str(data))
            TF1.write("\n")
            i += 1

for o in r:
    for ct in g:
        for s in p:
            TF1.write("Q "+str(i)+": what is "+o[1:-2]+" of " +ct[1:-1]+ " at "+s[:-1]+"?\n")
            cursor.execute("SELECT `"+o[1:-2]+"` FROM course_section_details_from_colleague WHERE `Section Name` = \""+ct[1:-1]+"\" , Term = "+s[:-1]+";")
            data = cursor.fetchone()
            TF1.write(str(data))
            TF1.write("\n")
            i += 1
            



print("done")
QN.close()
CN.close()
QT.close()
CT.close()
S.close()
TF1.close()

