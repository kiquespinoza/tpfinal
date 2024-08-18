import pandas as pd  


df1 = pd.read_csv(r'C:\Users\eespice\Desktop\tp2\pds\ecommerce_customers_dataset.csv')
df2 = pd.read_csv(r'C:\Users\eespice\Desktop\tp2\pds\ecommerce_order_items_dataset.csv')
df3 = pd.read_csv(r'C:\Users\eespice\Desktop\tp2\tp2.0\ecommerce_order_payments_dataset.csv')
df4 = pd.read_csv(r'C:\Users\eespice\Desktop\tp2\pds\ecommerce_orders_dataset.csv')
df5 = pd.read_csv(r'C:\Users\eespice\Desktop\tp2\pds\ecommerce_products_dataset.csv')


df1.set_index('customer_id', inplace = True)
df2.set_index('order_id', inplace = True) 
df3.set_index('order_id', inplace = True)
df4.set_index('order_id', inplace = True)
df5.set_index('product_id', inplace = True)


total_customers = df1.index.nunique()
print(f'numero total de clientes unicos : {total_customers}')

avg_payment_per_order = df3['payment_value'].mean()
print(f'promedio de valor de pago por pedido: {avg_payment_per_order}')

merged_df = pd.merge(df2, df5, on='product_id')

most_sold_category = merged_df.groupby('product_category_name')['order_item_id'].count().idxmax()
print(f'la categoria de producto mas vendida es: {most_sold_category}')



total_orders = df2.index.nunique()
print(f'numero total de pedidos realizados:{total_orders}')


import sqlite3 

conn = sqlite3.connect('ecommerce.db')

df1.to_sql('customers', conn, if_exists='replace')
df2.to_sql('orders', conn, if_exists='replace')
df3.to_sql('orders_items', conn, if_exists='replace')
df4.to_sql('products', conn, if_exists='replace')
df5.to_sql('payment', conn, if_exists='replace')

