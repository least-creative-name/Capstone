import re
import math
import regex

def calc_problem(calc, problem, stack, num_variants):
	result = []
	formStr = calc.formula
	print("Starting: "+ calc.name + " = " + formStr)

	#extract each element encompassed in single square brackets
	params = set(re.findall("\[([^\[\]]+)\]", formStr))

	#cycle check
	if any(item in stack for item in params):
		raise CycleError("Detected cycle when solving stack: "+ ", ".join(stack))

	#parameters exist check
	if not all(item in problem.parameters for item in params):
		raise ParamError("Invalid parameter name in formula "+calc.formula)

	#any additonal formatting tweaks to convert generic text to python styling
	formStr = formStr.replace("^","**") #allow exponents using ^

	#use log as natural logarithm (math.log())
	m = regex.search("(?<!math\.)log(\((?:[^)(]+|(?1))*+\))",formStr)
	while(m != None):
		formStr = formStr.replace(m[0],"math.log"+m[1])
		m = regex.search("(?<!math\.)log(\((?:[^)(]+|(?1))*+\))",formStr)


	for i in range(num_variants):
		variantStr = formStr
		for param in params:
			if problem.parameters[param].value == None:
				#recursively compute dependent formula parameters
				calc_problem(problem.parameters[param],problem,stack+[param], num_variants)
			#substitute parameters for values in expression
			variantStr = variantStr.replace("["+param+"]",str(problem.parameters[param].value[i]))
		#use eval to process equation
		result.append(eval(variantStr))
		#print(variantStr)
		#print(result[i])


	calc.set_value(result)
	print("Solved: " + calc.name + " = " + formStr)
	return result

def solve_all(problems, num_variants):
	for problem in problems:
		print("solving a problem")
		for calc in problem.calcs:
			#run all formulae unless they got processed in the recursive step
			if(calc.value==None):
				calc_problem(calc, problem, [calc.get_name()],num_variants)

	return problems


if __name__ == "__main__":
	print("don't run me directly")
