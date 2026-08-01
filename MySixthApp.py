import streamlit as st
import pandas as pd
import numpy as np
import time

st.title("⚡ Магия кеширования")

# Функция БЕЗ кеша
def load_data_no_cache():
    time.sleep(2)  # Имитация загрузки
    return pd.DataFrame(
        np.random.randn(1000, 5),
        columns=[f"Col_{i}" for i in range(5)]
    )

# Функция С кешем
# Загрузится 1 раз или с параметром ttl(время жизни кеша) - @st.cache_data(ttl=3600) - Кеш живет 1 час
@st.cache_data 
def load_data_with_cache():
    time.sleep(2)  # Будет выполнена 1 раз
    return pd.DataFrame(
        np.random.randn(1000, 5),
        columns=[f"Col_{i}" for i in range(5)]
    )

# Виджет-триггер
st.sidebar.header("Управление")
use_cache = st.sidebar.checkbox("Использовать кеш", value=True)
count = st.sidebar.slider("Количество перезагрузок", 1, 10, 3)

# Замеряем время
import time as time_module

for i in range(count):
    start = time_module.time()
    
    if use_cache:
        df = load_data_with_cache()
    else:
        df = load_data_no_cache()
    
    elapsed = time_module.time() - start
    st.write(f"Загрузка #{i+1}: {elapsed:.2f} сек")

st.dataframe(df.head())
"""
@st.cache_data
def load_data(file_path, use_cache=True):
    # Если use_cache меняется, кеш не пересоздается
    return pd.read_csv(file_path)
"""

"""
Очистка кеша вручную
if st.button("Очистить кеш"):
    st.cache_data.clear()
    st.success("Кеш очищен!")
"""