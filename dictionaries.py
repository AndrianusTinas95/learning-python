phonebook = {}

phonebook['cai'] = 86776
phonebook['coi'] = 75456

#print(phonebook)

phonebook= { 'cai':7447, 'coi':5678}

#for name, number in phonebook.items():
#	print('Phone number of %s is %d ' % (name,number))

#del phonebook['coi']
#phonebook.pop('coi')

#print(phonebook)

phonebook['tes']=673827876
phonebook.pop('coi')

#if 'tes' in phonebook :
#	print('tes in phone book')

#if 'coi' not in phonebook :
#	print('coi not in phone book')
search = 7447
 
for name , number in phonebook.items():
	if number is search :
		print('number 7447 in phone book')
		break
else :
	print('number is not found')

	
