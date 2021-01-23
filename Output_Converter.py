# for converting .tex files to pdf files
import os

def process_to_pdf(num_variants):
    probpath = "tex/problem"
    solpath = "tex/solution"
    outfolder = "output"

    print("Typesetting TeX files")

    #prep the output folder
    if not os.path.exists(outfolder):
        os.mkdir(outfolder)

    for i in range(num_variants):
        print("pdflatex -interaction -nonstopmode -output-directory "+outfolder+" "+probpath+str(i)+".tex")
        os.system("pdflatex -interaction -nonstopmode -output-directory "+outfolder+" "+probpath+str(i)+".tex")
        os.system("pdflatex -interaction -nonstopmode -output-directory "+outfolder+" "+solpath+str(i)+".tex")

    print("Done!")
