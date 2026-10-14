import streamlit as st
import pandas as pd

st.title("🛡️ Мониторинг госзакупок: Анализ аномалий")
st.write("Добро пожаловать в MVP-систему для анализа контрактов и поиска рисков!")

# Загрузка файла прямо в браузере
uploaded_file = st.file_uploader("Загрузите ваш Excel-файл с договорами (.xlsx)", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    
    st.success(f"Файл успешно загружен! Всего строк: {len(df)}")
    
    # Показываем первые строчки
    st.subheader("📋 Первые строки данных")
    st.dataframe(df.head(10))
    
    # Простая статистика
    if 'Сумма' in df.columns:
        st.subheader("📊 Общая статистика")
        total_sum = df['Сумма'].sum()
        st.metric(label="Общая сумма контрактов", value=f"{total_sum:,.2f} тенге")
else:
    st.info("Пожалуйста, загрузите файл с договорами, чтобы начать анализ.")
