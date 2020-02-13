'''
Text Analysis is a major application field for machine 
learning algorithms. However the raw data, a sequence of 
symbols cannot be fed directly to the algorithms 
themselves as most of them expect numerical feature vectors 
with a fixed size rather than the raw text documents 
with variable length.
'''

# We will use CountVectorizer to 
# "convert text into a matrix of token counts":

# example text for model training (SMS messages)
simple_train = ['call you tonight', 
                'Call me a cab', 
                'please call me... PLEASE!']

# import and instantiate CountVectorizer (with the 
# default parameters)
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
vect = CountVectorizer()

# learn the 'vocabulary' of the training data (occurs in-place)
vect.fit(simple_train)

# examine the fitted vocabulary
print(vect.get_feature_names())

# transform training data into a 'document-term matrix'
simple_train_dtm = vect.transform(simple_train)
print(simple_train_dtm)
# <3x6 sparse matrix of type '<class 'numpy.int64'>'
# with 9 stored elements in Compressed Sparse Row format>

# convert sparse matrix to a dense matrix
simple_train_dtm.toarray()
'''
array([[0, 1, 0, 0, 1, 1],
       [1, 1, 1, 0, 0, 0],
       [0, 1, 1, 2, 0, 0]])
'''

# examine the vocabulary and document-term matrix together
pd.DataFrame(simple_train_dtm.toarray(), columns=vect.get_feature_names())

'''
	cab	call me	 please	tonight	you
0	0	1	 0	 0	    1	    1
1	1	1	 1	 0	    0	    0
2	0	1	 1	 2	    0	    0
If a word appears in a sentence, then it has a 1

Each individual token occurrence frequency (normalized or not) 
is treated as a feature.

The vector of all the token frequencies for a given document
is considered a multivariate sample.

A corpus of documents can thus be represented by a matrix 
with one row per document and one column per token (e.g. word) 
occurring in the corpus.

We call vectorization the general process of turning a 
collection of text documents into numerical feature vectors. 
This specific strategy (tokenization, counting and 
normalization) is called the Bag of Words or "Bag of n-grams" 
representation. Documents are described by word occurrences 
while completely ignoring the relative position information 
of the words in the document.
'''

print(simple_train_dtm)

'''
['cab', 'call', 'me', 'please', 'tonight', 'you']
(0, 1)        1
(0, 4)        1
(0, 5)        1
Means that word call appears one time in first sentence
Word tonight appears one time in first sentence
Word you appears one time in first sentence
'''

'''
In order to be able to store such a matrix in memory 
but also to speed up operations, implementations will 
typically use a sparse representation such as the
implementations available in the scipy.sparse package.
'''

# example text for model testing
simple_test = ["please don't call me"]

# In order to make a prediction, the new observation
# must have the same features as the training observations, 
# both in number and meaning.

# transform testing data into a document-term matrix (using existing vocabulary)
simple_test_dtm = vect.transform(simple_test)
simple_test_dtm.toarray()
'''
array([[0, 1, 1, 1, 0, 0]])
'''

pd.DataFrame(simple_test_dtm.toarray(), columns=vect.get_feature_names())
'''
    cab	call	me	please	tonight	you
0	0	1	    1	1	    0	    0
'''

#vect.fit(train) learns the vocabulary of the training data
#vect.transform(train) uses the fitted vocabulary to build a document-term matrix from the training data
#vect.transform(test) uses the fitted vocabulary to build a document-term matrix from the testing data (and ignores tokens it hasn't seen before)


