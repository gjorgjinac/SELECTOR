from dom_mis import run_dom_mis
import argparse
from typing import List

similarity_thresholds=[0.9,0.95,0.97]
parser = argparse.ArgumentParser()
parser.add_argument('--run_id', required=True, type=int)

args = parser.parse_args().__dict__


print(f'Run id: {args["run_id"]}, similarity thresholds: {similarity_thresholds}')
run_dom_mis(args['run_id'], similarity_thresholds, save_results=True)