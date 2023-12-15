import os

import numpy as np
import pandas as pd
import scanpy as sc
import scvi




modified=sc.read_h5ad('/proj/sensoryaging/60_plates_data/Human_data/Ml/merged_data.h5ad')

# modified.layers["counts"] = modified.X.copy()
# sc.pp.normalize_total(modified, target_sum=1e4)
# sc.pp.log1p(modified)
# modified.layers["log1p"] = modified.X.copy()
# modified.X = modified.layers["counts"].copy()
# sc.pp.highly_variable_genes(modified, n_top_genes=3000, flavor='seurat_v3',layer='counts',subset=True, batch_key='Species')

# scvi.model.SCVI.setup_anndata(modified, layer="counts", batch_key='Species',continuous_covariate_keys=['total_counts'])

# scvi_model = scvi.model.SCVI(modified, n_layers=2, n_latent=50, dispersion='gene-batch',gene_likelihood='nb')

# scvi_model.train(max_epochs=50)

# scvi_model.save('/proj/sensoryaging/60_plates_data/Human_data/Ml/scvi_model',save_anndata=True, overwrite=True)

scvi_model= scvi.model.SCVI.load('/proj/sensoryaging/60_plates_data/Human_data/Ml/scvi_model')
scanvi_model = scvi.model.SCANVI.from_scvi_model(
    scvi_model,
    adata=modified,
    unlabeled_category="unknown",
    labels_key='scvi_cell_type',
)

scanvi_model.train(max_epochs=100, n_samples_per_label=15,batch_size=64,check_val_every_n_epoch=5)

scanvi_model.save('/proj/sensoryaging/60_plates_data/Human_data/Ml/scanvi_model',save_anndata=True, overwrite=True)