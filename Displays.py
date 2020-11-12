class Display:
    # who ever makes output formmatter, they should have overwritten this function
    def get_output():
        raise TypeError('this function should have been overwritten')
class Image(Display):
    def __init__(self, image_path):
        self.img_path = image_path
class Schematic(Display):
    def __init__(self, schematic_path):
        self.schematic_path = schematic_path
class Text(Display):
    def __init__(self, text):
        self.text = text
class Title(Display):
    def __init__(self, title):
        self.title = title