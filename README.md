# Bem vindo ao projeto Tech News!

## Intro:
Esse foi o meu primeiro crawler em Python. O Objetivo é fazer a raspagem das notícias  <br>
no [_blog da Trybe_](https://blog.betrybe.com).


## Habilidades desenvolvidas:

  * Utilizar o terminal interativo do Python

  * Escrever seus próprios módulos e importá-los em outros códigos

  * Aplicar técnicas de raspagem de dados

  * Extrair dados de conteúdo HTML

  * Armazenar os dados obtidos em um banco de dados


## Intruções para rodar o projeto localmente:
Clone o repositório, mude para o diretório do projeto, crie um ambiente virtual e instale as dependências:
```bash
  ## Clonando repositório:
  git clone git@github.com:Diego-Bueno-M/tech-news.git
  ## Indo para o repositório:
  cd tech-news
  ## Criando o ambiente virtual para o projeto:
  python3 -m venv .venv && source .venv/bin/activate
  ## Instalando as dependências:
  python3 -m pip install -r dev-requirements.txt
```

## Explicação das funções:
* Local: `tech_news/scraper.py`
    * `função fetch` -> Esta função será responsável por fazer a requisição HTTP ao site e obter o conteúdo HTML.
    * `função scrape_updates` -> Esta função fará o scrape da página Novidades para obter as URLs das páginas de notícias.
    * `função scrape_next_page_link` -> Esta função será responsável por fazer o scrape do link da próxima página.
    * `função scrape_news` -> A função busca, no conteúdo recebido, as informações das notícias para preencher um dicionário com os seguintes atributos:
      - `url` - link para acesso da notícia.
      - `title` - título da notícia.
      - `timestamp` - data da notícia, no formato `dd/mm/AAAA`.
      - `writer` - nome da pessoa autora da notícia.
      - `comments_count` - número de comentários que a notícia recebeu.
      - Se a informação não for encontrada, salve este atributo como `0` (zero)
      - `summary` - o primeiro parágrafo da notícia.
      - `tags` - lista contendo tags da notícia.
      - `category` - categoria da notícia.
    * `função get_tech_news` -> A função recebe como parâmetro um número inteiro n e buscar as últimas n notícias do site e depois são inseridas no MongoDB (Para acessar o banco de dados, importe e utilize as funções prontas em tech_news/database.py).
* Rodar MongoDB via Docker: docker-compose up -d mongodb no terminal. Para mais detalhes acerca do mongo com o docker, olhe o arquivo docker-compose.yml
* Local: tech_news/analyzer/search_engine.py
    * `função search_by_title` -> Faz buscas por título.
    * `função search_by_date` -> Faz buscas por data.
    * `função search_by_tag` -> Faz buscas por tag.
    * `função search_by_category` -> Faz buscas por categoria.
 
Obrigado pela leitura e espero que tenham gostado!
