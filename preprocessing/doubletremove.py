import scanpy as sc
import pandas as pd
import scvi

import scvi
introexon2=sc.read_h5ad("/proj/sensoryaging/data/data/up_dated_data/SGNs/introexon2.h5ad")
scvi.model.SCVI.setup_anndata(introexon2)
vae=scvi.model.SCVI(introexon2)
vae.train()

solo=scvi.external.SOLO.from_scvi_model(vae)
solo.train

solo.predict()
df=solo.predict()
df['prediction']=solo.predict(soft=False)
df[df.prediction=='doublet']
introexon2.obs['doublet']=df.prediction

introexon2.to_h5ad("/proj/sensoryaging/data/data/up_dated_data/SGNs/introexon2.h5ad")
print("completed")