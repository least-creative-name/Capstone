import argparse
import Parameters
import Displays
import Problem_Modifier
import Formatter
import Randomizer
import Solver
import Text_Formatter
import Parser
import Output_Converter

if __name__ == "__main__":
    Contain = Parser.parse_args_and_file()
    Parser.extend_const(Contain.get_problems(), Contain.get_num_variants())
    Randomizer.randomise_rand_and_range(Contain.get_problems() , Contain.get_num_variants())
    Solver.solve_all(Contain.get_problems(), Contain.get_num_variants())
    Text_Formatter.format_text(Contain.get_problems(), Contain.get_num_variants())
    Output_Converter.process_to_pdf(Contain.get_num_variants())

    