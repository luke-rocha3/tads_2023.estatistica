import  streamlit as st
import yfinance as yf
import plotly.graph_objects as go

# Título do app
st.title("stock history app")
# streamlit run /workspaces/tads_2023.estatistica/main.py --server.enableCORS false --server.enableXsrfProtection false

st.sidebar.title("selecione o stock")
ticker_symbol = st.sidebar.text_input("stock", "AAPL", max_chars=10)

# Baixando os dados do yahoo finanças
data = yf.download(ticker_symbol, start="2020-01-01", end = "2023-06-26")

#Exibir os dados
st.subheader("histórico")
st.dataframe(data)

# exbir o gráfico
fig = go.Figure()
fig.add_trace(go.Scatter(x=data.index, y = data["Close"], name = "fechamento"))
fig.update_layout(title = f"{ticker_symbol}", xaxis_title = "Data", yaxis_title = "preço")
st.plotly_chart(fig)
