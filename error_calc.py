import numpy as np
'''
This program is a class, physicsRules, for the rules in our physics lab.
Can import physicsRules and use rule 1-4. 
'''
#-------------------------------------------------------------------------

class Rules:
	#Rule 1
	#If Q=c*A -> δQ=|c|*δA
	def rule1(error, c):
		return round(abs(c) * error, 6)

	#Rule 2
	#If Q=c*A^m -> δQ=|c*m*A^(m-1)|*δA
	def rule2(value, error, exponent, c):
		absolute = abs(c * exponent * (value**(exponent-1)))
		dQ = absolute * error
		return round(dQ, 6)

	#Rule 3
	#If Q=A+B or Q=A-B -> δQ=√(δA^2+δB^2+...)
	def rule3(errors: list):
		sqrt_values = []
		for i in range(len(errors)):
			equation = errors[i] ** 2
			sqrt_values.append(equation)

		sqrt_ready = sum(sqrt_values)

		dQ = np.sqrt(sqrt_ready)
		return round(dQ, 6)	

	#Rule 4
	#If Q=cA^m*B^n -> δQ=|Q|√((m*δA/A)^2+(n*δB/B)^2+...)
	def rule4(values: list, errors: list, exponents: list, Q):
		sqrt_values = []
		for i in range(len(values)):
			equation = ((exponents[i] * errors[i]) / values[i]) ** 2
			sqrt_values.append(equation)
	
		sqrt_ready = sum(sqrt_values)
		
		dQ = abs(Q) * np.sqrt(sqrt_ready)
		return round(dQ, 6)

#-------------------------------------------------------------------------

if __name__ == '__main__':

#	!!!  Make sure values, errors, and exponents all have the same  !!!
#	!!!  number of items when working with them.  					!!!

	#Values for rules, e.g. (A, B, C, D)
	values = [(.2639*.0661), (0.271), ((1-.8221))]
	#Errors for rules, e.g. (δA, δB, δC, δD)
	errors = [.0001, .0005, .0013]
	#Exponents for rules, e.g. (m, n, o, p)
	exponents = [-1, .5, .5]
	#Constant for the rules
	c = 1
	#Value of the sought error
	Q = (2 * 9.8)**0.5

#Testing------------------------------------------------------------------

	#prints all the rules
	print(Rules.rule1(.1, 1))
	print(Rules.rule2(1, .1, 1, 1))
	print(Rules.rule3(errors))
	print(Rules.rule4(values, errors, exponents, Q))

	print()#--------------------------------------------------------------

#Lab Part 2---------------------------------------------------------------

	x = [1.1, 1.3, 1.4, 0.90, 0.95, 1.05]

	dx = np.std(x) / len(x)
	x_avg = np.average(x)

	print(dx)
	print(x_avg)

