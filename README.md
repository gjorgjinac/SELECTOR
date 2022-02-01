## SELECTOR: Selecting a Representative Benchmark Suite for Reproducible Statistical Comparison

![SELECTOR methodology pipeline](visualizations/selector_pipeline.pdf)

### Setup
Python 3.7 or 3.8 is recommended to be used.

All of the required libraries are listed in the _requirements.txt_ file and can be installed using the following command:

- `cat requirements.txt | xargs -n 1 pip install` (Linux)

- `FOR /F %k in (requirements.txt) DO pip install %k` (Windows)

### Usage

- Run All Instance Selection heuristics:
  - `run_all.sh` - Run the Clustering and 30 runs of the Graph Theory Algorithms

- Problem Instance Representation 
  - `ela_feature_definition.py` - Definition of the ELA features used for representing problem instances
  - `aggregate_ela.py` - Generation of representations for each problem instance by taking the median of the ELA features calculated in 30 different runs
  
- Instance Selection Using Clustering
  - `clustering.ipynb` - Generation of initial 12 cluster and subsequent subclustering of the largest cluster
  
- Instance Selection Using Graph Theory Algorithms
  - `dom_mis.py` - Utility function for generating the similarity graph and execution of the algorithms for finding Dominating and Maximal Independent Sets
  - `dom_mis_run.py` - Script for running the utility function in `dom_mis.py` from the command line
  - `dom_mis_run_30.sh` - Bash script for running 30 executions of the Dominating and Maximal Independent Sets algorithms with different random seeds
  
- Visualizations and Analysis:
  - `cluster_analysis.ipynb`
  - `graph_analysis.ipynb`
  - `stats.ipynb`