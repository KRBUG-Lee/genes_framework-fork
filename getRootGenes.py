import json
from functools import cache

genes=json.load(open("./data/save_genes_basic.json"))

rooters={}
families={}

@cache
def getRoot(genesName):
    global rooters
    if genesName=="SOURCE_BIO":
        return rooters
    bio=genes[genesName]
    if bio["root"]==["SOURCE_BIO","SOURCE_BIO"]:
        rooters[genesName]=["SOURCE_BIO","SOURCE_BIO"]
        return rooters
    rooters[genesName]=bio["root"]
    rooters.update(getRoot(bio["root"][0]))
    rooters.update(getRoot(bio["root"][1]))
    return rooters

for i in genes:
    families[i]=getRoot(i).copy()
    rooters={}
    
with open("./data/save_genes_family.json","w") as f:
    f.write(json.dumps(families,indent=4))