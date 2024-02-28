The simulation in this directory aims to provide simulations and quantitative metric values for the 9m vs 13m trade study.  Specifically, this directory deals with the "full array" configuration.

To set up the necessary environment for running the simulation, the user must first install the Python-based ngehtsim package.  The installation requires at least Python version 3.8, and it can be carried out using the requirements.txt document by running:

> pip install -r requirements.txt

This simulation is then run in two parts.

The first part requires running the "gendata.py" script.  This script produces a number directories containing (u,v)-coverage plots and .uvfits files capturing simulations of M87 carried out under different weather instantiations.  A geometric model for the M87 near-horizon source structure is used, though the recovered metric values have been shown to be consistent with those produced using proprietary GRMHD+GRRT simulations for the source structure.  Note: The gendata.py script will take several hours to complete on a typical laptop or desktop.

After gendata.py has finished running, the "compute_metrics_full_array.py" script should be run.  This script computes and prints out the various metric values appropriate for "full array" operations of the array, and it produces some comparison plots.
