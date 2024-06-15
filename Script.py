import pyodbc
import Credentials as c
import pandas as pd

server = c.server
database = c.database
username = c.username
password = c.password

connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
conn = pyodbc.connect(connectionString, autocommit=True)
cursor = conn.cursor()

cursor.execute("USE AdventureWorks2022")

df = pd.read_sql_query('select * from [Purchasing].[ProductVendor]', conn)
df = df.fillna(value=0)

cursor.execute("USE AWLanding")

cursor.execute("IF OBJECT_ID('[Purchasing].[ProductVendor]', 'U') IS NOT NULL TRUNCATE TABLE [Purchasing].[ProductVendor];")

for index, row in df.iterrows():
    cursor.execute("INSERT INTO [Purchasing].[ProductVendor] values(?,?,?,?,?,?,?,?,?,?,?)", row.ProductID, row.BusinessEntityID, row.AverageLeadTime, row.StandardPrice, row.LastReceiptCost, row.LastReceiptDate, row.MinOrderQty, row.MaxOrderQty, row.OnOrderQty, row.UnitMeasureCode, row.ModifiedDate)

cursor.execute("USE AdventureWorks2022")

df = pd.read_sql_query('select * from [Purchasing].[PurchaseOrderDetail]', conn)
df = df.fillna(value=0)

cursor.execute("USE AWLanding")

cursor.execute("IF OBJECT_ID('[Purchasing].[PurchaseOrderDetail]', 'U') IS NOT NULL TRUNCATE TABLE [Purchasing].[PurchaseOrderDetail];")

for index, row in df.iterrows():
    cursor.execute("INSERT INTO [Purchasing].[PurchaseOrderDetail] values(?,?,?,?,?,?,?,?,?,?,?)", row.PurchaseOrderID, row.PurchaseOrderDetailID, row.DueDate, row.OrderQty, row.ProductID, row.UnitPrice, row.LineTotal, row.ReceivedQty, row.RejectedQty, row.StockedQty, row.ModifiedDate)

cursor.execute("USE AdventureWorks2022")

df = pd.read_sql_query('select * from [Purchasing].[PurchaseOrderHeader]', conn)
df = df.fillna(value=0)

cursor.execute("USE AWLanding")

cursor.execute("IF OBJECT_ID('[Purchasing].[PurchaseOrderHeader]', 'U') IS NOT NULL TRUNCATE TABLE [Purchasing].[PurchaseOrderHeader];")

for index, row in df.iterrows():
    cursor.execute("INSERT INTO [Purchasing].[PurchaseOrderHeader] values(?,?,?,?,?,?,?,?,?,?,?,?)", row.PurchaseOrderID, row.RevisionNumber, row.Status, row.EmployeeID, row.VendorID, row.ShipMethodID, row.OrderDate, row.ShipDate, row.SubTotal, row.TaxAmt, row.Freight, row.ModifiedDate)

cursor.execute("USE AdventureWorks2022")

df = pd.read_sql_query('select * from [Purchasing].[ShipMethod]', conn)
df = df.fillna(value=0)

cursor.execute("USE AWLanding")

cursor.execute("IF OBJECT_ID('[Purchasing].[ShipMethod]', 'U') IS NOT NULL TRUNCATE TABLE [Purchasing].[ShipMethod];")

for index, row in df.iterrows():
    cursor.execute("INSERT INTO [Purchasing].[ShipMethod] values(?,?,?,?,?,?)", row.ShipMethodID, row.Name, row.ShipBase, row.ShipRate, row.rowguid, row.ModifiedDate)

cursor.execute("USE AdventureWorks2022")

df = pd.read_sql_query('select * from [Purchasing].[Vendor]', conn)
df = df.fillna(value=0)

cursor.execute("USE AWLanding")

cursor.execute("IF OBJECT_ID('[Purchasing].[Vendor]', 'U') IS NOT NULL TRUNCATE TABLE [Purchasing].[Vendor];")

for index, row in df.iterrows():
    cursor.execute("INSERT INTO [Purchasing].[Vendor] values(?,?,?,?,?,?,?,?)", row.BusinessEntityID, row.AccountNumber, row.Name, row.CreditRating, row.PreferredVendorStatus, row.ActiveFlag, row.PurchasingWebServiceURL, row.ModifiedDate)

cursor.execute("USE AdventureWorks2022")
