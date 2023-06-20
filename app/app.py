import streamlit as st
import psycopg2

# Conecta ao banco de dados PostgreSQL
conn = psycopg2.connect(
    host="postgres_db", database="postgres", user="postgres", password="postgres"
)


# Função para executar uma consulta SQL
def execute_query(query):
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows


# Consulta o banco de dados e exibe os resultados
def display_data():
    query = "SELECT * FROM public.challenge"
    rows = execute_query(query)

    if len(rows) > 0:
        st.table(rows)
    else:
        st.write("Nenhum dado encontrado.")


# Configurações da aplicação Streamlit
def main():
    st.title("Consulta de dados - Desafio")
    st.write("Exibindo os dados da tabela 'challenge'")

    display_data()


# Executa a aplicação
if __name__ == "__main__":
    main()
