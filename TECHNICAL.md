# TECHNICAL.md - Documentação Técnica

## 🏗️ Arquitetura do Scraper




## 🔍 Seletores HTML Utilizados

| Dado | Seletor | Tag | Atributo |
|------|---------|-----|----------|
| Título | `h3.a['title']` | `<h3><a>` | `title` |
| Preço | `p.price_color` | `<p>` | `class` |
| Link | `h3.a['href']` | `<a>` | `href` |
| Descrição | `div#product_description` | `<div>` | `id` |

## ⚙️ Fluxo Principal

1. **Requisição**: GET request para `https://books.toscrape.com/`
2. **Parse**: BeautifulSoup processa HTML
3. **Loop**: Itera sobre `<article class="product_pod">`
4. **Extração**: Coleta título, preço e descrição
5. **Validação**: Trata erros com try/except
6. **Armazenamento**: Adiciona à lista `livros[]`
7. **Export**: Salva em CSV com pandas

## 🛡️ Tratamento de Erros

```python
AttributeError    → Elemento não encontrado (pula)
Exception         → Erro genérico (registra e pula)
Descrição nula    → Mostra "Descrição não disponível"

📊 Configurações Ajustáveis
Python
# Limite de produtos
if len(livros) >= 30:  # Altere para outro número

# URL do site
url = 'https://books.toscrape.com/'  # Altere conforme necessário

# Nome do arquivo
df.to_csv('livros_test.csv', ...)  # Altere o nome


⚠️ ## 𝗣𝗿𝗼𝗯𝗹𝗲𝗺𝗮𝘀 𝗲 𝗦𝗼𝗹𝘂çõ𝗲𝘀 𝗖𝗼𝗺𝘂𝗻𝘀

Problema	      Causa	        Solução
AttributeError	     HTML diferente	        Atualizar seletores CSS
ConnectionError	    Sem internet	         Verificar conexão
Empty CSV	Nenhum    livro encontrado	Verificar seletores
Timeout	Site lento	Aumentar timeout do requests









⚠️ Problemas Comuns & Soluções
Problema	Causa	Solução
AttributeError	HTML diferente	Atualizar seletores CSS
ConnectionError	Sem internet	Verificar conexão
Empty CSV	Nenhum livro encontrado	Verificar seletores
Timeout	Site lento	Aumentar timeout do requests
