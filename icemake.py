

import os

if __name__ == "__main__":
    os.system("icemaker -export ex1.svg .\sample_asc_files\simple_R_series.asc ")  
    os.system("inkscape --export-type=png ex1.svg ")