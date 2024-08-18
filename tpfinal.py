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


total_orders = df1.index.nunique()
print(f'numero total de pedidos realizados : {total_orders}')