The simulation in this directory aims to provide quantitative values for some of the metrics relevant for the System Architecture Description Document (SADD).  Specifically, it quantifies the "minimum baseline RMS noise," "inverse shortest projected non-intrasite baseline," "inverse longest projected baseline," and "point source sensitivity" metrics appropriate for "monitoring array" operations of the array.

To set up the necessary environment for running the simulation, the user must first install the Python-based ngehtsim package.  The installation requires at least Python version 3.8, and it can be carried out using the requirements.txt document by running:

> pip install -r requirements.txt

This simulation is then run in two parts.

The first part requires running the "gendata.py" script.  This script will produce a directory containing a number of .uvfits files capturing simulations carried out under different weather instantiations.  A geometric model for the M87 near-horizon source structure is used, though the recovered metric values have been shown to be consistent with those produced using proprietary GRMHD+GRRT simulations for the source structure.

After gendata.py has finished running, the "compute_metrics_monitoring_array.py" script should be run.  This script computes and prints out the various metric values appropriate for "monitoring array" operations of the array.
