import os

import numpy as np
import pandas as pd
import scanpy as sc
import scvi




modified=sc.read_h5ad('/proj/sensoryaging/data/data/up_dated_data/SGNs/training_model.h5ad')


sc.pp.highly_variable_genes(modified, n_top_genes=3500, flavor='seurat_v3',layer='umi',subset=True)

scvi.model.SCVI.setup_anndata(modified, layer="umi")

scvi_model = scvi.model.SCVI(modified, n_layers=2, n_latent=50)

scvi_model.train(max_epochs=50)

scvi_model.save('/proj/sensoryaging/data/data/up_dated_data/SGNs/SCVI_model',save_anndata=True, overwrite=True)


scanvi_model = scvi.model.SCANVI.from_scvi_model(
    scvi_model,
    adata=modified,
    unlabeled_category="Unknown",
    labels_key='leiden_new',
)

scanvi_model.train(max_epochs=100, n_samples_per_label=30)

scanvi_model.save('/proj/sensoryaging/data/data/up_dated_data/SGNs/SCANVI_model',save_anndata=True, overwrite=True)
