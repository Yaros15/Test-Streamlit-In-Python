import streamlit as st
import pandas as pd
import numpy as np

st.title("📊 Анализ данных с Pandas")

# Генерируем тестовые данные
np.random.seed(42)
df = pd.DataFrame({
    "Дата": pd.date_range('2024-01-01', periods=100, freq='D'),
    "Продажи": np.random.randint(100, 500, 100),
    "Категория": np.random.choice(["A", "B", "C"], 100),
    "Регион": np.random.choice(["Север", "Юг", "Восток", "Запад"], 100)
})

st.subheader("1. Исходные данные")
st.dataframe(df.head(10))

st.subheader("2. Базовый анализ")

col1, col2, col3 = st.columns(3)
col1.metric("Всего строк", df.shape[0])
col2.metric("Всего колонок", df.shape[1])
col3.metric("Средние продажи", f"{df['Продажи'].mean():.0f}")

st.subheader("3. Группировка по категориям")
grouped = df.groupby("Категория").agg({
    "Продажи": ["mean", "sum", "count"]
})
st.dataframe(grouped)

st.subheader("4. Фильтрация в реальном времени")

# Интерактивные фильтры
col1, col2 = st.columns(2)
with col1:
    category_filter = st.multiselect(
        "Категории",
        df["Категория"].unique(),
        default=df["Категория"].unique()
    )
with col2:
    min_sales, max_sales = st.slider(
        "Диапазон продаж",
        int(df["Продажи"].min()),
        int(df["Продажи"].max()),
        (100, 400)
    )

# Применяем фильтры
filtered_df = df[
    (df["Категория"].isin(category_filter)) &
    (df["Продажи"] >= min_sales) &
    (df["Продажи"] <= max_sales)
]

st.write(f"Найдено записей: {len(filtered_df)}")
st.dataframe(filtered_df)

st.subheader("5. Сводная таблица (Pivot Table)")
pivot = df.pivot_table(
    values="Продажи",
    index="Категория",
    columns="Регион",
    aggfunc="mean",
    fill_value=0
)
st.dataframe(pivot)

# Скачивание обработанных данных
csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button(
    "📥 Скачать отфильтрованные данные",
    csv,
    "filtered_data.csv",
    "text/csv"
)

# Топ-15 методов Pandas для работы с данными

"""
1. Базовое знакомство с данными:

df.head()          # Первые 5 строк (как взгляд в таблицу)
df.tail(3)         # Последние 3 строки
df.info()          # Типы данных и количество непустых значений
df.describe()      # Статистика: среднее, медиана, мин, макс
df.shape           # (строки, колонки) — размер таблицы
df.columns         # Список названий колонок
df.dtypes          # Типы каждой колонки
"""

"""
2. Выборка данных:

# Выбор колонки (получаем Series)
df["Имя"]                    # Одна колонка
df[["Имя", "Зарплата"]]      # Несколько колонок

# Выбор строк по индексу
df.iloc[0]                   # Первая строка (по номеру)
df.iloc[1:3]                 # Строки 1-2 (как в Python)

# Выбор строк по условию (самое мощное!)
df[df["Возраст"] > 28]                       # Все старше 28
df[(df["Возраст"] > 25) & (df["Город"] == "Москва")]  # И то, и то
df[df["Город"].isin(["Москва", "СПб"])]     # Города из списка
"""

"""
3. Фильтрация:

# Фильтруем через query (читается как SQL)
df.query("Возраст > 25 and Город == 'Москва'")

# Строки с пропусками
df[df["Зарплата"].isna()]    # Где зарплата не указана
df[df["Зарплата"].notna()]   # Где зарплата указана
"""

"""
4. Сортировка

df.sort_values("Возраст")                    # По возрасту (по возрастанию)
df.sort_values("Зарплата", ascending=False)  # По убыванию зарплаты
df.sort_values(["Город", "Возраст"])         # По городу, внутри по возрасту
"""

"""
5. Агрегация и группировка (как сводные таблицы)

# Простая статистика по всей таблице
df["Зарплата"].mean()        # Средняя зарплата
df["Возраст"].max()          # Максимальный возраст
df["Зарплата"].sum()         # Сумма зарплат

# Группировка (как сводная таблица в Excel)
df.groupby("Город")["Зарплата"].mean()        # Средняя зарплата по городам
df.groupby("Город")["Возраст"].agg(["min", "max", "mean"])  # Разная статистика
df.groupby("Город").agg({                     # Свои агрегации
    "Зарплата": "mean",
    "Возраст": ["min", "max"]
})
"""

"""
6. Создание новых колонок:

# Простое присвоение
df["Бонус"] = df["Зарплата"] * 0.1           # 10% бонус

# Через apply (сложные вычисления)
df["Уровень"] = df["Зарплата"].apply(
    lambda x: "Высокий" if x > 90000 else "Средний"
)

# Условное присвоение (как если в Excel)
df.loc[df["Возраст"] > 30, "Категория"] = "Взрослый"
df.loc[df["Возраст"] <= 30, "Категория"] = "Молодой"
"""

"""
7. Работа с пропусками

df.isnull().sum()              # Количество пропусков в каждой колонке
df.dropna()                    # Удалить строки с любыми пропусками
df.fillna(0)                   # Заменить пропуски на 0
df.fillna(df.mean())           # Заменить на среднее значение
"""

"""
8. Объединение таблиц (как VLOOKUP)

# Две таблицы
df1 = pd.DataFrame({"ID": [1, 2, 3], "Имя": ["Анна", "Петр", "Мария"]})
df2 = pd.DataFrame({"ID": [1, 2, 4], "Зарплата": [80000, 95000, 70000]})

# Левое соединение (как VLOOKUP)
merged = pd.merge(df1, df2, on="ID", how="left")  # Все из левой + зарплаты

# Внутреннее (только пересечение)
merged = pd.merge(df1, df2, on="ID", how="inner")
"""

"""
цепочки методов (method chaining)

result = (df
    .query("Возраст > 25")
    .groupby("Город")
    .agg({"Зарплата": "mean"})
    .sort_values("Зарплата", ascending=False)
    .reset_index()
)
"""

"""
Шпаргалка по типам данных

# Преобразование типов
df["Возраст"] = df["Возраст"].astype("int64")
df["Дата"] = pd.to_datetime(df["Дата"])
df["Категория"] = df["Категория"].astype("category")  # Экономит память
"""