import pandas as pd
import numpy as np

def create_stock_series():
    tickers = ['AAPL', 'GOOG', 'MSFT', 'TSLA', 'AMZN']
    prices = np.round(np.random.uniform(100, 1000, size=5), 2)
    stock_series = pd.Series(prices, index=tickers)
    return stock_series

def create_employee_dataframe():
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan'],
        'Department': ['HR', 'Engineering', 'Marketing', 'Finance', 'IT'],
        'Salary': [70000, 85000, 60000, 75000, 80000]
    }
    employee_ids = [f'EMP{str(i).zfill(3)}' for i in range(1, 6)]
    employee_df = pd.DataFrame(data, index=employee_ids)
    return employee_df

def main():
    # Generate Series
    stock_series = create_stock_series()
    stock_series.to_csv('stock_prices.csv')
    print("Stock Series saved to 'stock_prices.csv'.")

    # Generate DataFrame
    employee_df = create_employee_dataframe()
    employee_df.to_csv('employee_data.csv')
    print("Employee DataFrame saved to 'employee_data.csv'.")

if __name__ == "__main__":
    main()
