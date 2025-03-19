import pandas as pd
import numpy as np

# Create the data as a dictionary
data = {
    "product_id": [0, 1],
    "store1": [95, 70],
    "store2": [100, np.nan],  # Use np.nan for null values
    "store3": [105, 80]
}


df = pd.DataFrame(data)


print(pd.melt(
    df, id_vars='product_id', var_name='store', value_name='price'
).dropna())