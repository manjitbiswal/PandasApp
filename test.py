import pandas as pd
import sqlite3
conn = sqlite3.connect(r"C:\Users\Manjit Biswal\Downloads\sqlite\Data Engineer_ETL Assignment.db")
cursor = conn.cursor()
cursor.execute(" select c.customer_id as customers,c. age,i.item_name as item,sum(o.quantity) as quantity from sales s left join customers c on s.customer_id=c.customer_id inner join orders o on s.sales_id=o.sales_id inner join items i on o.item_id = i.item_id where (c.age between 18 and 35) and (o.quantity<>0) group by c.customer_id,i.item_name;")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()