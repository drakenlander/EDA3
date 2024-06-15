USE AWLanding;

DROP VIEW IF EXISTS Fact_Order;
DROP VIEW IF EXISTS Dim_Vendor;
DROP VIEW IF EXISTS Dim_ShipMethod;
DROP VIEW IF EXISTS Dim_Product;

CREATE VIEW Fact_Order AS
SELECT d.PurchaseOrderID AS OrderID, 
h.VendorID, d.ProductID, 
h.ShipMethodID, d.DueDate, 
d.OrderQty, d.UnitPrice, 
d.ReceivedQty, d.RejectedQty, 
d.StockedQty, 
h.OrderDate, 
h.ShipDate, 
h.SubTotal, 
h.TaxAmt, 
h.Freight, 
h.TotalDue, 
h.ModifiedDate
FROM [Purchasing].[PurchaseOrderDetail] d 
LEFT JOIN [Purchasing].[PurchaseOrderHeader] h
ON d.PurchaseOrderID = h.PurchaseOrderID;

CREATE VIEW Dim_Vendor AS
SELECT v.BusinessEntityID AS VendorID, v.AccountNumber, v.Name, v.CreditRating, v.PreferredVendorStatus, v.ActiveFlag, pv.AverageLeadTime
FROM Purchasing.Vendor v
LEFT JOIN [Purchasing].[ProductVendor] pv
ON v.BusinessEntityID = pv.BusinessEntityID;

CREATE VIEW Dim_ShipMethod AS
SELECT ShipMethodID, Name, ShipBase, ShipRate, rowguid
FROM Purchasing.ShipMethod;

CREATE VIEW Dim_Product AS
SELECT ProductID, StandardPrice, LastReceiptCost, LastReceiptDate, MinOrderQty, MaxOrderQty, UnitMeasureCode
FROM Purchasing.ProductVendor