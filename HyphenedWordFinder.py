import re
from nltk.corpus import wordnet as wn
hyWordPtrn = re.compile(r'\b[a-z]{2,15}-[a-z]{2,15}\b')

def readLines (file):
    f = open (file, 'r')
    lns = [line for line in f]
    f.close()

    return lns

def hyWordFinder(file = 'hfind.txt'):
    lns = readLines(file)
    lnsSt = readLines('standrt.txt')

    hyWds = {}
    for l in lns:
        hWs = hyWordPtrn.findall(l)
        for w in hWs:
            w1 = w.replace('-','')
            w2 = w.replace('-',' ')
            if wn.synsets(w1) != [] and hyWds.get(w1) == None:
                hyWds[w1] = w2
                for ln in lnsSt:
                    if ln.find(w1) != -1:
                        print(w1)

    return hyWds

hwds = hyWordFinder()
f = open('1.txt','w')
for key, value in hwds.items():
    f.write(value + "," + key + '\n')
f.close()
print(hwds, '\n', len(hwds))