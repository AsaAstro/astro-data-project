import pandas as pd
import matplotlib.pyplot as plt

# باز کردن فایل
df = pd.read_csv(r"C:\Users\LENOVO\Desktop\ASTRO\gaia_1000.csv")

# === نمودار ۱: موقعیت ستاره‌ها توی آسمون ===
plt.figure(figsize=(8, 6))
plt.scatter(df["ra"], df["dec"], s=1, c="blue")
plt.xlabel("Right Ascension (deg)")
plt.ylabel("Declination (deg)")
plt.title("Gaia Stars - Sky Position")
plt.grid(True, alpha=0.3)
plt.savefig("plot_sky.png", dpi=150)
plt.show()

print("نمودار ۱ ذخیره شد!")

# === نمودار ۲: رنگ و روشنایی ستاره‌ها ===
plt.figure(figsize=(8, 6))
plt.scatter(df["bp_rp"], df["phot_g_mean_mag"], s=1, c="red")
plt.xlabel("BP - RP (Color)")
plt.ylabel("G Magnitude (Brightness)")
plt.title("Gaia Stars - Color vs Brightness")
plt.grid(True, alpha=0.3)
plt.gca().invert_yaxis()
plt.savefig("plot_color.png", dpi=150)
plt.show()

print("نمودار ۲ ذخیره شد!")