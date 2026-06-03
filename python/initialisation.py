import pandas as pd

# 1. quarterly_targets
targets_data = {
    "region": ["Europe","Europe","Europe","Europe","USA","USA","USA","USA","Asia","Asia","Asia","Asia"],
    "quarter": ["Q1 2026","Q2 2026","Q3 2026","Q4 2026","Q1 2026","Q2 2026","Q3 2026","Q4 2026","Q1 2026","Q2 2026","Q3 2026","Q4 2026"],
    "target_sales_usd": [750000,820000,900000,950000,1200000,1350000,1450000,1600000,950000,1020000,1100000,1250000],
    "target_profit_usd": [150000,165000,180000,190000,240000,270000,290000,320000,190000,205000,220000,250000],
    "target_customer_growth_pct": [5.0,4.5,5.0,6.0,4.0,5.5,5.0,6.5,6.0,7.0,7.5,8.0]
}
df_targets = pd.DataFrame(targets_data)
df_targets.to_excel("quarterly_targets.xlsx", sheet_name="Targets", index=False)

# 2. product_catalog
catalog_data = {
    "product_id": range(1,21),
    "product_name": ["Camembert","Heineken Beer","Spaghetti","Jamón Ibérico","Earl Grey Tea","Chardonnay","Brake Pads","Leather Wallet","Olive Oil","Smoked Salmon","4K TV 55\"","Smart Speaker","Cotton T-Shirt","SSD 1TB","Rice Cooker","Palm Oil","Car Battery","Smartphone","Software License","Refrigerator"],
    "category": ["Dairy","Beverage","Pasta","Meat","Beverage","Wine","Auto","Accessory","Grocery","Seafood","Electronics","Electronics","Apparel","Computer","Home","Commodity","Auto","Electronics","IT","Home"],
    "unit_price_usd": [5.99,2.50,1.80,45.00,4.20,12.00,35.00,29.99,15.00,22.50,599.99,49.99,12.99,89.99,45.00,35.00,120.00,399.99,299.99,799.99],
    "supplier_name": ["Fromages de France","Bayerische Brauerei","Pasta Italia SRL","Iberico Ham Suppliers","Tea & Biscuits UK","Vins de Bourgogne","TechParts USA","Fashion Forward","Midwest Foods","Petronas Chemicals","Sony Electronics","Alibaba Group","Tata Industries","Samsung Global","VinGroup","Petronas Chemicals","Toyota Auto Parts","Huawei Tech","Infosys Services","LG Electronics"],
    "stock_qty": [450,1200,800,120,350,280,600,400,320,150,85,700,1500,220,180,550,95,200,5000,45],
    "reorder_level": [50,200,100,20,50,30,80,60,40,25,10,100,200,30,20,100,15,25,500,5]
}
df_catalog = pd.DataFrame(catalog_data)
df_catalog.to_excel("product_catalog.xlsx", sheet_name="Products", index=False)

# 3. marketing_budget
budget_data = {
    "region": ["Europe","Europe","Europe","USA","USA","USA","Asia","Asia","Asia","Europe","Europe","Europe","USA","USA","USA","Asia","Asia","Asia","Global","Global"],
    "month": ["2026-01","2026-02","2026-03","2026-01","2026-02","2026-03","2026-01","2026-02","2026-03","2026-04","2026-05","2026-06","2026-04","2026-05","2026-06","2026-04","2026-05","2026-06","2026-07","2026-08"],
    "campaign_name": ["Winter Sale","Valentine Special","Spring Launch","New Year Promo","Super Bowl Ad","Spring Break","Lunar New Year","Valentine Tech","Cherry Blossom Campaign","Easter Deals","Summer Prep","Summer Solstice","Tax Day Relief","Memorial Day","Father's Day","Songkran Festival","Golden Week","Mid-Year Sale","Summer Mega Sale","Back to School"],
    "budget_usd": [15000,12000,18000,25000,40000,22000,30000,16000,20000,14000,19000,21000,15000,28000,26000,23000,35000,27000,50000,42000],
    "spend_usd": [14500,11800,17900,24800,40000,21500,29500,15800,19800,13800,18900,20800,14800,27800,25700,22800,34800,26800,49500,41800],
    "impressions": [850000,720000,1100000,1500000,2500000,1300000,1800000,950000,1200000,800000,1150000,1250000,900000,1700000,1550000,1400000,2100000,1600000,3000000,2500000],
    "clicks": [42000,38000,55000,75000,125000,65000,90000,48000,60000,40000,58000,63000,45000,85000,78000,70000,105000,80000,150000,125000],
    "conversions": [2100,1950,2750,3800,6200,3250,4500,2400,3000,2000,2900,3150,2250,4250,3900,3500,5200,4000,7500,6200]
}
df_budget = pd.DataFrame(budget_data)
df_budget.to_excel("marketing_budget.xlsx", sheet_name="Budget", index=False)

print("Fichiers Excel générés avec succès.")