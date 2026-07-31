
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ===== ЗАГОЛОВОК (в центре) =====
st.title("📊 Анализ продаж")

# ===== САЙДБАР — все настройки здесь =====
st.sidebar.header("⚙️ Настройки")
st.sidebar.subheader("Параметры отчета")

# Ползунок
months = st.sidebar.slider("Количество месяцев", 3, 12, 6)

# Выпадающий список
metric = st.sidebar.selectbox(
    "Что показываем?",
    ["Продажи", "Расходы", "Прибыль"]
)

# Чекбокс
show_grid = st.sidebar.checkbox("Показать сетку на графике")

# Кнопка
if st.sidebar.button("🔄 Обновить данные"):
    st.sidebar.success("Данные обновлены!")

# Разделитель
st.sidebar.divider()
st.sidebar.caption("Версия 1.0")

# ===== ОСНОВНОЙ КОНТЕНТ (в центре) =====
# Генерируем данные в зависимости от ползунка
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=months, freq='MS')
sales = np.random.randint(80, 200, months)
costs = np.random.randint(50, 150, months)
profit = sales - costs

df = pd.DataFrame({
    "Дата": dates,
    "Продажи": sales,
    "Расходы": costs,
    "Прибыль": profit
})

# Показываем данные
st.subheader(f"Данные за {months} месяцев")
st.dataframe(df)

# Строим график выбранной метрики
st.subheader(f"Динамика: {metric}")
fig, ax = plt.subplots(figsize=(10, 5))

if metric == "Продажи":
    ax.plot(df["Дата"], df["Продажи"], 'b-o', linewidth=2, label="Продажи")
elif metric == "Расходы":
    ax.plot(df["Дата"], df["Расходы"], 'r-o', linewidth=2, label="Расходы")
else:
    ax.plot(df["Дата"], df["Прибыль"], 'g-o', linewidth=2, label="Прибыль")

ax.set_xlabel("Дата")
ax.set_ylabel("Тыс. руб")
if show_grid:
    ax.grid(True, alpha=0.3)
ax.legend()
st.pyplot(fig)

# Сводка
st.subheader("📈 Итоги")
col1, col2, col3 = st.columns(3)
col1.metric("Средние продажи", f"{df['Продажи'].mean():.0f}")
col2.metric("Средние расходы", f"{df['Расходы'].mean():.0f}")
col3.metric("Средняя прибыль", f"{df['Прибыль'].mean():.0f}")