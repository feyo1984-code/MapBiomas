# Classificação do Uso e Ocupação do Solo por Município Operado pela Sabesp

Este projeto utiliza Streamlit para visualizar a classificação do uso e ocupação do solo por município operado pela Sabesp. Os dados são carregados de dados e arquivos vetoriais e exibidos em um gráfico de pizza interativo.

## Requisitos

Certifique-se de ter os seguintes pacotes instalados:

- streamlit
- pandas
- plotly
- openpyxl

Abra contas (gratuitas para este volume de publicação):
- Git HUB;
- Streamlit

Você pode instalar todos os pacotes necessários usando o seguinte comando:

- !pip install streamlit
- !pip install pandas
- !pip install plotly
- !pip install openpyxl

Passos:
Faça o clone do repositório no Git HUB para submeter os arquivos necessários para fazer o deploy da aplicação, a planilha com as classificações dos Muniípios, a lista de requirements.txt (pacotes), o arquivo escrito em Python necessário para criar um lista suspensa para seleção das labels dos municípios e gerar os gráficos 

Para toda alteração dos arquivos no desktop será necessário um Commit para atualização dos dados no Git HUB

Execute o script Streamlit no seu terminal bash com: streamlit run app.py


Estrutura do Projeto

Arquivos vetoriais e de dados contendo os dados de uso e ocupação do solo.

app.py: Script principal que carrega os dados, processa e exibe o gráfico de pizza.

Funcionalidades:

- Carrega dados de uma base de dados.
- Preenche as classificações vazias com "0".
- Exibe uma lista suspensa para selecionar o município.
- Gera um gráfico de pizza interativo mostrando a classificação do uso e ocupação do solo.
- Exibe as áreas por classe como uma lista.

Exemplo de Uso

Selecione um município na lista suspensa.

Veja o gráfico de pizza atualizado com os dados do município selecionado.


Extração de Dados da Coleção 8 do MapBiomas

Este projeto também inclui uma aplicação para extração de dados da Coleção 8 do MapBiomas usando o Google Earth Engine (GEE). A Coleção 8 do MapBiomas fornece mapas anuais de cobertura e uso da terra no Brasil entre 1985 e 2023.

https://ee-feyo1984.projects.earthengine.app/view/mapbiomas

Execute o Script de Extração: Utilize o script fornecido pelo MapBiomas para extrair os dados desejados. O script pode ser encontrado no repositório do MapBiomas no GEE.
Exemplo de Script

Recursos Adicionais
Documentação Oficial do MapBiomas: Acesse a documentação oficial para tutoriais e exemplos de uso.

Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.


Este README atualizado inclui uma seção sobre a aplicação de extração de dados da Coleção 8 do MapBiomas usando o Google Earth Engine, com instruções detalhadas e um exemplo de script. Se precisar de mais alguma coisa, estou aqui para ajudar!
