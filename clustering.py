import random

import numpy as np
import pandas as pd
from ela_feature_definition import ela_feature_names
from sklearn.cluster import AgglomerativeClustering


def set_random_seed(seed):
    np.random.seed(seed)
    random.seed(seed)


set_random_seed(42)

save_clusters = False

ela = pd.read_csv('data/aggregated_ela_representation_dropna.csv', index_col=[0, 1, 2])
ela = ela[set(ela_feature_names).intersection(ela.columns)]

initial_cluster_count = 12
metric = 'cosine'
agglomerative = AgglomerativeClustering(n_clusters=initial_cluster_count, affinity=metric, linkage='complete')
labels = agglomerative.fit(ela).labels_
cluster_12_df = ela.copy()
cluster_label_column = f'clustering_{initial_cluster_count}_clusters'
cluster_12_df[cluster_label_column] = labels
if save_clusters:
    cluster_12_df.to_csv(f'data/hierarchical_clustering_{initial_cluster_count}.csv')

cluster_sizes = pd.DataFrame(cluster_12_df[cluster_label_column]).value_counts()
max_cluster_size = cluster_sizes.max()
largest_cluster_id = cluster_sizes[cluster_sizes == max_cluster_size].index[0][0]

ela = cluster_12_df[cluster_12_df[cluster_label_column] == largest_cluster_id]
ela = ela[set(ela_feature_names).intersection(ela.columns)]
removed_instances = cluster_12_df[cluster_12_df[cluster_label_column] != largest_cluster_id]

selected_cluster_counts = [10, 15]
for cluster_count in selected_cluster_counts:
    agglomerative = AgglomerativeClustering(n_clusters=cluster_count, affinity=metric, linkage='complete')
    labels = agglomerative.fit(ela).labels_
    ela[f'subclustering_{cluster_count}_clusters'] = [initial_cluster_count + l for l in labels]
    removed_instances[f'subclustering_{cluster_count}_clusters'] = removed_instances[cluster_label_column]

all_instances = ela.append(removed_instances)
if save_clusters:
    all_instances.to_csv('data/subclustering.csv')
print(all_instances)