


"""
Главное правило работы с БД в Streamlit

# Паттерн, который ты будешь использовать всегда:

@st.cache_data(ttl=3600)  # Кешируем на час
def load_data_from_db():
    conn = get_connection()  # Подключаемся
    df = pd.read_sql("SELECT * FROM table", conn)  # Загружаем
    conn.close()  # Закрываем
    return df

df = load_data_from_db()  # Теперь данные в DataFrame
"""

# Способ 2: через SQLAlchemy (удобнее)
    # engine = create_engine(f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}")
    # df = pd.read_sql_query(query, engine)
    # return df

""""
# В файле .streamlit/secrets.toml
# [database]
# host = "localhost"
# user = "admin"
# password = "supersecret"
# database = "my_db"

import streamlit as st
import psycopg2

@st.cache_resource
def get_connection():
    return psycopg2.connect(
        host=st.secrets["database"]["host"],
        user=st.secrets["database"]["user"],
        password=st.secrets["database"]["password"],
        database=st.secrets["database"]["database"]
    )

@st.cache_data(ttl=300)
def load_data():
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM table", conn)
    conn.close()
    return df
"""    