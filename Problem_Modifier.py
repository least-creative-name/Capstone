import Parameters
import Displays


class Container:
    def __init__(self,problems,formatter):
        self.problems = problems
        self.formatter = formatter
        self.num_variants = None
    def get_problems(self):
        return self.problems
    def set_problems(self,problems):
        self.problems = problems
    def set_num_variants(self, value):
        self.num_variants = value
    def get_num_variants(self):
        return self.num_variants



class Problem_Specs:
    def __init__(self):
        # dictionary of every parameter, found by using its name
        self.parameters = {}

        # list of every parameter organized by their type, this data should match the info in the dictionary above
        self.consts = []
        self.rands = []
        self.ranges = []
        self.calcs = []
        self.sims = []

        # this dictionary maps variable names in this program to points in the schematic
        self.sim_mappings = {}

        # this keeps track of everything that will need to be displayed in the order they should be displayed (for problems)
        self.problem_displays = []
        # this keeps track of everything that will need to be displayed in the order they should be displayed (for solutions)
        self.solution_displays = []

        self.display_solution_parameters = False

        # this is for the original file path for the schematic
        self.circuit_schematic_path = None
        # might consider creating additioanl circuit schematic display objects, 1 for each variant since each display holds 1 path to a modified/annotated ASC file
        self.circuit_schematic_display = None
        # all modified/annotated netlists for each variant
        self.circuit_schematics = None

        self.title = None
        self.marks = None

    def add_parameter(self, param):
        if(isinstance(param, Parameters.Const)):
            self.consts.append(param)
        elif(isinstance(param, Parameters.Rand)):
            self.rands.append(param)
        elif(isinstance(param, Parameters.Range)):
            self.ranges.append(param)
        elif(isinstance(param, Parameters.Calc)):
            self.calcs.append(param)
        elif(isinstance(param, Parameters.Sim)):
            self.sims.append(param)
        else:
            raise TypeError('parameter was trying to be added that isnt supported')
        if(self.parameters.get(param.get_name()) != None):
            raise ValueError('multiple parameters were being created that had the same name')
        self.parameters[param.get_name()] =  param
    
    def to_sim(self, var_name, schematic_name):
        if(type(var_name) != str or type(schematic_name) != str):
            raise TypeError('the to sim command was handled with things that werent strings')
        self.sim_mappings[var_name] = schematic_name

    def add_display_to_problem(self, display):
        if not (isinstance(display, Displays.Display)):
            raise TypeError('tried adding display to the problem that wasnt of type display')
        self.problem_displays.append(display)
    
    def add_soldisplay_to_problem(self, display):
        if not (isinstance(display, Displays.Display)):
            raise TypeError('tried adding display to the problem that wasnt of type display')
        self.solution_displays.append(display)
    
    def show_solution_all_params(self, show):
        if (type(show) != bool):
            raise TypeError('parameter for show all param soltuions was not bool')
        self.display_solution_parameters = show

    def set_title(self, title):
        if(type(title) != str):
            raise TypeError('the title of the problem is not a string')
        self.title = title
        print('using title '+title)

    def set_marks(self, marks):
        if(type(marks) != int):
            raise TypeError('the marks assiocated with this problem is not an integer')
        self.marks = marks
        print('using mnarks '+str(marks))

    def set_circuit_schematic_path_and_display(self, file_path, display):
        if(type(file_path) != str):
            raise TypeError('the schematic path assiocated with this problem is not a string')
        if (self.circuit_schematic_path is not None):
            raise ValueError('multiple schematics have been provided for the same problem, this is not allowed')
        if not (isinstance(display, Displays.Display)):
            raise TypeError('tried adding display to the problem that wasnt of type display')
        self.circuit_schematic_path = file_path
        self.circuit_schematic_display = display


if __name__ == "__main__":
    print('why is this being run?')