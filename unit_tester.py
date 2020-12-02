import argparse
import Parameters
import Displays
import Problem_Modifier
import Formatter
import Randomizer
import Solver
import Text_Formatter
import Parser
import math


class Tester:
    def __init__(self):
        self.container = None
    
    def setup_m1_test(self):
        self.container = Parser.parse_args_and_file('./unit_tests.txt', 1)
    
    def run_case(self):
        Parser.extend_const(self.container.get_problems(), self.container.get_num_variants())
        Randomizer.randomise_rand_and_range(self.container.get_problems() , self.container.get_num_variants())
        Solver.solve_all(self.container.get_problems(), self.container.get_num_variants())
        # Text_Formatter.format_text(self.container.get_problems(), self.container.get_num_variants())
    
    def verify_m1_parser(self):
        subtraction_exists = False
        addition_exists = False
        for problem in self.container.get_problems():
            if(problem.title == 'Subtraction'):
                subtraction_exists = True
                assert(problem.parameters['R1'].get_value()[0] == 373)
                assert(problem.parameters['R2'].min == 1 and problem.parameters['R2'].max == 10)
                assert(problem.parameters['R3'].values == [1, 2, 3, 4])
                assert(problem.marks == 10)
                assert(problem.parameters['hot_pancakes'].formula == '[R1]-[R2]-[R3]')
                assert(problem.sim_mappings['R1'] == 'R_1')
            elif (problem.title == 'Addition'):
                addition_exists = True
                assert(problem.parameters['R1'].get_value()[0] == 373)
                assert(problem.parameters['R2'].min == 1 and problem.parameters['R2'].max == 10)
                assert(problem.parameters['R3'].values == [1, 2, 3, 5])
                assert(problem.parameters['french_toast'].formula == '[hot_pancakes]+1')
                assert(problem.parameters['hot_pancakes'].formula == '[R1]+[R2]+[R3]')
        assert(subtraction_exists)
        assert(addition_exists)

    def verify_m1_randomizer(self):
        for problem in self.container.get_problems():
            if(problem.title == 'Subtraction'):
                assert(problem.parameters['R1'].get_value()[0] == 373)
                assert(problem.parameters['R2'].get_value()[0] >= 1 and problem.parameters['R2'].get_value()[0] <= 10)
                assert(problem.parameters['R3'].get_value()[0] in [1, 2, 3, 4])
            elif(problem.title == 'Addition'):
                assert(problem.parameters['R1'].get_value()[0] == 373)
                assert(problem.parameters['R2'].get_value()[0] >= 1 and problem.parameters['R2'].get_value()[0] <= 10)
                assert(problem.parameters['R3'].get_value()[0] in [1, 2, 3, 5])
    
    def verify_m1_solver(self):
        for problem in self.container.get_problems():
            if(problem.title == 'Subtraction'):
                assert(problem.parameters['hot_pancakes'].get_value()[0] == (problem.parameters['R1'].get_value()[0] - problem.parameters['R2'].get_value()[0] - problem.parameters['R3'].get_value()[0]))
            elif(problem.title == 'Addition'):
                assert(problem.parameters['hot_pancakes'].get_value()[0] == (problem.parameters['R1'].get_value()[0] + problem.parameters['R2'].get_value()[0] + problem.parameters['R3'].get_value()[0]))
                assert(problem.parameters['french_toast'].get_value()[0] == (problem.parameters['hot_pancakes'].get_value()[0] +1))
        
    def verify_m1_solver_complex(self):
        problem = Problem_Modifier.Problem_Specs()
        A = Parameters.Const('A', 4)
        B = Parameters.Const('B', 7)
        C = Parameters.Const('C', 3)
        D = Parameters.Const('D', 2)
        E = Parameters.Calc('E', '((log([A])*[B])^[C])^0.5\n')
        problem.add_parameter(A)
        problem.add_parameter(B)
        problem.add_parameter(C)
        problem.add_parameter(D)
        problem.add_parameter(E)
        problems = [ problem ]

        Parser.extend_const(problems, 1)
        Randomizer.randomise_rand_and_range(problems , 1)
        Solver.solve_all(problems, 1)
        target_value = ((math.log(A.get_value()[0])*B.get_value()[0])**C.get_value()[0])**0.5
        assert(problem.parameters['E'].get_value()[0] == target_value)

    def verify_m1_results(self):
        print('###############################################################################')
        print('Starting Milestone 1 Unit Tests')
        print('###############################################################################')
        print('Starting parser test')
        self.verify_m1_parser()
        print("Result: Passed")
        print('...............................................................................')
        print('Starting randomizer test')
        self.verify_m1_randomizer()
        print("Result: Passed")
        print('...............................................................................')
        print('Starting solver (simple formula) test')
        self.verify_m1_solver()
        print("Result: Passed")
        print('...............................................................................')
        print('Starting solver (complex formula) test')
        self.verify_m1_solver_complex()
        print("Result: Passed")
        

if __name__ == "__main__":
    tester = Tester()
    tester.setup_m1_test()
    tester.run_case()
    tester.verify_m1_results()