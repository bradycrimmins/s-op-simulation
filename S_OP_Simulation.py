from sqlalchemy import create_engine
import pandas as pd

# Connection strings
cloud_db_string = 'your_cloud_database_connection_string'
on_prem_db_string = 'your_on_premises_database_connection_string'

# Create engines
cloud_engine = create_engine(cloud_db_string)
on_prem_engine = create_engine(on_prem_db_string)

# Fetch historical sales data
sales_sql = """
SELECT product_id, date, quantity_sold
FROM sales
WHERE date >= DATEADD(year, -1, GETDATE());
"""

# Fetch production capacity
capacity_sql = """
SELECT product_id, date, capacity
FROM production_capacity;
"""

# Fetch inventory levels
inventory_sql = """
SELECT product_id, date, inventory_level
FROM inventory;
"""

sales_data = pd.read_sql(sales_sql, cloud_engine)
capacity_data = pd.read_sql(capacity_sql, on_prem_engine)
inventory_data = pd.read_sql(inventory_sql, cloud_engine)

import numpy as np

def simulate_inventory(sales_forecast, production_plan, initial_inventory, lead_time):
    """
    Simulates inventory levels over time.
    
    :param sales_forecast: Array of forecasted sales quantities.
    :param production_plan: Array of planned production quantities.
    :param initial_inventory: Initial inventory level.
    :param lead_time: Lead time in periods before production affects inventory.
    :return: Array of inventory levels over time.
    """
    inventory_levels = [initial_inventory]
    for t in range(len(sales_forecast)):
        # Production adds to inventory after lead time
        production = production_plan[t-lead_time] if t >= lead_time else 0
        new_inventory = inventory_levels[-1] + production - sales_forecast[t]
        inventory_levels.append(max(0, new_inventory))  # Inventory cannot go below zero
    return inventory_levels

# Example usage
sales_forecast = sales_data['quantity_sold'].values  # Placeholder for actual forecast data
production_plan = np.full_like(sales_forecast, 50)  # Placeholder for production plan
initial_inventory = 100  # Placeholder for initial inventory
lead_time = 2  # Placeholder for lead time

inventory_levels = simulate_inventory(sales_forecast, production_plan, initial_inventory, lead_time)

import matplotlib.pyplot as plt

# Visualize inventory levels over time
plt.figure(figsize=(12, 6))
plt.plot(inventory_levels, label='Simulated Inventory Levels')
plt.title('Inventory Level Simulation')
plt.xlabel('Time Period')
plt.ylabel('Inventory Level')
plt.legend()
plt.show()
