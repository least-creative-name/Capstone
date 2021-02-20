import Displays
import Problem_Modifier
import Parameters
import re
import os

def format_text(container, num_variants):

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
		prob.write(r'\usepackage{tabularx, makecell}'+"\n")
		prob.write(r'\usepackage{fancyhdr}'+"\n")
		prob.write(r'\graphicspath{ {./}{../}{../sample_svg_files/} }'+ "\n") #TODO, proper image path detection
		

		soln.write(r'\documentclass[12pt, a4paper]{article}'+ "\n")
		soln.write(r'\usepackage[utf8]{inputenc}'+ "\n")
		soln.write(r'\usepackage{graphicx}'+ "\n")
		soln.write(r'\usepackage{parskip}'+ "\n")
		soln.write(r'\usepackage[margin=1in]{geometry}'+"\n")
		soln.write(r'\usepackage{tabularx, makecell}'+"\n")
		soln.write(r'\usepackage{fancyhdr}'+"\n")
		soln.write(r'\graphicspath{ {./}{../}{../sample_svg_files/} }'+ "\n")
		

		#formatter elements

		#header/footer
		if container.formatter.left_header or container.formatter.left_footer or container.formatter.right_header or container.formatter.right_footer:
			prob.write(r'\pagestyle{fancy}'+"\n")
			soln.write(r'\pagestyle{fancy}'+"\n")
			prob.write(r'\fancyhf{}'+"\n")
			soln.write(r'\fancyhf{}'+"\n")

		if container.formatter.left_header:
			prob.write(r'\lhead{'+ container.formatter.left_header.replace("PAGENUM", '\thepage') +'}'+"\n")
			soln.write(r'\lhead{'+ container.formatter.left_header.replace("PAGENUM", '\thepage') +'}'+"\n")
		if container.formatter.left_footer:
			prob.write(r'\lfoot{'+ container.formatter.left_footer.replace("PAGENUM", '\thepage') +'}'+"\n")
			soln.write(r'\lfoot{'+ container.formatter.left_footer.replace("PAGENUM", '\thepage') +'}'+"\n")
		if container.formatter.right_header:
			prob.write(r'\rhead{'+ container.formatter.right_header.replace("PAGENUM", '\thepage') +'}'+"\n")
			soln.write(r'\rhead{'+ container.formatter.right_header.replace("PAGENUM", '\thepage') +'}'+"\n")
		if container.formatter.right_footer:
			prob.write(r'\rfoot{'+ container.formatter.right_footer.replace("PAGENUM", '\thepage') +'}'+"\n")
			soln.write(r'\rfoot{'+ container.formatter.right_footer.replace("PAGENUM", '\thepage') +'}'+"\n")


		prob.write(r'\begin{document}'+ "\n")
		soln.write(r'\begin{document}'+ "\n")

		#title page elements
		if container.formatter.generate_title_page:
			if container.formatter.title_text:
				prob.write(r'\section*{\centering '+container.formatter.title_text+'}'+"\n")
				soln.write(r'\section*{\centering '+container.formatter.title_text+'}'+"\n")

			#rest of title elements go here

			#name/student number fields (latex doesn't care for newlines, lets make life easier)
			prob.write(r'\bigskip\begin{minipage}{.5\textwidth}\begin{large}Last Name: \hrulefill\\ \\First Name: \hrulefill\\ \\Student \#: \hrulefill\end{large}\end{minipage}'+"\n")
			soln.write(r'\bigskip\begin{minipage}{.5\textwidth}\begin{large}Last Name: \hrulefill\\ \\First Name: \hrulefill\\ \\Student \#: \hrulefill\end{large}\end{minipage}'+"\n")

			#mark total
			prob.write(r'\flushright\begin{minipage}{.5\textwidth}\centering\setcellgapes{4pt}\makegapedcells\begin{tabularx}{0.8\textwidth} { | >{\raggedright\arraybackslash}X | >{\raggedleft\arraybackslash}X | }\hline'+"\n")
			soln.write(r'\flushright\begin{minipage}{.5\textwidth}\centering\setcellgapes{4pt}\makegapedcells\begin{tabularx}{0.8\textwidth} { | >{\raggedright\arraybackslash}X | >{\raggedleft\arraybackslash}X | }\hline'+"\n")

			markSum = 0
			probNum = 1
			for problem in container.get_problems():
				prob.write("Q"+str(probNum)+" & ")
				soln.write("Q"+str(probNum)+" & ")
				probNum+=1

				if problem.marks: 
					markSum += problem.marks
					prob.write("/"+str(problem.marks))
					soln.write("/"+str(problem.marks))

				prob.write(r' \\ \hline'+"\n")
				soln.write(r' \\ \hline'+"\n")

			if markSum > 0:
				prob.write(r'\textbf{Total} & \textbf{/'+str(markSum)+r'} \\ \hline' + "\n")
				soln.write(r'\textbf{Total} & \textbf{/'+str(markSum)+r'} \\ \hline' + "\n")

			prob.write(r'\end{tabularx}\end{minipage}'+"\n")
			soln.write(r'\end{tabularx}\end{minipage}'+"\n")

			#restore the left align
			prob.write(r'\flushleft'+"\n")
			soln.write(r'\flushleft'+"\n")

		for problem in container.get_problems():
			#make each problem start a new page
			prob.write(r"\newpage"+"\n")
			soln.write(r"\newpage"+"\n")

			#use section formatting for problem title
			if problem.title:
				prob.write(r"\section{"+problem.title + "}\n")
				soln.write(r"\section{"+problem.title + "}\n")
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
