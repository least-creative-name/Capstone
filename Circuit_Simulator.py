import Parameters
import Displays
import Problem_Modifier
import PySpice
from PySpice.Spice.Parser import SpiceParser
from inspect import getmembers, isfunction


class spice_schematic:
    def __init__(self,path):
        self._parse_path(path)
    def _parse_path(self, path):
        print(PySpice.__version__)
        print(dir(PySpice))
        # print(getmembers(PySpice, isfunction))
        imported_file_parser = SpiceParser(path=path)
        constructed_circuit = imported_file_parser.build_circuit()
        # pyspice_parser = PySpice.Spice.Parser.SpiceParser(path = path)
        print('starting the printing/.///.....................................')
        print(imported_file_parser.circuit)
        print(imported_file_parser.subcircuits)
        print(imported_file_parser.models)

        circuit_elems = list(constructed_circuit.elements)
        print(circuit_elems)
        print(circuit_elems[0])
        print(constructed_circuit.element_names)
        print(constructed_circuit.has_ground_node)
        print(constructed_circuit.elements)
        nodes = list(constructed_circuit.nodes)
        nodes_names = list(constructed_circuit.node_names)
        print(nodes)
        print(nodes_names)
        print(constructed_circuit.R1.minus)
        print(constructed_circuit.R1.plus)
        print('finished the printing //.//.....................................')

def parse_schematic_paths_for_problems(container):
    for problem in container.get_problems():
        netlist = spice_schematic(problem.circuit_schematic_path)
if __name__ == "__main__":
    print('why is this being run?')