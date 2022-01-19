#!/bin/bash
for i in {0..30}
do
   export PYTHONHASHSEED=$((i * 100))
   python run.py --run_id=$i
done