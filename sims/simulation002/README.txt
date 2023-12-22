This simulation is run in two parts.

The first part uses the "gendata.py" script and requires access to proprietary data.  Specifically, we use synthetic images of M87 produced from GRMHD+GRRT simulations that have been carried out by Andrew Chael.  The images are stored in a proprietary location that is accessed by the "gendata.py" script, which then produces .uvfits files that are stored in this repository.

The second part uses the "compute_metrics_monitoring_array.py" script, which computes and prints out various metric values appropriate for "monitoring array" operations of the array.
