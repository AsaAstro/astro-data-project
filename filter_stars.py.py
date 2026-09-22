import pandas as pd
import matplotlib.pyplot as plt

# باز کردن فایل
df = pd.read_csv(r"C:\Users\LENOVO\Desktop\ASTRO\gaia_1000.csv")

print("=== تعداد کل ستاره‌ها ===")
print(len(df))

# === فیلتر ۱: فقط ستاره‌های درخشان ===
bright = df[df["phot_g_mean_mag"] < 15]
print("\n=== ستاره‌های درخشان (mag < 15) ===")
print(len(bright))

# === فیلتر ۲: فقط ستاره‌های نزدیک ===
near = df[df["parallax"] > 1]
print("\n=== ستاره‌های نزدیک (parallax > 1) ===")
print(len(near))

# === فیلتر ۳: هر دو شرط با هم ===
bright_near = df[(df["phot_g_mean_mag"] < 15) & (df["parallax"] > 1)]
print("\n=== درخشان و نزدیک با هم ===")
print(len(bright_near))

# === نمودار مقایسه‌ای ===
plt.figure(figsize=(10, 8))

# همه ستاره‌ها (خاکستری کم‌رنگ)
plt.scatter(df["ra"], df["dec"], s=1, c="lightgray", label="All stars")

# ستاره‌های درخشان (زرد)
plt.scatter(bright["ra"], bright["dec"], s=3, c="gold", label="Bright (mag < 15)")

# ستاره‌های نزدیک (آبی)
plt.scatter(near["ra"], near["dec"], s=3, c="blue", label="Near (parallax > 1)")

plt.xlabel("Right Ascension (deg)")
plt.ylabel("Declination (deg)")
plt.title("Gaia Stars - Filtered")
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("plot_filtered.png", dpi=150)
plt.show()

print("\nنمودار فیلترشده ذخیره شد!")