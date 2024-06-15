USE [AWLanding];

IF OBJECT_ID('[Purchasing].[ProductVendor]', 'U') IS NOT NULL
DROP TABLE [Purchasing].[ProductVendor];

SELECT * INTO [Purchasing].[ProductVendor] FROM [AdventureWorks2022].[Purchasing].[ProductVendor];

IF OBJECT_ID('[Purchasing].[PurchaseOrderDetail]', 'U') IS NOT NULL
DROP TABLE [Purchasing].[PurchaseOrderDetail];

SELECT * INTO [Purchasing].[PurchaseOrderDetail] FROM [AdventureWorks2022].[Purchasing].[PurchaseOrderDetail];

IF OBJECT_ID('[Purchasing].[PurchaseOrderHeader]', 'U') IS NOT NULL
DROP TABLE [Purchasing].[PurchaseOrderHeader];

SELECT * INTO [Purchasing].[PurchaseOrderHeader] FROM [AdventureWorks2022].[Purchasing].[PurchaseOrderHeader];

IF OBJECT_ID('[Purchasing].[ShipMethod]', 'U') IS NOT NULL
DROP TABLE [Purchasing].[ShipMethod];

SELECT * INTO [Purchasing].[ShipMethod] FROM [AdventureWorks2022].[Purchasing].[ShipMethod];

IF OBJECT_ID('[Purchasing].[Vendor]', 'U') IS NOT NULL
DROP TABLE [Purchasing].[Vendor];

SELECT * INTO [Purchasing].[Vendor] FROM [AdventureWorks2022].[Purchasing].[Vendor]