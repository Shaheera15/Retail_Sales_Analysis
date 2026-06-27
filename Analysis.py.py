#IMPORTING REQUIRED PACKAGES
import pandas as pd
import matplotlib.pyplot as plt

#Loading Reatail_Sales_Analysis
file = "Retail_Sales_Analysis.xlsx"
xls = pd.ExcelFile(file)
print("Sheets found:", xls.sheet_names)

# Loading sheets
main_df = pd.read_excel(file, sheet_name="Retail_Sales_Analysis.xlsx")
region_df = pd.read_excel(file, sheet_name="Sales_by_Region")
monthly_df = pd.read_excel(file, sheet_name="Monthly_Sales")
product_df = pd.read_excel(file, sheet_name="Product_Sales")
rank_df = pd.read_excel(file, sheet_name="Highest_to_Lowest_Sales")


#Cleaning column names
def clean(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    return df
main_df = clean(main_df)
region_df = clean(region_df)
monthly_df = clean(monthly_df)
product_df = clean(product_df)
rank_df = clean(rank_df)

# MAIN DATA ANALYSIS
print("\nTOTAL SALES (MAIN DATA):", main_df['sales'].sum())

# VALIDATION (EXCEL vs PYTHON)
if 'sales' in rank_df.columns:
    print("TOTAL SALES (EXCEL PIVOT):", rank_df['sales'].sum())

# REGION ANALYSIS
print("\nREGION SALES:")
print(region_df.sort_values('sum_of_sales', ascending=False))

region_df.sort_values('sum_of_sales').plot(
    kind='barh', x='row_labels', y='sum_of_sales'
)
plt.title("Sales by Region")
plt.savefig("Region_Sales.png")
plt.show()


#MONTHLY SALES TREND
monthly_df.columns = monthly_df.columns.str.lower()
print("\nMONTHLY SALES:")
print(monthly_df)
monthly_df.plot(kind='line', x='row_labels', y='sum_of_sales', marker='o')
plt.title("Monthly Sales Trend")
plt.xticks(rotation=45)
plt.savefig("Monthly_Sales.png")
plt.show()

#PRODUCT ANALYSIS
product_df.columns = product_df.columns.str.lower()
top10 = product_df.sort_values('sum_of_sales', ascending=False).head(10)
print("\nTOP 10 PRODUCTS:")
print(top10)
top10.plot(kind='barh', x='row_labels', y='sum_of_sales')
plt.title("Top 10 Products by Sales")
plt.gca().invert_yaxis()
plt.savefig("Top_Products.png")
plt.show()

# BUSINESS INSIGHTS
print("_____________________________________________")

print("             RETAIL SALES INSIGHTS           ")
clean_region = region_df[~region_df['row_labels'].astype(str).str.lower().str.contains('total')]
top_region_row = clean_region.loc[clean_region['sum_of_sales'].idxmax()]

print(f"HIGHEST PERFORMING REGION")
print(f"**Region: {top_region_row['row_labels']}**")
print(f"Total Sales: ${top_region_row['sum_of_sales']:,.2f}\n")

clean_product = product_df[~product_df['row_labels'].astype(str).str.lower().str.contains('total')]
top_product_row = clean_product.loc[clean_product['sum_of_sales'].idxmax()]

print(f"TOP SELLING PRODUCT")
print(f"**Product Name: {top_product_row['row_labels']}**")
print(f"Total Sales: ${top_product_row['sum_of_sales']:,.2f}\n")

clean_monthly = monthly_df[~monthly_df['row_labels'].astype(str).str.lower().str.contains('total')]
clean_monthly = clean_monthly[clean_monthly['row_labels'].str.len() == 3] 
top_month_row = clean_monthly.loc[clean_monthly['sum_of_sales'].idxmax()]

print(f"PEAK SALES MONTH")
print(f"**Month: {top_month_row['row_labels']}**")
print(f"Total Sales: ${top_month_row['sum_of_sales']:,.2f}")

print("__________________________________________________")
