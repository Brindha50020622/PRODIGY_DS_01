import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Create the DataFrame
data = pd.read_csv(r"C:\Users\sarat\OneDrive\Documents\Task_01\ECommerce_consumer behaviour_2023.csv")

df = pd.DataFrame(data)

# Calculate total number of purchases
total_purchases = len(df)

# Count occurrences of each product_id
product_counts = df['product_id'].value_counts()

# Calculate percentage of each product_id
product_percentage = (product_counts / total_purchases) * 100

# Convert the series to a DataFrame for Plotly
product_percentage_df = product_percentage.reset_index()
product_percentage_df.columns = ['product_id', 'percentage']

# Calculate counts of reordered and not reordered products
reordered_counts = df['reordered'].value_counts()

# Convert the series to a DataFrame for Plotly
reordered_counts_df = reordered_counts.reset_index()
reordered_counts_df.columns = ['reordered', 'count']

#Interactive bar plot for Reordered plot
fig_reordered = px.bar(
    reordered_counts_df,
    x='reordered',
    y='count',
    labels={'reordered': 'Reordered', 'count': 'Count'},
    title='Count of Reordered and Not Reordered Products',
    color='reordered', 
)

# Create the interactive bar plot
fig = px.bar(
    product_percentage_df,
    x='product_id',
    y='percentage',
    labels={'product_id': 'Product ID', 'percentage': 'Percentage of Purchases (%)'},
    title='Percentage of Purchases by Product ID',
    hover_data={'percentage': ':.2f'},  # Format the hover data to 2 decimal places
    color='percentage',  # Color bars based on percentage
    color_continuous_scale='viridis',  
)

#Annotation for maximum percentage
max_percentage = product_percentage_df['percentage'].max()
max_product_id = product_percentage_df.loc[product_percentage_df['percentage'].idxmax(), 'product_id']
fig.add_annotation(x=max_product_id, y=max_percentage,
                   text=f'Max: {max_percentage:.2f}%',
                   showarrow=True,
                   arrowhead=1)


# Show the plot
fig.show()
fig_reordered.show()
