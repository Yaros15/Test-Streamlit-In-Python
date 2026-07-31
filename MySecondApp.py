
import streamlit as st
import pandas as pd
import numpy as np

st.title("Анализ данных")

df = pd.DataFrame(
    {
        "Товар": ["Яблоки", "Бананы", "Апельсины"],
        "Продажи": [150, 200, 120],
        "Цена": [80, 60, 100]
    }
)

# Делим экран: 2/3 под график, 1/3 под таблицу
col_graph, col_table = st.columns([2, 1])

with col_graph: # Конструкция "with" говорит: всё, что внутри — в эту колонку
    st.subheader("📊 График продаж")
    st.bar_chart(df.set_index("Товар")["Продажи"])  # Встроенный барчарт

with col_table:
    st.subheader("📋 Данные")
    st.dataframe(df)  # Интерактивная таблица

st.header("Дэшборд в 3 колонки")  
# Создаем 3 колонки
c1, c2, c3 = st.columns(3)

# В первой — ползунок
with c1:
    st.subheader("Настройка")
    freq = st.slider("Частота", 1, 10, 3)
    amp = st.slider("Амплитуда", 1, 10, 2)

# Во второй — кнопка
with c2:
    st.subheader("Управление")
    if st.button("🔄 Обновить"):
        st.success("Обновлено!")
    show_grid = st.checkbox("Показать сетку")

# В третьей — информация
with c3:
    st.subheader("Статистика")
    st.metric("Частота", freq)
    st.metric("Амплитуда", amp)
