import numpy as np
import streamlit as st

def calculate_average(measurements):
    return np.mean(measurements) if measurements else float('nan')

def calculate_standard_uncertainty(measurements):
    return (np.std(measurements, ddof=1) / np.sqrt(len(measurements))) if len(measurements) > 1 else float('nan')

def main():
    st.title("Ölçüm Analiz Uygulaması")
    days = ['1. Gün', '2. Gün', '3. Gün']
    total_measurements = []
    
    for day in days:
        st.subheader(f"{day} İçin Ölçümleri Girin")
        measurements = []
        for i in range(5):
            value = st.number_input(f"{day} - Tekrar {i+1}", value=None, step=0.01, format="%.2f", key=f"{day}_{i}")
            if value is not None:
                measurements.append(value)
        total_measurements.append(measurements)
    
    if st.button("Sonuçları Hesapla"):
        for i, day in enumerate(days):
            avg = calculate_average(total_measurements[i])
            uncertainty = calculate_standard_uncertainty(total_measurements[i])
            st.write(f"{day} - Ortalama: {avg:.4f}, Belirsizlik: {uncertainty:.4f}")
        
        overall_measurements = [value for day in total_measurements for value in day]
        overall_avg = calculate_average(overall_measurements)
        overall_uncertainty = calculate_standard_uncertainty(overall_measurements)
        st.write(f"Genel Ortalama: {overall_avg:.4f}, Genel Belirsizlik: {overall_uncertainty:.4f}")

if __name__ == "__main__":
    main()
