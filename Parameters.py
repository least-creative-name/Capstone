class Parameter:
    def __init__(self, name):
        if type(name)!= str:
            raise TypeError('a parameter was given an invalid name')
        self.name = name

class Const(Parameter):
    def __init__(self, name, value):
        Parameter.__init__(self=self, name=name)
        if(type(value) != int and type(value) != float):
            raise TypeError('A parameter called '+self.name+' was given an invalid value of '+value)
        self.value = value

class Rand(Parameter):
    def __init__(self, name, min, max):
        Parameter.__init__(self=self, name=name)
        if(type(min) != int and type(min) != float):
            raise TypeError('A parameter called '+self.name+' was given an invalid min of '+min)
        if(type(max) != int and type(max) != float):
            raise TypeError('A parameter called '+self.name+' was given an invalid max of '+max)
        self.min = min
        self.max = max

class Range(Parameter):
    def __init__(self, name, values):
        Parameter.__init__(self=self, name=name)
        if(type(values) != list):
            raise TypeError('A parameter called '+self.name+' was given an invalid list of values of '+ str(values))
        self.values = values

class Calc(Parameter):
    def __init__(self, name, formula):
        Parameter.__init__(self=self, name=name)
        if(type(formula) != str):
            raise TypeError('A parameter called '+self.name+' was given an invalid list of values of '+ str(formula))
        self.formula = formula

class Sim(Parameter):
    def __init__(self, name, schematic_name):
        Parameter.__init__(self=self, name=name)
        if(type(schematic_name) != str):
            raise TypeError('A parameter called '+self.name+' was given an invalid list of values of '+ str(schematic_name))
        self.schematic_name = schematic_name

def main():
    # testing = Parameter('bob')
    testing = Const('bob', 5)
    testing = Rand('bob', 0, 10)
    testing = Range('bob', [1, 2, 3, 4])
    testing = Calc('bob', '43 = 234234 + 3123')
    testing = Sim('bob', 'SHJfjsikjf')

if __name__ == "__main__":
    main()