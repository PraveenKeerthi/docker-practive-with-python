import os
import pandas as pd


# determine output directory from environment (default to /app)
out_dir = os.environ.get('OUTPUT_DIR', '/app')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, 'update_order.csv')

df = pd.read_csv('Order_v3.csv', encoding='latin1')
# remove columns that are entirely null
df = df.dropna(axis=1, how='all')

# select useful columns and sort
updated_df = df[['orderIdentifier', 'vendor.organizationIdentifier', 'buyer.organizationIdentifier', 'quantity', 'totalValue']]
updated_df = updated_df.sort_values('quantity', ascending=False)

# write the processed CSV to the configured output path
updated_df.to_csv(out_path, index=False)