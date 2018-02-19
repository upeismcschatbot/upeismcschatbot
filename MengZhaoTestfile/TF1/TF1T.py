import MySQLdb
db = MySQLdb.connect("137.149.157.4","chatbot_readonly","gitRdone12358","chatbot" )
cursor = db.cursor()

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
        TF1.write("Q "+str(i)+": what is the "+q[:-2]+" of " +cn[:-1]+ " ? ")
        cursor.execute("SELECT "+q[:-1]+" FROM course_details_from_colleague WHERE CRS_NAME = \""+cn[:-1]+"\";")
        data = cursor.fetchone()
        TF1.write("\n"+str(data))
        TF1.write("\n")
        i += 1

for q in r:
    for ct in g:
        TF1.write("Q "+str(i)+": what is the "+q[:-1]+" of " +ct[:-2]+ " ? ")
        cursor.execute("SELECT "+q[:-1]+" FROM course_details_from_colleague WHERE CRS_TITLE = \""+ct[1:-2]+"\";")
        data = cursor.fetchone()
        TF1.write("\n"+str(data))
        TF1.write("\n")
        i += 1


            



print("done")
QN.close()
CN.close()
QT.close()
CT.close()
TF1.close()
