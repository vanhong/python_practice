# StateMachine/StateMachine.py
# Take a list of Inputs to move from State to
# State using a template methon.

class StateMachine:
	def __init__(self, initailState):
		self.currentState = initailState
		self.currentState.run()
	#Template methon:
	def runAll(self, inputs):
		for i in inputs:
			print i
			self.currentState = self.currentState.next(i)
			self.currentState.run()