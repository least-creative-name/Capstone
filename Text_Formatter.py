import Displays
import Problem_Modifier
import Parameters
import re
import os

def format_text(problems, num_variants):

	#prep the output folder
	if not os.path.exists("tex"):
		os.mkdir("tex")

	print("Beginning TeX output formatting");
	for i in range(num_variants):
		prob = open("tex/problem"+str(i)+".tex","w")
		soln = open("tex/solution"+str(i)+".tex","w")


		#set up the preamble
		prob.write(r'\documentclass[12pt, a4paper]{article}'+ "\n")
		prob.write(r'\usepackage[utf8]{inputenc}'+ "\n")
		prob.write(r'\usepackage{graphicx}'+ "\n")
		prob.write(r'\usepackage{parskip}'+ "\n")
		prob.write(r'\usepackage[margin=1in]{geometry}'+"\n")
		prob.write(r'\graphicspath{ {./}{../}{../sample_svg_files/} }'+ "\n") #TODO, proper image path detection
		prob.write(r'\begin{document}'+ "\n")

		soln.write(r'\documentclass[12pt, a4paper]{article}'+ "\n")
		soln.write(r'\usepackage[utf8]{inputenc}'+ "\n")
		soln.write(r'\usepackage{graphicx}'+ "\n")
		soln.write(r'\usepackage{parskip}'+ "\n")
		soln.write(r'\usepackage[margin=1in]{geometry}'+"\n")
		soln.write(r'\graphicspath{ {./}{../}{../sample_svg_files/} }'+ "\n")
		soln.write(r'\begin{document}'+ "\n")

		for problem in problems:
			#make each problem start a new page
			prob.write(r"\newpage"+"\n")
			soln.write(r"\newpage"+"\n")

			#use section formatting for problem title
			if problem.title:
				prob.write(r"\section*{"+problem.title + "}\n")
				soln.write(r"\section*{"+problem.title + "}\n")
			if problem.marks:
				prob.write("\nMarks: "+str(problem.marks) + "\n\n")
				soln.write("\nMarks: "+str(problem.marks) + "\n\n")

			for item in problem.problem_displays:
				if isinstance(item,Displays.Text):
					formStr = item.text
					#extract each element encompassed in single square brackets
					paramList = set(re.findall("\[([^\[\]]+)\]", formStr))
					#fill in the numbers
					for param in paramList:
						formStr =  formStr.replace("["+param+"]",str(problem.parameters[param].value[i]))
					prob.write(formStr + "\n\n") #double newline is a paragraph break, single does nothing
				elif isinstance(item,Displays.Image):
					prob.write(r"\includegraphics[width=1\textwidth]{"+item.img_path+"}\n\n")
				elif isinstance(item,Displays.Schematic_Graphical):
					prob.write(r"\includegraphics[width=1\textwidth]{"+os.path.splitext(os.path.basename(item.schematic_image_path))[0]+"}\n\n")
			for item in problem.solution_displays:
				if isinstance(item,Displays.Text):
					formStr = item.text
					#extract each element encompassed in single square brackets
					paramList = set(re.findall("\[([^\[\]]+)\]", formStr))
					#fill in the numbers
					for param in paramList:
						formStr =  formStr.replace("["+param+"]",str(problem.parameters[param].value[i]))
					soln.write(formStr + "\n\n")
				elif isinstance(item,Displays.Image):
					soln.write(r"\includegraphics[width=1\textwidth]{"+item.img_path+"}\n\n")
				elif isinstance(item,Displays.Schematic_Graphical):
					soln.write(r"\includegraphics[width=1\textwidth]{"+os.path.splitext(os.path.basename(item.schematic_image_path))[0]+"}\n\n")
			if problem.display_solution_parameters:
				soln.write("\nDump of all parameters:\n\n")
				for key in problem.parameters.keys():
					# format as "verbatim" mostly because underscores are macro for subscript (consider modifying to escape via \_ instead)
					soln.write(r"\verb|"+problem.parameters[key].get_name() +" : "+str(problem.parameters[key].value[i]) + "|\n\n")
			prob.write("\n")
			soln.write("\n")

		prob.write(r"\end{document}")
		soln.write(r"\end{document}")
		prob.close()
		soln.close()
		print("Problem formatting complete")
