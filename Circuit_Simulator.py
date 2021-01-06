import Parameters
import Displays
import Problem_Modifier
import PySpice
import numpy as np
from PySpice.Spice.Parser import SpiceParser
from PySpice.Probe.Plot import plot
import matplotlib.pyplot as plt
from inspect import getmembers, isfunction


class spice_schematic:
    def __init__(self,path):
        self.imported_file_parser = SpiceParser(path=path)
        self.circuit = self.imported_file_parser.build_circuit()
        # pyspice_parser = PySpice.Spice.Parser.SpiceParser(path = path)
        # print('starting the printing/.///.....................................')
        print(self.imported_file_parser.circuit)
        print(self.imported_file_parser.subcircuits)
        print(self.imported_file_parser.models)

        self.circuit_elems = list(self.circuit.elements)
        print(self.circuit_elems)
        print(self.circuit_elems[0])
        print(self.circuit.element_names)
        print(self.circuit.has_ground_node)
        print(self.circuit.elements)
        self.nodes = list(self.circuit.nodes)
        self.nodes_names = list(self.circuit.node_names)
        print(self.nodes)
        print(self.nodes_names)
        print(self.circuit.R1.minus)
        print(self.circuit.R1.plus)
        # print('finished the printing //.//.....................................')
        # print (analysis)
        print('finished the printing //.//.....................................')
    # def _parse_path(self, path):
    #     print(PySpice.__version__)
    #     print(dir(PySpice))
    #     # print(getmembers(PySpice, isfunction))
    #     imported_file_parser = SpiceParser(path=path)
    #     circuit = imported_file_parser.build_circuit()
    #     # pyspice_parser = PySpice.Spice.Parser.SpiceParser(path = path)
    #     # print('starting the printing/.///.....................................')
    #     print(imported_file_parser.circuit)
    #     print(imported_file_parser.subcircuits)
    #     print(imported_file_parser.models)

    #     circuit_elems = list(circuit.elements)
    #     print(circuit_elems)
    #     print(circuit_elems[0])
    #     print(circuit.element_names)
    #     print(circuit.has_ground_node)
    #     print(circuit.elements)
    #     nodes = list(circuit.nodes)
    #     nodes_names = list(circuit.node_names)
    #     print(nodes)
    #     print(nodes_names)
    #     print(circuit.R1.minus)
    #     print(circuit.R1.plus)
    #     # print('finished the printing //.//.....................................')
    #     print (analysis)
    #     print('finished the printing //.//.....................................')
    def plot_graph(self,title,x_label,y_label,amplitude,analyse_value,analyse_value_2 = None):
        '''
        Function to plot graphs 
        '''
        figure, ax = plt.subplots(figsize=(20, 10))
        ax.set_title(title)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.grid()
        if analyse_value_2 != None:
            ax.plot(analyse_value,analyse_value_2)
        else:
            ax.plot(analyse_value)
        ax.legend(('input', 'output'), loc=(.05,.1))
        ax.legend(('input', 'output'), loc=(.05,.1))
        ax.set_ylim(float(-amplitude*1.1), float(amplitude*1.1))
        plt.tight_layout()
        plt.show()



   
    def simulate_mode_dc_op(self):
        '''
        Computes the DC operating point treating 
        capacitors as open cicuits and inductors
        as shorts
        '''
        simulator = self.circuit.simulator(temperature=25, nominal_temperature=25)
        analysis = simulator.operating_point()
        for node in analysis.nodes.values(): 
            print('Node {}: {:4.3f} V'.format(str(node), float(node)))
        for node in analysis.branches.values(): 
            print('Node {}: {:5.3f} A'.format(str(node), float(node))) 
  
    def simulate_mode_transient(self):
        '''
        Performs Non Linear time domain simulations
        '''
        amplitude = 4
        simulator = self.circuit.simulator(temperature=25, nominal_temperature=25)
        analysis = simulator.transient(step_time=0.0000001,end_time=0.02)
        self.plot_graph('Voltage  vs Time','Time [s]','Voltage [V]',amplitude,analysis.nodes['n001'])

    def simulate_mode_dc_transfer(self):
        '''
        Find DC small signal transfer function
        '''
        simulator = self.circuit.simulator(temperature=25, nominal_temperature=25)
        analysis = simulator.transfer_function(outvar='v(1,2)',insrc='v1')
        for node in analysis.nodes.values(): 
            print('Node {}: {:4.3f} '.format(str(node), float(node)))

    def simulate_mode_dc_sweep(self):
        '''
        Computes the DC operating point of a circuit 
        while stepping independent sources and treating 
        capacitances as open circuits and inductances 
        as short circuits.
        Note: Only linear sweep is supported for now 
        '''
        amplitude = 5
        simulator = self.circuit.simulator(temperature=25, nominal_temperature=25)
        analysis = simulator.dc(v1=slice(0, 5, .01))
        self.plot_graph('Voltage (n1) vs Voltage(n2)','Voltage[Vn2]','Voltage [Vn1]',amplitude,analysis.nodes['2'],analysis.nodes['1'])
        
    def simulate_mode_ac_analysis(self):
        '''
        Computes the small signal AC behaviour of the 
        circuit linearied about its DC operating point 
        '''
        amplitude_imag = -1000000e-8 
        amplitude_real = 2
        simulator = self.circuit.simulator(temperature=25, nominal_temperature=25)
        analysis = simulator.ac(start_frequency=1000, stop_frequency=1e8, number_of_points=20,  variation='dec')
        self.plot_graph('Frequency Response Bode plot','dB','Frequency',amplitude_real,np.real(analysis.nodes['n002']))
        self.plot_graph('Frequency Response Bode plot','dB','Frequency',amplitude_imag,np.imag(analysis.nodes['n002']))



    
    



def parse_schematic_paths_for_problems(container):
    netlists = []
    for problem in container.get_problems():
        netlists.append(spice_schematic(problem.circuit_schematic_path))
    for sim_netlist in netlists:
        sim_netlist.simulate_mode_transient()
    

    

if __name__ == "__main__":
    print('why is this being run?')