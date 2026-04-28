import pandas as pd
import os

def process_algorithm_performance(input_file: str):
    """
    Loads a CSV file, groups by the 'algorithm' column, calculates the average runtime
    for each algorithm, computes the absolute difference between each runtime and
    the group's mean runtime, adds it as 'perf_variation', and saves the result
    as '<basename>_perf_variation.csv' in the same directory.
    
    Parameters:
        input_file (str): Path to the input CSV file.
    """
    # Load CSV file
    df = pd.read_csv(input_file)
    
    # Ensure necessary columns exist
    if 'algorithm' not in df.columns or 'runtime' not in df.columns:
        raise ValueError("Input CSV must contain 'algorithm' and 'runtime' columns.")
    
    # Compute mean runtime for each algorithm
    algo_avg = df.groupby('algorithm')['runtime'].mean()
    
    # Map averages back to the dataframe
    df['avg_runtime'] = df['algorithm'].map(algo_avg)
    
    # Compute absolute difference between runtime and average
    df['perf_variation'] = (df['runtime'] - df['avg_runtime']).abs()
    
    # Determine output file name
    base, ext = os.path.splitext(input_file)
    output_file = f"{base}_perf_variation.csv"
    
    # Save to CSV
    df.to_csv(output_file, index=False)
    print(f"Processed file saved as: {output_file}")

files = ["cg.csv",	"ft.csv",	"lu.csv",
"amr.csv","comd.csv","kripke.csv","mg.csv"]

for f in files:
   process_algorithm_performance(f)
