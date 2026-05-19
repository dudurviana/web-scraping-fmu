import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin # Import urljoin to handle relative URLs

# URL do site de teste
url = 'https://books.toscrape.com/'

# Faz a requisição simples
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')

livros = []

# No Books to Scrape, cada bloco de livro fica dentro de um <article class="product_pod">
for item in soup.find_all('article', class_='product_pod'):
    if len(livros) >= 30: # Limite de 10 produtos solicitado
        break

    try:
        # 1. Pegando o título de dentro da tag <a> que está dentro de <h3> usando o atributo ['title']
        # Isso garante que pegamos o nome completo ("A Light in the Attic") e não o texto cortado ("A Light in the ...")
        titulo = item.h3.a['title']

        # 2. Pegando o preço através da classe 'price_color'
        preco = item.find('p', class_='price_color').text.strip()

        # 3. Pegando a URL da página de detalhes do livro
        relative_book_url = item.h3.a['href']
        book_url = urljoin(url, relative_book_url) # Constrói a URL absoluta

        # Faz a requisição para a página de detalhes do livro
        book_resp = requests.get(book_url)
        book_soup = BeautifulSoup(book_resp.text, 'html.parser')

        # Encontra a descrição do produto. Na Books to Scrape, está dentro de um div com id="product_description" e um p
        description_tag = book_soup.find('div', id='product_description')
        descricao = description_tag.find_next_sibling('p').text.strip() if description_tag else 'Descrição não disponível'

        # Adiciona à lista com os nomes de colunas que você deseja
        livros.append({
            'Nome do produto': titulo,
            'Preço': preco,
            'Descrição': descricao # Adiciona a descrição aqui
        })
    except AttributeError:
        # Se falhar em algum elemento, pula para o próximo
        continue
    except Exception as e:
        print(f"Erro ao processar o livro: {titulo if 'titulo' in locals() else 'Desconhecido'}, Erro: {e}")
        continue

# Transforma em DataFrame e exporta para CSV
df = pd.DataFrame(livros)
df.to_csv('livros_test.csv', index=False, encoding='utf-8-sig')

print(f'Sucesso! {len(livros)} livros coletados e salvos em "livros_test.csv"!')
