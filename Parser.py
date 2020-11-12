import argparse
import Parameters
import Displays
import Problem_Modifier

def isfloat(x):
    try:
        a = float(x)
    except (TypeError, ValueError):
        return False
    else:
        return True

def isint(x):
    try:
        a = float(x)
        b = int(a)
    except (TypeError, ValueError):
        return False
    else:
        return a == b

def convert_num(value):
    if(isfloat(value)):
        return float(value)
    if(isint(value)):
        return int(value)

def get_args():
    parser = argparse.ArgumentParser(description='idk lets parse some args')
    parser.add_argument("-input",help="insert input txt file (mandatory)" , dest="input", type=str, required=True)

    args = parser.parse_args()
    return args

def parse_variable_line(problem, line):
    if(len(line[1:]) < 3):
        raise ValueError('give a proper variable command pls')
    var_name = line[1]
    var_type = line[2]
    values = line[3:]
    param = None
    if(var_type == 'CONST'):
        values = convert_num(values[0])
        param = Parameters.Const(var_name, values)
    elif(var_type == 'RAND'):
        minimum = convert_num(values[0])
        maximum = convert_num(values[1])
        param = Parameters.Rand(var_name, minimum, maximum)
    elif(var_type == 'RANGE'):
        for val in values:
            val = convert_num(val)
        param = Parameters.Range(var_name, values)
    elif(var_type == 'CALC'):
        values = values[0]
        param = Parameters.Calc(var_name, values)
    elif(var_type == 'SIM'):
        values = values[0]
        param = Parameters.Sim(var_name, values)
    else:
        raise ValueError('var command had wrong type')
    problem.add_parameter(param)


def parse_args_and_file():
    args = get_args()
    print(args.input)
    problems = []
    with open(args.input, "r") as file:
        problem= None
        for line in file.readlines():
            if (line == '=====\n' ):
                print('created problem')
                if(problem is not None):
                    problems.append(problem)
                problem = Problem_Modifier.Problem_Specs()
                continue
            data = line.split()
            if(data[0] == 'VAR'):
                parse_variable_line(problem, data)
            elif (data[0] == 'TOSIM'):
                if(len(data[1:])< 2):
                    raise ValueError('TOSIM had too few arguments')
                problem.to_sim(data[1], data[2])
            elif (data[0] == 'IMAGE'):
                file_path = data[1]
                display = Displays.Image(file_path)
            elif (data[0] == 'SCHEMATIC'):
                file_path = data[1]
                show = True
                if(len(data[1:]) == 2):
                    show = bool(data[2])
                display = Displays.Schematic(file_path, show)
                problem.add_soldisplay_to_problem(display)
            elif (data[0] == 'TEXT'):
                text = ' '.join(data[1:])
                display = Displays.Text(text)
                problem.add_display_to_problem(display)
            elif (data[0] == 'SOLTEXT'):
                text = ' '.join(data[1:])
                display = Displays.Text(text)
                problem.add_soldisplay_to_problem(display)
            elif (data[0] == 'SOLDISPLAY'):
                problem.show_solution_all_params(True)
            elif (data[0] == 'TITLE'):
                title = data[1]
                problem.set_title(title)
            elif (data[0] == 'MARKS'):
                marks = int(data[1])
                problem.set_marks(marks)

    return problems

if __name__ == "__main__":
    parse_args_and_file()