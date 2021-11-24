from collections import Counter

c = Counter()

c['red']+=1

cars =  ['red', 'blue', 'black', 'black', 'black', 'red', 'blue', 'red', 'white']

c = Counter(cars)
print(c)