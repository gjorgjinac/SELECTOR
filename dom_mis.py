import os
import pandas as pd
import numpy as np
from networkx import Graph, write_adjlist, read_adjlist
from sklearn.metrics.pairwise import cosine_similarity
from collections import defaultdict
from ela_feature_definition import ela_feature_names
from networkx.algorithms.dominating import dominating_set
from networkx.algorithms.mis import maximal_independent_set
import random

def set_random_seed(seed):
    np.random.seed(seed)
    random.seed(seed)
    
def generate_graph_from_similarity_matrix(min_similarity_threshold, na_handling_setting_name):
    ela_representation_df = pd.read_csv(f'data/aggregated_ela_representation_{na_handling_setting_name}.csv', index_col=[0,1,2])
    s = cosine_similarity(ela_representation_df.values,ela_representation_df.values)
    similarity_df=pd.DataFrame(s,index=ela_representation_df.index,columns=ela_representation_df.index)
    
    
    g = Graph()
    g.add_nodes_from(similarity_df.index)

    i=0
    for index1, row1 in similarity_df.iterrows():
        for index2 in row1.keys():
            i+=1
            if index1==index2:
                continue
            if row1[index2] > min_similarity_threshold:
                g.add_edge(index1, index2)
            if i % 1000000==0:
                print(f'{100*  round(i/(similarity_df.shape[0]*similarity_df.shape[0]),2)}%')
    return g

def run_dom_mis(run_id, similarity_thresholds, save_results=False):
    set_random_seed(run_id*100)
    id_columns=['suite','fid', 'iid']
    for na_handling_setting_name in ['dropna','fillna']:


        for min_similarity_threshold in similarity_thresholds:
            
            
            graph_file_name=f'data/graph_{min_similarity_threshold}_{na_handling_setting_name}_adj'
            g=generate_graph_from_similarity_matrix(min_similarity_threshold, na_handling_setting_name)
            if not os.path.isfile(graph_file_name):
                write_adjlist(g,graph_file_name)
            for algorithm_name, algorithm_results in [('dominant', dominating_set(g)), ('mis', maximal_independent_set(g))]:
                print(algorithm_results)
                if save_results:
                    result_directory=os.path.join('results',na_handling_setting_name,algorithm_name)
                    os.makedirs(result_directory, exist_ok=True)
                    result_file_name=os.path.join(result_directory,f'{min_similarity_threshold}_{run_id}.csv')
                    pd.DataFrame(algorithm_results,columns=id_columns).to_csv(result_file_name)
