def cai():
	print('this is cai function')

#cai()

def sum(a,b):
        return a + b

#print(sum(2,3))

def nameAge(name,age):
	print('your name is %s and you are also %d years old.' %(name,age))

#nameAge('cai',23)

data = [
		{'name': 'cai', 'age':23},
		{'name': 'uul', 'age':27},
		{'name': 'ikwan', 'age':23},
	]

for v in data :
	nameAge(v['name'],v['age'])

