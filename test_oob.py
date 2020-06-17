class A:
	count=0

	def __init__(self, a):
		self.name = a
		A.inc_count()

	@staticmethod
	def inc_count():
		A.count += 1

#A.inc_count = staticmethod(A.inc_count)

a=A('a')
print a.name
print A.count

b=A('b')
print b.name
print A.count