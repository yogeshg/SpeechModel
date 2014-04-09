import nltk
from nltk.probability import (ConditionalProbDist, ConditionalFreqDist,
                              MLEProbDist)
from nltk.probability import LidstoneProbDist, WittenBellProbDist
import numpy, random, re, time

import kalki

STARTWORD	= kalki.STARTWORD
STOPWORD	= kalki.STOPWORD
TEXT	= kalki.TEXT

unigrams = []
lengths  = []


for line in TEXT:
	words = line.split()
	lengths.append( len(words) )
	unigrams.extend( words )

# estimator = None
# estimator = lambda fdist, bins: MLEProbDist(fdist)
estimator = lambda fdist, bins: LidstoneProbDist(fdist, 0.2)
# estimator = lambda fdist, bins: WittenBellProbDist(fdist, 0.2)

model1 = nltk.model.ngram.NgramModel(1, unigrams, estimator=estimator)

model2 = nltk.model.ngram.NgramModel(2, unigrams, estimator=estimator)

model3 = nltk.model.ngram.NgramModel(3, unigrams, estimator=estimator)

def musigma( arr ):
	arr = numpy.array(arr)
	return (arr.mean(), arr.std())

(mu, sigma) = musigma(lengths)

lambda1 = 0.20
lambda2 = 0.35
lambda3 = 0.45

theta1 = lambda1
theta2 = theta1 + lambda2
theta3 = theta2 + lambda3

def generateDialog():
	x = random.normalvariate(0,1)
	l = max( int( mu + x*sigma ) , 15 )
	
	dia = [ STARTWORD ]
	while( len(dia) < l or dia[-1]!=STOPWORD):
		r = random.random()
		if r <= theta1:
			dia = model1.generate(1,context=dia)
		elif r <= theta2:
			dia = model2.generate(1,context=dia)
		elif r <= theta3:
			dia = model3.generate(1,context=dia)
		if dia[-1] == '.':
			dia = dia[0:-1]
	return dia

def postprocess(dia):
	startRegex = re.compile( re.escape(STARTWORD)+' (.)' )
	def startRepl(m):
		return m.group(1).upper()
	return startRegex.sub(startRepl, ' '.join(dia)).replace(' '+STOPWORD, '.')

def main():
	print postprocess(generateDialog())

if __name__ == '__main__':
	main()

#FIXME analyze perprlexity
#FIXME make class
