import json,random,string,hashlib,time

rooters=json.load(open("./source_root_basic_info.json"))
dnaCount={}

while True:
    a=random.choice(list(rooters.values()))
    b=random.choice(list(rooters.values()))
    if a!=b:
        break

def genNew(a,b):
    n={}
    dna=""
    for i in range(len(a["dna"])):
        choice=random.randint(0,10000)
        if choice<4995:
            dna+=a["dna"][i]
        elif choice>=4995 and choice<9990:
            dna+=b["dna"][i]
        else:
            dna+=random.choice(string.ascii_letters+string.digits)
    if dna==a["dna"] or dna==b["dna"]:
        n=genNew(a,b)
    n["name"]="".join([random.choice(string.ascii_letters+string.digits) for _ in range(32)])
    n["dna"]=dna
    n["hash"]=hashlib.md5(bytes(n["name"]+n["dna"],"utf-8")).hexdigest()
    n["root"]=[a["name"],b["name"]]
    n["borntime"]=time.time()
    n["factor"]=max(a["factor"],b["factor"])+1
    return n

bios=rooters.copy()
while len(bios)<2000:
    while True:
        a1=random.choice(list(bios.values()))
        b1=random.choice(list(bios.values()))
        #a1=list(bios.values())[-1]
        #b1=list(bios.values())[-2]
        if a1!=b1:
            n=genNew(a1,b1)
            bios[n["name"]]=n
            count={}
            for j in string.ascii_letters+string.digits:
                count[j]=bios[n["name"]]["dna"].count(j)
                dnaCount[n["name"]]=count
            break

with open("save_genes_basic.json","w") as f:
    f.write(json.dumps(bios,indent=4))

with open("save_genes_count.json","w") as f:
    f.write(json.dumps(dnaCount,indent=4))