
import streamlit as st
import pandas as pd
import numpy as np

# Виджет возвращает значение, которое ты сохраняешь в переменную

# st.button() — кнопка (возвращает True/False)
if st.button("🚀 Нажми меня!"):
    st.balloons()  # Эффект! 
    st.success("Кнопка нажата!")
else:
    st.info("Нажми кнопку выше")

# st.slider() — ползунок (возвращает число)
# Целое число
age = st.slider("Ваш возраст", 0, 100, 25)
st.write(f"Вам {age} лет")

# Число с плавающей точкой
temp = st.slider("Температура", -10.0, 40.0, 20.0, step=0.5)
st.write(f"Температура: {temp}°C")

# Диапазон (два ползунка!)
range_val = st.slider("Выберите диапазон", 0.0, 100.0, (25.0, 75.0))
st.write(f"От {range_val[0]} до {range_val[1]}")

# st.selectbox() — выпадающий список (возвращает выбранное)
city = st.selectbox(
    "Выберите город",
    ["Москва", "Санкт-Петербург", "Казань", "Новосибирск"],
    index=1  # По умолчанию выбран СПб (индекс 1)
)
st.write(f"Вы выбрали: {city}")

# С индексами
options = ["Красный", "Зеленый", "Синий"]
color = st.selectbox("Цвет", options, index=2)  # По умолчанию Синий

# st.multiselect() — множественный выбор (возвращает список)
colors = st.multiselect(
    "Выберите любимые цвета",
    ["Красный", "Зеленый", "Синий", "Желтый"],
    default=["Зеленый", "Синий"]  # По умолчанию выбраны
)
st.write(f"Ваши цвета: {', '.join(colors) if colors else 'не выбраны'}")

# st.checkbox() — галочка (возвращает True/False)
show_data = st.checkbox("Показать данные")
if show_data:
    st.dataframe(pd.DataFrame({"A": [1,2,3], "B": [4,5,6]}))
else:
    st.write("Поставьте галочку, чтобы увидеть данные")

# st.radio() — радиокнопки (возвращает выбранное)
option = st.radio(
    "Выберите способ оплаты",
    ["Карта", "Наличные", "Криптовалюта"],
    index=0  # По умолчанию выбрана карта
)
st.write(f"Вы выбрали: {option}")

# st.text_input() — текстовое поле (возвращает строку)
name = st.text_input("Введите ваше имя", value="Анна")
if name:
    st.write(f"Привет, {name}!")
    
# Пароль с маскировкой
password = st.text_input("Пароль", type="password")
