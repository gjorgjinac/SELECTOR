import pandas as pd
import numpy as np
from networkx import Graph, write_adjlist
from sklearn.metrics.pairwise import cosine_similarity
from collections import defaultdict
from ela_feature_definition import ela_feature_names
from networkx.algorithms.dominating import dominating_set
from networkx.algorithms.mis import maximal_independent_set


df = pd.read_csv('data/ela.csv', index_col=[0])
ela_df=df[ela_feature_names]
id_columns=['suite','fid', 'iid']


pd.options.mode.use_inf_as_na = True

df_dropna=df.dropna(axis=1)
df_fillna=df.fillna(df.mean())
print(df.shape)
print(df_dropna.shape)
print(df_fillna.shape)


for na_handling_setting_name, df_without_na in [('dropna', df_dropna), ('fillna', df_fillna)]:
    ela_representation_df = df_without_na.groupby(id_columns).median()
    ela_representation_df.to_csv(f'data/aggregated_ela_representation_{na_handling_setting_name}.csv')