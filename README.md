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
Without simulation
![Without simulation](https://github.com/least-creative-name/Capstone/blob/main/Readme_img_02.JPG?raw=true)

With simulation
![With simulation](https://github.com/least-creative-name/Capstone/blob/main/Readme_img_01.JPG?raw=true)


### External Links and resources 

### Future Improvement 
