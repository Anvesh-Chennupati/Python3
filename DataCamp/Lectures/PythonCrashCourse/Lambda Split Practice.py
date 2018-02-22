t = lambda var : var**2

l1 = list(range(1,25))



#print('\n',list(map(lambda x: x**3,l1)))

domains = ['anvesh@conduent.com','anvesh@gmail.com','acn@yahoo.com','x@apple.com']
"""
d2 = []

for i in domains:
  d2.append(i.split('@')[1])
  
print(d2)
"""

s = 'There are two dogs on the road. First dog is A and second dog is B.'

s1 = list(s.split(' '))

count = 0

for i in s1:
  if i == 'dogs' or i == 'dog':
    count = count + 1

print(count)
