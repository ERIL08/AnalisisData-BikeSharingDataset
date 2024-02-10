import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


st.set_option('deprecation.showPyplotGlobalUse', False)
# Menampilkan data
st.write("# Proyek Analisis Data: Bike Sharing Dataset")
st.write("- Kelompok: IF-3 Seaborn")
st.write("- Anggota:")
st.write("  - 10122112 - MOHAMAD SYERIL AKBAR")
st.write("  - 10122103 - MUHAMMAD FIQIH RAMANANDA")
st.write("  - 10122499 - JINAN MUMTAZ")
st.write("  - 10122496 - MUHAMMAD WILDAN")
st.write("  - 10122101 - LIDAN WISNU SAPUTRA")

# Load data
day_data = pd.read_csv('Bike-sharing-dataset/day.csv')
hour_data = pd.read_csv('Bike-sharing-dataset/hour.csv')

# Menampilkan data
st.write("## Menentukan Pertanyaan Bisnis")
st.write("- 1. Berapakah Perbandingan dari pengguna sepeda Casual dan Register?")
st.write("- 2. Menghitung kecepatan angin pada tanggal (1/1/2011 hingga 3/1/2011) serta buat gambarannya")
st.write("- 3. Analisis berapa banyak pendaftar, casual, dan jumlah serta buat visualisasi plot dari tanggal (1/1/2011 hingga 3/1/2011)")
st.write("- 4. Berapa suhu penggunaan sepeda tertinggi dan di suhu berapakah yang paling banyak?")
st.write("- 5. Menganalisis kondisi humidity (kelembapan) dan temp (temperature) pada tanggal")

# Menampilkan data
st.write("## Menyiapkan semua library yang dibuthkan")
st.write("Library sudah diimpor.")

# Menampilkan data
st.write("## Data Wrangling")
st.write("### Gathering Data")
st.write("Data telah dimuat.")

# Menampilkan data
st.write("### Assessing Data")
st.write("#### Day Data Summary:")
st.write(day_data.describe())
st.write("#### Day Data Missing Values:")
st.write(day_data.isnull().sum())
st.write("#### Hour Data Summary:")
st.write(hour_data.describe())
st.write("#### Hour Data Missing Values:")
st.write(hour_data.isnull().sum())

# Menampilkan data
st.write("## Exploratory Data Analysis (EDA)")

# Menampilkan data
st.write("### Explore ...")
st.write(day_data['dteday'])

# Menampilkan data
st.write(hour_data.head())

# Menampilkan data
st.write("## Visualization & Explanatory Analysis")

# Pertanyaan 1: Berapakah Perbandingan dari pengguna sepeda Casual dan Register
fig_day, ax_day = plt.subplots(figsize=(10, 5))
ax_day.bar(['Casual', 'Registered'], [day_data['casual'].sum(), day_data['registered'].sum()], color=['blue', 'orange'])
ax_day.set_title('Perbandingan Pengguna Sepeda Casual dan Registered (Data Harian)')
ax_day.set_ylabel('Jumlah')
st.pyplot(fig_day)

fig_hour, ax_hour = plt.subplots(figsize=(10, 5))
ax_hour.bar(['Casual', 'Registered'], [hour_data['casual'].sum(), hour_data['registered'].sum()], color=['green', 'red'])
ax_hour.set_title('Perbandingan Pengguna Sepeda Casual dan Registered (Data Jam)')
ax_hour.set_ylabel('Jumlah')
st.pyplot(fig_hour)

# Pertanyaan 2: Menghitung kecepatan angin pada tanggal (1/1/2011 hingga 3/1/2011) serta buat gambarannya
st.write("### Pertanyaan 2: Menghitung kecepatan angin pada tanggal (1/1/2011 hingga 3/1/2011) serta buat gambarannya")
# Konversi 'dteday' ke format datetime
day_data['dteday'] = pd.to_datetime(day_data['dteday'])
# Filter data dari 1/1/2011 hingga 3/1/2011
filtered_data = day_data[(day_data['dteday'] >= '2011-01-01') & (day_data['dteday'] <= '2011-03-01')]
# Hitung rata-rata kecepatan angin
average_windspeed = filtered_data['windspeed'].mean()
st.write(f"Rata-rata Kecepatan Angin (1/1/2011 hingga 3/1/2011): {average_windspeed}")
# Visualisasi kecepatan angin
fig_windspeed, ax_windspeed = plt.subplots(figsize=(12, 6))
ax_windspeed.plot(filtered_data['dteday'], filtered_data['windspeed'], label='Kecepatan Angin', marker='o')
ax_windspeed.axhline(y=average_windspeed, color='r', linestyle='--', label='Rata-rata Kecepatan Angin')
ax_windspeed.set_title('Kecepatan Angin (1/1/2011 hingga 3/1/2011)')
ax_windspeed.set_xlabel('Tanggal')
ax_windspeed.set_ylabel('Kecepatan Angin')
ax_windspeed.legend()
ax_windspeed.grid(True)
st.pyplot(fig_windspeed)

# Pertanyaan 3: Analisis berapa banyak pendaftar, casual, dan jumlah serta buat visualisasi plot dari tanggal (1/1/2011 hingga 3/1/2011)
st.write("### Pertanyaan 3: Analisis berapa banyak pendaftar, casual, dan jumlah serta buat visualisasi plot dari tanggal (1/1/2011 hingga 3/1/2011)")
# Filter data dari 1/1/2011 hingga 3/1/2011
filtered_data = day_data[(day_data['dteday'] >= '2011-01-01') & (day_data['dteday'] <= '2011-03-01')]
# Plotting casual data
fig_casual, ax_casual = plt.subplots(figsize=(12, 6))
ax_casual.plot(filtered_data['dteday'], filtered_data['casual'], label='Casual', marker='o', color='blue')
ax_casual.set_title('Pengguna Sepeda Casual (1/1/2011 hingga 3/1/2011)')
ax_casual.set_xlabel('Tanggal')
ax_casual.set_ylabel('Jumlah Casual')
ax_casual.legend()
ax_casual.grid(True)
st.pyplot(fig_casual)

