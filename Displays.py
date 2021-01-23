import os 
class Display:
    # who ever makes output formmatter, they should have overwritten this function
    def get_output():
        raise TypeError('this function should have been overwritten')
class Image(Display):
    def __init__(self, image_path):
        self.img_path = image_path
        print('added image with path '+image_path)
class Schematic(Display):
    def __init__(self, schematic_path, show=True):
        if(type(schematic_path) != str):
            raise TypeError('schematic path should be a string')
        if(type(show) != bool):
            raise TypeError('show should be a bool')
        self.schematic_path = schematic_path
        self.show = show
        

class Schematic_Graphical(Display):
    def __init__(self, schematic_path, show=True):
        if(type(schematic_path) != str):
            raise TypeError('schematic path should be a string')
        if(type(show) != bool):
            raise TypeError('show should be a bool')
        self.schematic_path = schematic_path
        self.show = show
        self.random_flag = 0 
        if(self.random_flag == 0):
          os.system("icemaker -export ex1.svg " +".\\"+self.schematic_path)  #     os.system("icemaker -export ex1.svg .\sample_asc_files\simple_R_series.asc ")  
          os.system("inkscape --export-type=png ex1.svg ")
          self.schematic_image_path = "./ex1.png"
          print('added schematic with path '+self.schematic_path+ ' '+str(self.show))       

class Text(Display):
    def __init__(self, text):
        if(type(text) != str):
            raise TypeError('text should be a string')
        self.text = text
        print('created text with value '+text)