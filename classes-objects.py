class rumah : 
	name ='cai'
			       
	def dapur(self):
		print('tes function in class ')

home = rumah()
house = rumah()
#print('ini rumah ' + home.name)

#home.dapur()

house.name= 'coi'

#print('ini rumah ' +  house.name)

class Vehicle :
	name = ''
	kind = 'car'
	color= ''
	value=100.00

	def description(self):
		desc_str = '%s is a %s %s worth $%.2f .' %(self.name,self.color, self.kind ,self.value)
		return desc_str

car1 = Vehicle()
car2 = Vehicle()

car1.name='truck'
car1.color='black'

car2.name='peckup'
car2.color='yellow'
car2.value=150

print(car1.description())
print(car2.description())
