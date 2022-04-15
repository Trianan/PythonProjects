
# Boolean values conversion into binary values, represented as ordered pairs:
list_1 = [True, False]
print(list_1)

del list_1[-1]
list_1.append(True)

if list_1[0] and list_1[1] == True:
	print('1,1')
	#Could stop here for basic AND gate.
elif (list_1[0] == True) and (list_1[1] == False):
	print('1,0')
elif (list_1[0] == False) and (list_1[1] == True):
	print('0,1')
	#Stop here for AND/OR gate.
else:
	print('0,0')

print(list_1)


