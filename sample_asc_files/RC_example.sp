Example netlist
R1 N002 N001 100
C1 N002 0 100f
V1 N001 0 SINE(0 4 1K 0 0 0)
.tran 0.000001 0.02 0.01
.print tran V(N001)
*use this simulation file for transient example
.end
