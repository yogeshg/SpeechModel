import nltk
from nltk.probability import (ConditionalProbDist, ConditionalFreqDist,
                              MLEProbDist)
from nltk.probability import LidstoneProbDist, WittenBellProbDist
import numpy, random, re

import kalki					#TODO: in constructor

STARTWORD	= kalki.STARTWORD	# field
STOPWORD	= kalki.STOPWORD	# field
TEXT	= kalki.TEXT

unigrams = []					# field (or not?)
lengths  = []

for line in TEXT:
	words = line.split()
	lengths.append( len(words) )
	unigrams.extend( words )

# estimator = None
# estimator = lambda fdist, bins: MLEProbDist(fdist)
estimator = lambda fdist, bins: LidstoneProbDist(fdist, 0.2)			# field
# estimator = lambda fdist, bins: WittenBellProbDist(fdist, 0.2)

model1 = nltk.model.ngram.NgramModel(1, unigrams, estimator=estimator)	# field
model2 = nltk.model.ngram.NgramModel(2, unigrams, estimator=estimator)	# field
model3 = nltk.model.ngram.NgramModel(3, unigrams, estimator=estimator)	# field

def musigma( arr ):
	arr = numpy.array(arr)
	return (arr.mean(), arr.std())

(mu, sigma) = musigma(lengths)	# field

lambda1 = 0.20
lambda2 = 0.35
lambda3 = 0.45

theta1 = lambda1			# field
theta2 = theta1 + lambda2	# field
theta3 = theta2 + lambda3	# field

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
			dia = dia[0:-1]							#FIXME: Why this hack? :O
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

#TODO analyze perprlexity
#TODO make class
#TODO work on argo
