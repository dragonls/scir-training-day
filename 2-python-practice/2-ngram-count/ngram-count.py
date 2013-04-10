#!/usr/bin/env python

class NGram(object):

    def __init__(self, n):
        # n is the order of n-gram language model
	self.n = n
	self.unigram=0
	self.bigram=0

    # scan a sentence, extract the ngram and update their
    # frequence.
    #
    # @param    sentence    list{str}
    # @return   none
    def scan(self, sentence):
        # file your code here
	l = sentence.strip()
	self.ngram( l.split() )

    # caluclate the ngram of the words
    #
    # @param    words       list{str}
    # @return   int         count of the ngram
    def ngram(self, words):
        # file your code here
	for i in range(len(words)):
		if(words[i]=="unigram"):
			self.unigram=self.unigram+1
		elif(words[i]=="bigram"):
			self.bigram=self.bigram+1

if __name__=="__main__":
	import sys
	try:
		fpi = open(sys.argv[1], "r")
	except IOError:
		print >> sys.stderr, "failed to open file."
		sys.exit(1)

	try:
		fpou = open("data.uni", "w")
	except IOError:
		print >> sys.stderr, "failed to open data.uni."
		sys.exit(1)
	
	try:
		fpob = open("data.bi", "w")
	except IOError:
		print >> sys.stderr, "failed to open data.bi."
		sys.exit(1)

	N = NGram(1)
	line = fpi.readline()
	while line:
		N.scan(line)
		line = fpi.readline()
	fpou.write(str(N.unigram))
	fpob.write(str(N.bigram))

