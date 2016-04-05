''' First attempt at a course plan making function.'''
import random
import copy
'''TODO: create Course class w/ is_requirement, suggested_semester, connect to algorithm'''
gottatake = ['PaM', 'LinI', 'PoE', 'Bio', 'Chem', 'Robo', 'Mechanics', 'Art']
classorder = range(len(gottatake))
difficulties = {'PaM':1, 'LinI':2, 'PoE':5, 'Bio':4, 'Chem':3, 'Robo':2, 'Mechanics':4, 'Art':3}

sem1 = range(4)
sem2 = range(4,8)

s1diff = 0
s2diff = 0
mindiff = 50
myOrder = None

for i in range(10):
	random.shuffle(classorder)
	for slot in sem1:
		s1diff += difficulties[gottatake[classorder[slot]]]
		s2diff += difficulties[gottatake[classorder[slot + 4]]]
	if (s1diff < mindiff and s2diff < mindiff):
		mindiff = max([s1diff,s2diff])
		myOrder = copy.copy(classorder)
	s1diff = 0
	s2diff = 0

print 'Semester 1: '
for i in range(4):
	print gottatake[myOrder[i]],
print '\nSemester 2: '
for i in range(4,8):
	print gottatake[myOrder[i]],