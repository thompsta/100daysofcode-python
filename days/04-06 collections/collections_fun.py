from collections import defaultdict, namedtuple, Counter, deque
import csv
import random
from urllib.request import urlretrieve
import timeit

'''
tuples / namedtuples

namedtuples == elegant + readable

'''
user = ('stan', 'baller')

print(f'{user[0]} is a {user[1]}')

User = namedtuple('User','name role')

user = User(name='stan', role='baller')

print(user.name)

#named tuples allow you to access each value by attribute, makes more more readible code
print(f'{user.name} is a {user.role}')

'''
defaultdict

great way to build up a nested data structure
'''

#good for nested data structuures and when keys may not be present
users = {'stan': 'baller'}

#solid way of getting values by key
users.get('stan')

challenges_done = [('mike', 10), ('julian', 7), ('bob', 5),
                   ('mike', 11), ('julian', 8), ('bob', 6)]

print(challenges_done)

#apparently this throws a KeyError for 'mike' because he is not present in the first round
'''challenges = {}
for name, challenge in challenges_done:
    challenges[name].append(challenge)'''

# default dict never raises a KeyError, any key that does not exist gets the value returned by the default factory (function). 
# Be sure to pass the function object to defaultdict()
# Do not call the function, i.e. defaultdict(func), not defaultdict(func())
challenges = defaultdict(list)
for name, challenge in challenges_done:
    challenges[name].append(challenge)

print(challenges)

'''
counter

dont reinvent the wheel...
'''

words = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been 
the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and 
scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into 
electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of
Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus
PageMaker including versions of Lorem Ipsum""".split()

print(words[:5])

#getting most common words without Collections
#keep a dictionary, loop over words, see if word is in dictionary, if not set to 0, if it is add 1
common_words = {}
for word in words:
    if word not in common_words:
        common_words[word] = 0
    common_words[word] += 1
# loop over values in k, v pairs
# sort dict by values descending and slice first 5 to get most common
for k, v in sorted(common_words.items(),
                   key=lambda x: x[1],
                   reverse=True)[:5]:
    print(k ,v)

# now using Counter and its most_common method
print(Counter(words).most_common(5))

'''

deque

Deques are a generalization of stacks and queues 
(the name is pronounced “deck” and is short for “double-ended queue”). 
Deques support thread-safe, memory efficient appends and pops from either 
side of the deque with approximately the same O(1) performance in either direction.

If you need to add/remove at both ends of a collection, consider using a deque.

'''
#create list of 10,000,000 ints
lst = list(range(10000000))
deq = deque(range(10000000))

#takes sequence and randomly choose one item, remove item at index of random item, and insert the same value
def insert_and_delete(ds):
    #its conventional in python to use _ for throwaway variables
    for _ in range(10):
        index = random.choice(range(100))
        ds.remove(index)
        ds.insert(index, index)

#%timeit is an ipython magic function, which can be used to time a particular piece of code
#timeit module can be used too (for when not using ipython)
print(timeit.timeit('insert_and_delete(lst)',number=1,globals=globals()))

#apparently deques 
print(timeit.timeit('insert_and_delete(deq)',number=1,globals=globals()))

