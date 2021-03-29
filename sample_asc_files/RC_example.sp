Example netlist
R_1 N002 N001 47
C_1 N002 0 50
V1 N001 0 AC 3
*.tran 0.000001 0.02 0.01
*.print tran V(N001)
*use this simulation file for transient example
.ac lin 100 1 500
.print V(N002)
.end
