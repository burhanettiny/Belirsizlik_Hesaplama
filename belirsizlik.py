import numpy as np 
import streamlit as st
import matplotlib.pyplot as plt

def calculate_average(measurements):
    return np.mean(measurements) if measurements else float('nan')

def calculate_standard_uncertainty(measurements):
    return (np.std(measurements, ddof=1) / np.sqrt(len(measurements))) if len(measurements) > 1 else float('nan')

def calculate_repeatability(measurements):
    return np.std(measurements, ddof=1) if len(measurements) > 1 else float('nan')

def plot_error_bars(days, averages, uncertainties):
    # Hata barları ile grafik çizme
    plt.figure(figsize=(10, 6))
    plt.errorbar(days, averages, yerr=uncertainties, fmt='o', capsize=5, color='b', label='Ortalama ve Belirsizlik')
    plt.title('Ortalama ve Hata Barları')
    plt.xlabel('Günler')
    plt.ylabel('Değerler')
    plt.grid(True)
    plt.legend()

    # Streamlit'te gösterim
    st.pyplot(plt)

def main():
    st.title("Belirsizlik Hesaplama; Developed by Burhanettin")
    days = ['1. Gün', '2. Gün', '3. Gün']
    total_measurements = []
    uncertainty_components = []
    
    for day in days:
        st.subheader(f"{day} İçin Ölçüm Sonuçlarını Girin")
        measurements = []
        for i in range(5):
     
