import pandas as pd
import matplotlib.pyplot as plt

def plot_csv_column(csv_path, column_name):
    """
    Reads a CSV file and plots the specified column.
    """
    df = pd.read_csv(csv_path)
    if column_name not in df.columns:
        print(f"Column '{column_name}' not found in CSV.")
        return
    plt.figure(figsize=(10, 5))
    plt.plot(df[column_name])
    plt.title(f"{column_name} over rows")
    plt.xlabel("Row")
    plt.ylabel(column_name)
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    plot_csv_column('./NVIDIA_App_Performance_Log_2025-05-20T20-38-33.csv', 'FPS')