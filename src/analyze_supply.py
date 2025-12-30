import pandas as pd

def analyze_oversupply(csv_path):
    """Identify years of oversupply based on production threshold."""
    df = pd.read_csv(csv_path)
    
    # Calculate 5-year moving average of production
    df['prod_ma5'] = df['total_production'].rolling(window=5, min_periods=1).mean()
    
    # Flag oversupply: production > 5% above moving average
    df['oversupply'] = df['total_production'] > (1.05 * df['prod_ma5'])
    
    # Get list of oversupply years
    oversupply_years = df[df['oversupply']]['year'].tolist()
    
    return oversupply_years

if __name__ == "__main__":
    oversupply = analyze_oversupply('data/wheat_historical_data.csv')
    print("Oversupply years (production > 5% above 5-year moving average):")
    print(oversupply)