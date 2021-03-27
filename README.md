## Electronics Problem Set Generator - ECE496
This tool genereates multiple variants of a problem sets for electronics courses given a base input file 

### Installation Guide 
To clone this repository use the below command 

`git clone https://github.com/least-creative-name/Capstone.git`

Seperate installations are needed for the individual packaages needed to support the project.<br />
The necessary prerequisites are listed in the next section along with links to their installations. 

### Prerequisites 
Below is a list of tools and links to their installations needed to support individual functionality relating to this project :  
* [Pyspice v1.3 or up](https://pyspice.fabrice-salvaire.fr/releases/v1.3/)
* [Ngspice](http://ngspice.sourceforge.net/docs.html)
* [Icewire](https://icewire.ca/)
* [Inkscape](https://inkscape.org/)  
* [TexLive or other LaTEX distribution](https://www.tug.org/texlive/)

OS supported
* Windows (recommended)
* Linux (Ubuntu 18.0)

Python version - 3.8.0 + (recommended)<br />
Also works with latest [Anaconda](https://www.anaconda.com/products/individual) distribution 

### Usage
Once the above listed prerequisites have been installed Follow the below steps to generate multiple variants 

### _1. Creating base input file_ .
Create the problem specification file specifying the questions to be randomized along with the relevant formatting details
A specification for the template can be found in this repository. 

A sample input file is attached below . We have one input file for regular questions and another to showcase simulator input.
Note that the simulator input is only intended as a verification tool and not intended to produce solutions as these may or may not 
account for approximations and differences in the way the course is conducted. The outputs from the simulator are piped to and output file 
or saved as images in the simulation directory.

#### Sample Input files  
No simulation : <br />
![Without simulation](https://github.com/least-creative-name/Capstone/blob/main/Readme_img_02.JPG?raw=true)

With simulation : <br />
![With simulation](https://github.com/least-creative-name/Capstone/blob/main/Readme_img_01.JPG?raw=true)

The relevant specifics/details on the base file creation and functions supported are provided in the input specification guide 
that is attached with this repository

### _2. Create spice schematic (Optional)_ .
Start by going into LTspice or any other spice simulation software and create the necessary netlist file to be verified 
corresponding to given problem. 
From here we need to generate two files which are the .sp and .asc schematic files. 

These two files are then pointed to in the base input file using the _SCHEMATIC_ keyword as shown [here](https://github.com/least-creative-name/Capstone/blob/main/Readme_img_01.JPG?raw=true)

the _TOSIM_ keyword then simulates the relevant variables . More details are mentioned in the input specification guide

###  _3. Run the tool_ .
To run the tool use the below command 
  `python3.8 problem_set_generator.py -input input_file.txt -num_variants ###`




### External Links and resources 

### Future Improvement 
