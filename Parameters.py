class Parameter:
    def __init__(self, name ):
        if type(name)!= str:
            raise TypeError('a parameter was given an invalid name')
        self.name = name
        self.value = None
    def get_name(self):
        return self.name
    # each child class should have its own version of get/ set, someone should add this when they play with the data
    def get_value(self):
        return self.value
    def set_value(self , value):
        self.value = value

class Const(Parameter):
    def __init__(self, name, value):
        Parameter.__init__(self=self, name=name)
        if(type(value) != int and type(value) != float):
            raise TypeError('A parameter called '+self.name+' was given an invalid value of '+value)
        self.value = value
        print('created const '+name+' '+ str(self.value))

class Rand(Parameter):
    def __init__(self, name, min, max):
        Parameter.__init__(self=self, name=name)
        if(type(min) != int and type(min) != float):
            raise TypeError('A parameter called '+self.name+' was given an invalid min of '+min)
        if(type(max) != int and type(max) != float):
            raise TypeError('A parameter called '+self.name+' was given an invalid max of '+max)
        self.min = min
        self.max = max
        print('created rand '+name+' '+str(self.min)+' '+str(self.max))
    def get_min(self):
        return self.min
    def get_max(self):
        return self.max 



class Range(Parameter):
    def __init__(self, name, values):
        Parameter.__init__(self=self, name=name)
        if(type(values) != list):
            raise TypeError('A parameter called '+self.name+' was given an invalid list of values of '+ str(values))
        self.values = values
        print('created range '+name+' '+str(self.values))
    

class Calc(Parameter):
    def __init__(self, name, formula):
        Parameter.__init__(self=self, name=name)
        if(type(formula) != str):
            raise TypeError('A parameter called '+self.name+' was given an invalid list of values of '+ str(formula))
        self.formula = formula
        print('created calc '+name+' '+self.formula)

class Sim(Parameter):
    def __init__(self, name, schematic_var_name):
        Parameter.__init__(self=self, name=name)
        if(type(schematic_var_name) != str):
            raise TypeError('A parameter called '+self.name+' was given an invalid list of values of '+ str(schematic_var_name))
        self.schematic_var_name = schematic_var_name
        print('created sim '+name+' '+self.schematic_var_name)

if __name__ == "__main__":
    print('why is this being run LOL?')