from itertools import count
import json,random,string,hashlib,time

sourceDNA={}
sourceCount={}

for i in range(52):
    genes={}
    genes["name"]=string.ascii_letters[i]+str(i+1)
    genes["dna"]="".join([random.choice(string.ascii_letters+string.digits) for _ in range(64)])
    genes["hash"]=hashlib.md5(bytes(genes["dna"],"utf-8")).hexdigest()
    genes["root"]=["SOURCE_BIO","SOURCE_BIO"]
    genes["borntime"]=time.time()
    genes["factor"]=0
    count={}
    for j in string.ascii_letters+string.digits:
        count[j]=genes["dna"].count(j)
    sourceCount[genes["name"]]=count
    sourceDNA[genes["name"]]=genes

for i in sourceDNA:
    print(i,sourceDNA[i])

with open("./data/source_root_basic_info.json","w") as f:
    f.write(json.dumps(sourceDNA,indent=4))

with open("./data/source_root_count_info.json","w") as f:
    f.write(json.dumps(sourceCount,indent=4))
