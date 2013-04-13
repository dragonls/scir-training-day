#!/usr/bin/env python
import cPickle as pickle
import sys

def max_match_segment( line, dic ):
    # write your code here
	index=0
	maxLen=5
	l=unicode(line, "utf-8")
	end=len(l)
	r=[]
	while index!=end:
		if index+maxLen<end:
			str_end=index+maxLen
		else:
			str_end=end
		tmp=l[index:str_end].encode("utf-8")
		while index < str_end-1:
			if tmp in dic:
				r.append(tmp)
				break;
			else:
				str_end-=1
			tmp=l[index:str_end].encode("utf-8")
		if index==str_end-1:
			r.append(tmp)
		index=str_end
	return r
	

if __name__=="__main__":

    try:
        fpi=open(sys.argv[1], "r")
    except:
        print >> sys.stderr, "failed to open file"
        sys.exit(1)

    try:
        fdic=open(sys.argv[2], "r")
        dic=pickle.load(fdic)
    except:
        print >> sys.stderr, "failed to load dict"
        sys.exit(1)

    try:
        fpo=open("output.dat", "w")
    except:
        print >> sys.stderr, "failed to open file"
        sys.exit(1)

    for line in fpi:
        print >> fpo, "\t".join( max_match_segment( line.strip(), dic) )

