import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# Título da página
st.title("Classificação MapBiomas nos Municípios Operados pela Sabesp")
# Carregar o arquivo Excel
df = pd.read_excel("./classes_area-km_por_municipiosabesp.xlsx")
# Preencher células vazias com zero
df = df.fillna(0)

# Remover espaços extras dos nomes das colunas
df.columns = df.columns.str.strip()

# Lista de classes de uso do solo e suas cores correspondentes
classes_uso = {
    "Formação Florestal": "#006400",
    "Formação Savânica": "#00ff00",
    "Mangue": "#687537",
    "Silvicultura": "#935132",
    "Campo Alagado e Área Pantanosa": "#45c2a5",
    "Formação Campestre": "#b8af4f",
    "Outras Formações não Florestais": "#bdb76b",
    "Pastagem": "#ffd966",
    "Cana": "#c27ba0",
    "Mosaico de Usos": "#fff3bf",
    "Praia, Duna e Areal": "#dd7e6b",
    "Área Urbanizada": "#af2a2a",
    "Outras Áreas não Vegetadas": "#ff99ff",
    "Afloramento Rochoso": "#ff8C00",
    "Mineração": "#8a2be2",
    "Aquicultura": "#29eee4",
    "Apicum": "#968c46",
    "Rio, Lago e Oceano": "#0000ff",
    "Soja": "#c59ff4",
    "Outras Lavouras Temporárias": "#e787f8",
    "Café": "#cca0d4",
    "Citrus": "#d082de",
    "Outras Lavouras Perenes": "#cd49e4",
    "Restinga Arborizada": "#6b9932",
    "Restinga Herbácea": "#66ffcc"
}

# Cria o app Dash
#app = dash.Dash(__name__)

# Layout do Dash
#app.layout = html.Div([
    # Título

    # Lista suspensa para selecionar o município
    # Lista suspensa para selecionar o município
municipio_selecionado = st.selectbox(
    'Selecione o Município',
    options=df['Município'].unique(),
    index=0  # Valor inicial do dropdown
)
    #dcc.Dropdown(
        #id='municipio-dropdown',
        #options=[{'label': municipio, 'value': municipio} for municipio in df['Município'].unique()],
       # value=df['Município'].unique()[0],  # Valor inicial do dropdown
        #style={'width': '50%', 'margin': 'auto'}
    #),

    # Gráfico de pizza
    #dcc.Graph(id='pie-chart'),

    # Exibição das áreas em Km²
    #html.Div(id='area-info', style={'margin-top': '20px', 'textAlign': 'center'})
#])

# Função para atualizar o gráfico e as áreas conforme o município
#@app.callback(
    #[Output('pie-chart', 'figure'),
    # Output('area-info', 'children')],
    #[Input('municipio-dropdown', 'value')]
#)
#def update_graph(municipio_selecionado):
    # Filtra os dados para o município selecionado
    df_filtrado = df[df['Município'] == municipio_selecionado]

    # Garantir que todas as classes de uso estejam presentes no gráfico de pizza
    areas = {classe: df_filtrado[classe].sum() for classe in classes_uso.keys()}

    # Remover classes com área zero
    areas = {classe: area for classe, area in areas.items() if area > 0}

    # Cria o gráfico de pizza com cores personalizadas
    fig = go.Figure(data=[go.Pie(labels=list(areas.keys()), values=list(areas.values()), hole=0.3,
                                 marker=dict(colors=[classes_uso[classe] for classe in areas.keys()]))])

    fig.update_layout(title=f'Distribuição de Áreas por Classe de Uso do Solo - {municipio_selecionado}', title_x=0.5)

    # Criar o texto com as áreas em Km²
    area_text = [f'{classe}: {area:.2f} km²' for classe, area in areas.items()]

    # Exibir as áreas como uma lista no HTML
    # area_info = html.Ul([html.Li(area) for area in area_text])
    #Exibe o gráfico
    st.plotly_chart(fig)

    #return fig, area_info

# Rodar o servidor Dash
#if __name__ == '__main__':
    #app.run_server(debug=True, use_reloader=False)

# Rodar o servidor Dash
if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)
