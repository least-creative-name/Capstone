import Parameters
import Displays
import Problem_Modifier
import PySpice
import numpy as np
from PySpice.Spice.Parser import SpiceParser
from PySpice.Probe.Plot import plot
import matplotlib.pyplot as plt
from inspect import getmembers, isfunction

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

class spice_schematic:
    def __init__(self,path, problem_specs):
        self.path = path
        self.imported_file_parser = SpiceParser(path=path)
        self.circuit = self.imported_file_parser.build_circuit()
        self.problem_specs = problem_specs
    
    def fetch_sim_type_and_args(self):
        spice_file_lines = open(self.path).readlines()
        if(len(spice_file_lines) < 2):
            raise ValueError("input simulation file contained too few lines")
        for line in spice_file_lines:
            if(line.startswith('.op') or line.startswith('.tran') or line.startswith('.tf') or line.startswith('.dc') or line.startswith('.ac')):
                terms = line.split()
                sim_type = terms.pop(0)
                return sim_type, terms
        raise ValueError("simulation type was not included in simulation file")
    
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

    def simulate_mode_transient(self, args):
        '''
        Performs Non Linear time domain simulations
        '''
        # TODO: add initial conditions in the future, otherwise this may not work as intended
        simulator = self.circuit.simulator(temperature=25, nominal_temperature=25)
        print(type(simulator))
        dic = dict()
        if(len(args)<2):
            raise ValueError("simulation file for transient analysis has too few arguments, atleast needs to have step time and end time")
        dic['step_time'] = float(args[0])
        dic['end_time'] = float(args[1])
        if(len(args)>2):
            if(isfloat(args[2]) or isint(args[2])):
                dic['start_time'] = convert_num(args[2])
            elif(args[2]=='uic'):
                dic['use_initial_condition'] = True
            else:
                raise ValueError("gave faulty parameters for simulation")
        if(len(args)>3):
            if(isfloat(args[3]) or isint(args[3])):
                dic['max_time'] = convert_num(args[3])
            elif(args[3]=='uic' and 'use_initial_condition' not in dic):
                dic['use_initial_condition'] = True
            else:
                raise ValueError("gave faulty parameters for simulation")
        if(len(args)>4):
            if(args[4]=='uic' and 'use_initial_condition' not in dic):
                dic['use_initial_condition'] = True
            else:
                raise ValueError("gave faulty parameters for simulation")
        
        analysis = simulator.transient(**dic)
        probed_values = list(analysis.nodes['n001'])
        for i in range(len(probed_values)):
            probed_values[i] = float(probed_values[i])
        amplitude = max(probed_values)
        self.plot_graph('Voltage  vs Time','Time [s]','Voltage [V]',amplitude,analysis.nodes['n001'])

    def simulate_mode_dc_transfer(self, args):
        '''
        Find DC small signal transfer function
        '''
        if(len(args)<2):
            raise ValueError('gave faulty parameters for simulation')
        simulator = self.circuit.simulator(temperature=25, nominal_temperature=25)
        analysis = simulator.transfer_function(outvar=args[0],insrc=args[1])
        print('printing now')
        for node in analysis.nodes.values(): 
            print('Node {}: {:4.3f} '.format(str(node), float(node)))
        print('done')

    def simulate_mode_dc_sweep(self, args):
        '''
        Computes the DC operating point of a circuit 
        while stepping independent sources and treating 
        capacitances as open circuits and inductances 
        as short circuits.
        Note: Only linear sweep is supported for now 
        '''
        if(len(args)<4):
            raise ValueError("gave faulty parameters for dc sweep")
        for i in range(1, 4):
            if(not (isfloat(args[i]) or isint(args[i])) ):
                raise ValueError('gave faulty parameters for simulation')
        dic = dict()
        dic[args[0]] = slice(convert_num(args[1]), convert_num(args[2]), convert_num(args[3]))
        simulator = self.circuit.simulator(temperature=25, nominal_temperature=25)
        analysis = simulator.dc(**dic)
        probed_values = list(analysis.nodes['n002'])
        for i in range(len(probed_values)):
            probed_values[i] = float(probed_values[i])
        amplitude = max(probed_values)
        self.plot_graph('Voltage (n1) vs Voltage(n2)','Voltage[Vn2]','Voltage [Vn1]',amplitude,analysis.nodes['n001'],analysis.nodes['n002'])
    
    def simulate_mode_ac_analysis(self, args):
        '''
        Computes the small signal AC behaviour of the 
        circuit linearied about its DC operating point 
        '''
        if(len(args)< 4):
            raise ValueError("gave faulty parameters for simulation")
        for i in range(1, 4):
            if(not (isfloat(args[i]) or isint(args[i])) ):
                raise ValueError("gave faulty parameters for simulation")
        if(args[0] not in ['lin', 'dec', 'oct']):
            raise ValueError("gave faulty parameters for simulation")
        print(args)
        amplitude_imag = -1000000e-8 
        amplitude_real = 2
        simulator = self.circuit.simulator(temperature=25, nominal_temperature=25)
        analysis = simulator.ac(start_frequency=convert_num(args[2]), stop_frequency=convert_num(args[3]), number_of_points=convert_num(args[1]),  variation=args[0])
        self.plot_graph('Frequency Response Bode plot','dB','Frequency',amplitude_real,np.real(analysis.nodes['n002']))
        self.plot_graph('Frequency Response Bode plot','dB','Frequency',amplitude_imag,np.imag(analysis.nodes['n002']))

def parse_schematic_paths_for_problems(container):
    netlists = []
    for problem in container.get_problems():
        netlists.append(spice_schematic(problem.circuit_schematic_path, problem))
    # for netlist in netlists:
    #     _insert_helper_func to modifify component values based on parameters
    for sim_netlist in netlists:
        sim_type, sim_args = sim_netlist.fetch_sim_type_and_args()
        print('here is what was parsed')
        print(sim_type)
        print(sim_args)
        print('done')
        if(sim_type == '.op'):
            sim_netlist.simulate_mode_dc_op()
        elif(sim_type == '.tran'):
            sim_netlist.simulate_mode_transient(sim_args)
        elif(sim_type == '.tf'):
            sim_netlist.simulate_mode_dc_transfer(sim_args)
        elif(sim_type == '.dc'):
            sim_netlist.simulate_mode_dc_sweep(sim_args)
        elif(sim_type == '.ac'):
            sim_netlist.simulate_mode_ac_analysis(sim_args)
        else:
            raise ValueError("simulation file has unknown simulation type")

if __name__ == "__main__":
    print('why is this being run?')