class State:

	def __init__(self, name=''):
		self.name = name

	def run(self):
		assert 0

	def next(self, input):
		assert 0

class StateMachine:
	def __init__(self, q0, F=[]):
		self.currentState = q0

		self.acceptableState = F

	def runAll(self, inputs="", reset=False):
		if reset:
			self.__init__(S1(), F=[S1()])
		F = list(map(lambda x: x.name,self.acceptableState))
		print('------ EVEN NUMBER OF ONES STATE MACHINE ------')
		print('Q = ["S1","S2"]')
		print('q0 = ' + self.currentState.name)
		print('E = ["0","1"]')
		print('F = ' + str(F) )
		print('SIGMA = [ "S(S1, 0) = 0", "S(S1, 1)= S2", "S(S2, 0)= S2", "S(S2, 1)= S1" ')
		print('INPUTS = ' + inputs)
		print('ORDER OF STATES:')
		for i, char in enumerate(inputs):
			self.currentState.run()
			self.currentState = self.currentState.next(char)
		print("ACCEPTABLE: " + str(self.currentState.name in F))
		print('------ STATEMACHINE DONE ------\n')

# STATES
class S1(State):
	def __init__(self):
		self.name = 'S1'

	def run(self):
		print(self.name)

	def next(self, input):
		if input=='0':
			return S1()
		elif input=='1':
			return S2()
		else:
			raise TypeError('Input must be = {"0","1"}')

class S2(State):
	def __init__(self):
		self.name = 'S2'

	def run(self):
		print(self.name)

	def next(self, input):
		if input=='1':
			return S1()
		elif input=='0':
			return S2()
		else:
			raise TypeError('Input must be = {"0","1"}')

x = StateMachine(q0=S1(), F=[S1()])
x.runAll(inputs='0', reset=True)
x.runAll(inputs='011', reset=True)
x.runAll(inputs='01110', reset=True)
x.runAll(inputs='0100001000', reset=True)





