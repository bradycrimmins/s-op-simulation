# S&OP Simulation for Supply Chain Management

This repository contains Python code designed to fetch historical sales data, production capacity, and inventory levels from cloud and on-premises databases. It then simulates inventory levels over time based on sales forecasts, production plans, initial inventory, and lead times. The simulation helps in understanding how different factors influence inventory levels, aiding in making informed decisions regarding production and inventory management in supply chain operations.

## Description

The code performs the following key tasks:

1. **Data Fetching:** Retrieves historical sales data, production capacity, and inventory levels from specified databases using SQL queries. This data is crucial for simulating accurate inventory levels.
   
2. **Inventory Simulation:** Simulates inventory levels over time based on provided sales forecasts, production plans, initial inventory, and lead times. The simulation accounts for the delay in production affecting inventory due to lead times and adjusts inventory based on sales and production quantities.

3. **Visualization:** Plots the simulated inventory levels over time, providing a visual representation of how inventory levels are expected to change. This visualization aids in identifying potential shortages or excesses in inventory, allowing for timely adjustments to production plans.

## Setup

### Database Connections
- Two SQLAlchemy engine connections are established to fetch data from cloud and on-premises databases. Replace `your_cloud_database_connection_string` and `your_on_premises_database_connection_string` with your actual database connection strings.

### SQL Queries
- Three SQL queries are used to fetch the necessary data:
  - `sales_sql` fetches historical sales data.
  - `capacity_sql` fetches production capacity.
  - `inventory_sql` fetches inventory levels.

### Inventory Simulation Function
- The `simulate_inventory` function simulates inventory levels based on sales forecasts, production plans, initial inventory, and lead times. Adjust the placeholders for actual forecast data, production plan, initial inventory, and lead time as per your data.

## Usage

1. **Database Query Execution:**
   - Execute the provided SQL queries to fetch the necessary data.
   - Ensure your database user has the required permissions to execute these queries.

2. **Simulation:**
   - Call the `simulate_inventory` function with your sales forecast, production plan, initial inventory, and lead time data to simulate inventory levels.

3. **Visualization:**
   - Run the visualization code to plot the simulated inventory levels over time. This plot helps in understanding inventory dynamics and planning accordingly.

## Requirements

- SQLAlchemy: For database connection and query execution.
- pandas: For data manipulation and analysis.
- numpy: For numerical operations.
- matplotlib: For plotting the inventory level simulation.

Ensure you have these libraries installed in your Python environment to successfully run the code.

## Contributing
Contributions to enhance the simulation's accuracy, efficiency, or usability are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.

## License
This project is open-source and available for personal and commercial use.
