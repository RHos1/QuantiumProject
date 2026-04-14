import pandas as pd
import os

data_folder = './data'
output_file = 'formatted_data.csv'
processed_dfs = []

for filename in os.listdir(data_folder):
    if filename.endswith(".csv"):
        file_path = os.path.join(data_folder, filename)
        
        df = pd.read_csv(file_path)
        
        df = df[df['product'].str.lower() == 'pink morsel']
        
        if df['price'].dtype == 'object':
            df['price'] = df['price'].str.replace('$', '', regex=False).astype(float)
        
        df['sales'] = df['price'] * df['quantity']
        
        df = df[['sales', 'date', 'region']]
        
        processed_dfs.append(df)

final_df = pd.concat(processed_dfs, ignore_index=True)
final_df.to_csv(output_file, index=False)

print(f"Data processing complete! Created {output_file}")