import Displays
import Problem_Modifier
import Parameters
import re

def format_text(problems, num_variants):
	print("Beginning basic output formatting");
	for i in range(num_variants):
		prob = open("output\problem"+str(i)+".txt","w")
		soln = open("output\solution"+str(i)+".txt","w")
		for problem in problems:
			if problem.title:
				prob.write(problem.title + "\n")
				soln.write(problem.title + "\n")
			if problem.marks:
				prob.write("Marks: "+str(problem.marks) + "\n")
				soln.write("Marks: "+str(problem.marks) + "\n")

			for item in problem.problem_displays:
				if isinstance(item,Displays.Text):
					formStr = item.text
					#extract each element encompassed in single square brackets
					paramList = set(re.findall("\[([^\[\]]+)\]", formStr))
					#fill in the numbers
					for param in paramList:
						formStr =  formStr.replace("["+param+"]",str(problem.parameters[param].value[i]))
					prob.write(formStr + "\n")
					soln.write(formStr + "\n")
			for item in problem.solution_displays:
				if isinstance(item,Displays.Text):
					formStr = item.text
					#extract each element encompassed in single square brackets
					paramList = set(re.findall("\[([^\[\]]+)\]", formStr))
					#fill in the numbers
					for param in paramList:
						formStr =  formStr.replace("["+param+"]",str(problem.parameters[param].value[i]))
					soln.write(formStr + "\n")
			if problem.display_solution_parameters:
				soln.write("\nDump of all parameters:\n")
				for key in problem.parameters.keys():
					soln.write(problem.parameters[key].get_name() +" - "+str(problem.parameters[key].value[i]) + "\n")
			prob.write("\n")
			soln.write("\n")
		prob.close()
		soln.close()
		print("Problem formatting complete")