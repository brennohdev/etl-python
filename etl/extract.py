import pandas as pd

def read_csv(filepath):
    try:
        return pd.read_csv(filepath)
    except FileNotFoundError:
        print(f"Error: The file {filepath} was not found.")
    except pd.errors.ParserError:
        print(f"Error: The file {filepath} could not be parsed. Please check the file format.")
        return None
    
    