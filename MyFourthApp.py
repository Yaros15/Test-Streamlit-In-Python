
import streamlit as st
import pandas as pd
import numpy as np

st.title("🏢 Отдел продаж")

# Создаем данные
np.random.seed(42)
df = pd.DataFrame({
    "Менеджер": [f"Сотрудник {i}" for i in range(1, 21)],
    "Продажи": np.random.randint(50, 500, 20),
    "Клиенты": np.random.randint(5, 30, 20),
    "Регион": np.random.choice(["Москва", "СПб", "Казань", "Новосибирск"], 20)
})

st.subheader("📋 Таблица продаж")

st.dataframe( # Кликай по колонкам — сортировка!
    df,
    use_container_width=True, # Адаптивная ширина (растягивается на весь экран)
    height=400
)

# Аналитика на основе таблицы
st.subheader("📊 Аналитика")

col1, col2 = st.columns(2)
with col1:
    top_seller = df.loc[df["Продажи"].idxmax()]
    st.metric("Лучший менеджер", top_seller["Менеджер"], f"{top_seller['Продажи']} продаж")

with col2:
    avg_sales = df["Продажи"].mean()
    st.metric("Средние продажи", f"{avg_sales:.0f}")

# Фильтруем таблицу (показываем только избранных)
st.subheader("🔍 Фильтр: топ-5 по продажам")
top5 = df.nlargest(5, "Продажи")
st.dataframe(top5, use_container_width=True)




st.header("st.table — статичная таблица")
st.table({ # Просто картинка, ничего не нажимается
    "Параметр": ["Скорость", "Ускорение", "Торможение"],
    "Значение": [120, 9.8, 45]
}) 


# Редактируемая таблица!
edited_df = st.data_editor(df, num_rows="dynamic")

st.write("Измененные данные:")
st.dataframe(edited_df)