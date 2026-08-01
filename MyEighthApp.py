import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("📊 Визуализация данных с Pandas")

# Генерируем данные
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=90, freq='D')
df = pd.DataFrame({
    'Дата': dates,
    'Продажи': np.random.randint(100, 500, 90),
    'Расходы': np.random.randint(50, 300, 90),
    'Категория': np.random.choice(['A', 'B', 'C'], 90),
    'Регион': np.random.choice(['Север', 'Юг'], 90)
})

# Боковая панель с настройками
with st.sidebar:
    st.header("Настройки визуализации")
    
    chart_type = st.selectbox(
        "Выберите тип графика",
        ["Линейный", "Столбчатый", "Гистограмма", "Ящик с усами", "Точечный"]
    )
    
    # Выбор колонок для графиков
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    
    if chart_type in ["Линейный", "Столбчатый", "Ящик с усами"]:
        y_col = st.selectbox("Колонка для оси Y", numeric_cols, index=0)
    
    elif chart_type == "Точечный":
        x_col = st.selectbox("Ось X", numeric_cols, index=0)
        y_col = st.selectbox("Ось Y", numeric_cols, index=1 if len(numeric_cols) > 1 else 0)
    
    # Дополнительные параметры
    show_grid = st.checkbox("Показать сетку", value=True)
    figsize_x = st.slider("Ширина графика", 6, 16, 10)
    figsize_y = st.slider("Высота графика", 4, 10, 6)

# Основной контент
st.subheader("📋 Данные")
st.dataframe(df.head(10))

st.subheader("📈 График")

# Строим график в зависимости от выбора
fig, ax = plt.subplots(figsize=(figsize_x, figsize_y))

if chart_type == "Линейный":
    df.set_index('Дата')[y_col].plot(ax=ax, linewidth=2, marker='o', markersize=4)
    ax.set_title(f"Динамика {y_col}")
    ax.set_xlabel("Дата")
    ax.set_ylabel(y_col)

elif chart_type == "Столбчатый":
    # Группируем по категориям для столбчатой диаграммы
    grouped = df.groupby('Категория')[y_col].mean()
    grouped.plot.bar(ax=ax, rot=0)
    ax.set_title(f"Средний {y_col} по категориям")
    ax.set_ylabel(y_col)

elif chart_type == "Гистограмма":
    df[y_col].plot.hist(ax=ax, bins=20, edgecolor='black', alpha=0.7)
    ax.set_title(f"Распределение {y_col}")
    ax.set_xlabel(y_col)
    ax.set_ylabel("Частота")

elif chart_type == "Ящик с усами":
    df.boxplot(column=numeric_cols, ax=ax)
    ax.set_title("Распределение числовых переменных")

elif chart_type == "Точечный":
    df.plot.scatter(x=x_col, y=y_col, ax=ax, alpha=0.6, s=50)
    ax.set_title(f"Зависимость {y_col} от {x_col}")

# Сетка
if show_grid:
    ax.grid(True, alpha=0.3)

st.pyplot(fig)

# Дополнительная статистика
with st.expander("📊 Статистика по данным"):
    st.write(df[numeric_cols].describe())
    
    # Корреляционная матрица
    st.subheader("Корреляция")
    corr = df[numeric_cols].corr()
    st.dataframe(corr.style.background_gradient(cmap='coolwarm'))

"""
В Pandas графики строятся через метод .plot(). 
Он использует Matplotlib под капотом, но с минимальным кодом.
"""

"""
import pandas as pd
import matplotlib.pyplot as plt

df.plot()           # Самый простой график
plt.show()          # Показываем (в Jupyter)
"""

"""
fig, ax = plt.subplots()
df.plot(ax=ax)      # Передаем оси
st.pyplot(fig)
"""

"""
1. Линейный график — .plot() или .plot.line()

import pandas as pd
import numpy as np

# Генерируем данные
dates = pd.date_range('2024-01-01', periods=30, freq='D')
df = pd.DataFrame({
    'Дата': dates,
    'Продажи': np.random.randint(100, 500, 30),
    'Расходы': np.random.randint(50, 300, 30)
})

# Линейный график
df.set_index('Дата').plot() ИЛИ
Расширенные настройки:
df.set_index('Дата').plot(
    figsize=(12, 6),
    title='Динамика продаж и расходов',
    grid=True,
    style=['b-o', 'r--s'],  # b=синий, o=круги, r=красный, --=пунктир
    linewidth=2,
    alpha=0.7
)
plt.xlabel('Дата')
plt.ylabel('Тыс. руб')
plt.legend(['Продажи', 'Расходы'])
"""

"""
2. Столбчатая диаграмма — .plot.bar()

df_cat = pd.DataFrame({
    'Категория': ['A', 'B', 'C', 'D'],
    'Значение': [25, 40, 35, 20]
})

# Вертикальные столбцы
df_cat.plot.bar(x='Категория', y='Значение', legend=False)

# Горизонтальные столбцы (для длинных названий)
df_cat.plot.barh(x='Категория', y='Значение', legend=False)

# Группированные столбцы
df_cat2 = pd.DataFrame({
    'Категория': ['A', 'B', 'C'],
    'Продажи': [100, 150, 120],
    'Расходы': [80, 90, 70]
})
df_cat2.plot.bar(x='Категория', rot=0)  # rot=0 — горизонтальные подписи
"""

"""
3. Круговая диаграмма — .plot.pie()

Для долей и процентов.
df_pie = pd.DataFrame({
    'Продукт': ['Телефоны', 'Ноутбуки', 'Планшеты', 'Аксессуары'],
    'Доля': [45, 30, 15, 10]
})

df_pie.plot.pie(
    y='Доля',
    labels=df_pie['Продукт'],
    autopct='%1.1f%%',  # Проценты с одним знаком
    figsize=(8, 8)
)
"""

"""
4. Гистограмма — .plot.hist()

# Одномерная гистограмма
df['Возраст'].plot.hist(bins=20, edgecolor='black')

# Несколько гистограмм на одном графике
df = pd.DataFrame({
    'A': np.random.normal(0, 1, 1000),
    'B': np.random.normal(2, 1.5, 1000),
    'C': np.random.normal(-1, 0.8, 1000)
})
df.plot.hist(bins=30, alpha=0.5)
"""

"""
5. Ящик с усами (Box Plot) — .plot.box()

Для поиска выбросов и распределения.

df = pd.DataFrame({
    'Группа A': np.random.normal(0, 1, 100),
    'Группа B': np.random.normal(2, 1.5, 100),
    'Группа C': np.random.normal(-1, 0.8, 100)
})
df.plot.box()
"""

"""
6. Точечный график (Scatter) — .plot.scatter()

df_scatter = pd.DataFrame({
    'Рост': np.random.normal(175, 10, 100),
    'Вес': np.random.normal(70, 15, 100)
})

df_scatter.plot.scatter(x='Рост', y='Вес', c='red', s=50, alpha=0.6)
"""