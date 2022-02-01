#!/bin/bash
export PYTHONHASHSEED=42

python aggregate_ela.py

python clustering.py

for i in {0..30}
do
   export PYTHONHASHSEED=$((i * 100))
   python dom_mis_run.py --run_id=$i
done
