class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def call_name(self):
		return(f"{self.name}, ,your name was called !!!")


p1 = Person("Yadnesh", 21)
p2 = Person("Kirti", 22)

print(p2.call_name())
