# Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output, where every other
# element of the input tuple is copied, starting with the first one. So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'),
# then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple').

animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}
del animals['b']

print(animals.items())