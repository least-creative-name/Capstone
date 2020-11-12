import Parameters
import Displays

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

if __name__ == "__main__":
    print('why is this being run?')
    # problem1 = Problem_Specs()
    # temp1 = Parameters.Const('bob', 5)
    # temp2 = Parameters.Rand('bob1', 0, 5)
    # temp3 = Parameters.Range('bob2', [1, 2, 3, 4])
    # temp4 = Parameters.Calc('bob3', '234 = 234234 =234')
    # temp5 = Parameters.Sim('bob4', 'apple')
    # problem1.add_parameter(temp1)
    # problem1.add_parameter(temp2)
    # problem1.add_parameter(temp3)
    # problem1.add_parameter(temp4)
    # problem1.add_parameter(temp5)