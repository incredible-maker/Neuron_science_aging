import scanpy as sc
import pandas as pd
adata=sc.read_h5ad("/proj/sensoryaging/data/data/new_data_11.9/modified_data/modified.h5ad")

import os
unique_platesID=adata.obs['platesID'].unique()
save_path='/proj/sensoryaging/data/data/data_for_yuvraj'
for plate_id in unique_platesID:
    subset=adata[adata.obs['platesID']==plate_id]
    df = pd.DataFrame(subset.X, index=subset.obs.index, columns=subset.var.index)

    # 构建文件名和路径
    file_name = f"{plate_id}.csv"
    file_path = os.path.join(save_path, file_name)

    # 导出 CSV 文件
    df.to_csv(file_path)

print("File done")