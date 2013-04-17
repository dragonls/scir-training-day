import sys
import string

if __name__ == "__main__":
    try:
        f=open("gene.counts","r")
    except:
        print>>sys.stderr,"Failed to open file"
        sys.exit(1)

    word=[]
    for line in f:
        line=line.split()
        if line[1]=='WORDTAG' and string.atoi(line[0])<5:
            word.append(line[3])
    f.close()
    # Convert to set for better performence.
    word=set(word)

    try:
        ft=open("gene.train","r")
    except:
        print>>sys.stderr,"Failed to open file"
        sys.exit(1)
    try:
        fo=open("gene.train2","w")
    except:
        print>>sys.stderr,"Failed to open file"
        sys.exit(1)

    for line in ft:
        line=line.split()
        if len(line)>0 and line[0] in word:
            line[0]="_RARE_"
        print>>fo," ".join(line)
    ft.close()
    fo.close()