# Plotting registered data
fig_registered, ax_registered = plt.subplots(figsize=(12, 6))
ax_registered.plot(filtered_data['dteday'], filtered_data['registered'], label='Registered', marker='o', color='green')
ax_registered.set_title('Pengguna Sepeda Registered (1/1/2011 hingga 3/1/2011)')
ax_registered.set_xlabel('Tanggal')
ax_registered.set_ylabel('Jumlah Registered')
ax_registered.legend()
ax_registered.grid(True)
st.pyplot(fig_registered)

# Plotting jumlah total data
fig_total, ax_total = plt.subplots(figsize=(12, 6))
ax_total.plot(filtered_data['dteday'], filtered_data['cnt'], label='Total', marker='o', color='purple')
ax_total.set_title('Total Pengguna Sepeda (1/1/2011 hingga 3/1/2011)')
ax_total.set_xlabel('Tanggal')
ax_total.set_ylabel('Jumlah Total')
ax_total.legend()
ax_total.grid(True)
st.pyplot(fig_total)

# Pertanyaan 4: Berapa suhu penggunaan sepeda tertinggi dan di suhu berapakah yang paling banyak?
st.write("### Pertanyaan 4: Berapa suhu penggunaan sepeda tertinggi dan di suhu berapakah yang paling banyak?")
max_temp = day_data['temp'].max()
mode_temp = day_data['temp'].mode()[0]
st.write(f"Suhu penggunaan sepeda tertinggi: {max_temp}")
st.write(f"Suhu yang paling banyak digunakan: {mode_temp}")

# Melanjutkan dari langkah sebelumnya...

# Pertanyaan 5: Menganalisis kondisi humidity (kelembapan) dan temp (temperature) pada tanggal
st.write("### Pertanyaan 5: Menganalisis kondisi humidity (kelembapan) dan temp (temperature) pada tanggal")
# Filter data pada tanggal tertentu (misalnya 2011-01-01)
specific_date = '2011-01-01'
specific_date_data = day_data[day_data['dteday'] == specific_date]
st.write(f"Data pada tanggal {specific_date}:")
st.write(specific_date_data[['temp', 'hum']])

# Data Mining
# 1. Identifikasi Korelasi antara Variabel
st.write("### Identifikasi Korelasi antara Variabel")
# Menggunakan metode korelasi Pearson
correlation = day_data.corr()
st.write("Korelasi Pearson:")
st.write(correlation)
# Visualisasi matriks korelasi
plt.figure(figsize=(12, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Matriks Korelasi antara Variabel')
st.pyplot()

# 2. Visualisasi Data menggunakan Scatter Plot
st.write("### Visualisasi Data menggunakan Scatter Plot")
# Scatter plot antara 'temp' dan 'cnt' (jumlah total)
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=day_data, x='temp', y='cnt', alpha=0.7, ax=ax1)
ax1.set_title('Scatter Plot: Temperature vs Total Count')
ax1.set_xlabel('Temperature (Celsius)')
ax1.set_ylabel('Total Count')
st.pyplot(fig1)

# Scatter plot antara 'hum' dan 'cnt' (jumlah total)
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=day_data, x='hum', y='cnt', alpha=0.7, ax=ax2)
ax2.set_title('Scatter Plot: Humidity vs Total Count')
ax2.set_xlabel('Humidity')
ax2.set_ylabel('Total Count')
st.pyplot(fig2)

# 3. Analisis Distribusi Variabel
st.write("### Analisis Distribusi Variabel")
# Distribusi variabel 'temp'
fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.histplot(day_data['temp'], bins=30, kde=True, color='blue', ax=ax3)
ax3.set_title('Distribution of Temperature')
ax3.set_xlabel('Temperature (Celsius)')
ax3.set_ylabel('Frequency')
st.pyplot(fig3)

# Distribusi variabel 'hum'
fig4, ax4 = plt.subplots(figsize=(10, 6))
sns.histplot(day_data['hum'], bins=30, kde=True, color='green', ax=ax4)
ax4.set_title('Distribution of Humidity')
ax4.set_xlabel('Humidity')
ax4.set_ylabel('Frequency')
st.pyplot(fig4)

# 4. Analisis Outlier
st.write("### Analisis Outlier")
# Boxplot untuk 'temp'
fig5, ax5 = plt.subplots(figsize=(8, 6))
sns.boxplot(data=day_data, x='temp', color='orange', ax=ax5)
ax5.set_title('Boxplot of Temperature')
ax5.set_xlabel('Temperature (Celsius)')
st.pyplot(fig5)

# Boxplot untuk 'hum'
fig6, ax6 = plt.subplots(figsize=(8, 6))
sns.boxplot(data=day_data, x='hum', color='purple', ax=ax6)
ax6.set_title('Boxplot of Humidity')
ax6.set_xlabel('Humidity')
st.pyplot(fig6)

# Menutup semua plot yang telah digunakan
plt.close(fig1)
plt.close(fig2)
plt.close(fig3)
plt.close(fig4)
plt.close(fig5)
plt.close(fig6)