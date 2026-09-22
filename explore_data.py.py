import pandas as pd

# باز کردن فایل
df = pd.read_csv(r"C:\Users\LENOVO\Desktop\ASTRO\gaia_1000.csv")

# ۵ سطر اول
print("=== ۵ سطر اول ===")
print(df.head())

# اسم ستون‌ها
print("\n=== ستون‌ها ===")
print(df.columns)

# تعداد ستاره‌ها
print("\n=== تعداد ستاره‌ها ===")
print(len(df))