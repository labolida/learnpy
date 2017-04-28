#
#Examples from:
#https://wiki.python.org/moin/SimplePrograms
#
#
print 'Hello, world!'

name = raw_input('What is your name?\n')
print 'Hi, %s.' % name



friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print "iteration {iteration} is {name}".format(iteration=i, name=name)
    
    
    
parents, babies = (1, 1)
while babies < 100:
    print 'This generation has {0} babies'.format(babies)
    parents, babies = (babies, parents + babies)
    
    
    
def greet(name):
    print 'Hello', name
    
greet('Jack')
greet('Jill')
greet('Bob')




# This program adds up integers in the command line
import sys
try:
    total = sum(int(arg) for arg in sys.argv[1:])
    print 'sum =', total
except ValueError:
    print 'Please supply integer arguments'
    
    
