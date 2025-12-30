import pandas as pd

def analyze_oversupply(csv_path):
    """
    Identify years of oversupply based on dual criteria:
    1. Production exceeds 5-year moving average by more than 3%.
    2. Average price for the year is below the 10-year moving average price.
    
    This dual-condition model ensures that intervention is triggered only when
    excess supply coincides with depressed prices, making the policy more
    targeted and economically justified.
    """
    df = pd.read_csv(csv_path)
    
    # Calculate 5-year moving average of production
    df['prod_ma5'] = df['total_production'].rolling(window=5, min_periods=1).mean()
    
    # Calculate 10-year moving average of price
    df['price_ma10'] = df['avg_price'].rolling(window=10, min_periods=1).mean()
    
    # Condition 1: production > 3% above its 5-year moving average
    cond1 = df['total_production'] > (1.03 * df['prod_ma5'])
    
    # Condition 2: price below its 10-year moving average
    cond2 = df['avg_price'] < df['price_ma10']
    
    # Oversupply year: both conditions true
    df['oversupply'] = cond1 & cond2
    
    # Get list of oversupply years
    oversupply_years = df[df['oversupply']]['year'].tolist()
    
    return oversupply_years

if __name__ == "__main__":
    oversupply = analyze_oversupply('data/wheat_historical_data.csv')
    print("Oversupply years (production > 3% above 5‑year MA AND price below 10‑year MA):")
    print(oversupply)