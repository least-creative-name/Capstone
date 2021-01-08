* C:\Users\Shruti Patel\Documents\GitHub\capstone_project\Capstone\sample_asc_files\volt_div.asc
V1 N001 0 10
R_1 N002 N001 3
R_2 N002 0 7
*.tf v(N002,0) V1
.op
*.dc V1 0 20 2
* use V1 N001 0 10 for all the above simulation types
*.ac lin 15 10000 25000
* use V1 N001 0 AC 3 for ac sweep simulation
.print V(N001)
.end
