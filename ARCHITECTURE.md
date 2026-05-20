# 📐 Arquitetura do Projeto


## Componentes Principais

### 1. **Requests** (HTTP Client)
- Faz requisições ao site
- Retorna HTML da página
- Trata erros de conexão

### 2. **BeautifulSoup** (Parser HTML)
- Analisa a estrutura HTML
- Extrai dados específicos
- Navegação por seletores CSS

### 3. **Pandas** (Data Processing)
- Organiza dados em tabela
- Exporta para CSV
- Valida informações

## Seletores CSS Utilizados

| Elemento | Seletor CSS | Função |
|----------|-------------|--------|
| Livro | `.product_pod` | Container do livro |
| Título | `h3 > a` | Nome do livro |
| Preço | `.price_color` | Valor em libras |
| Descrição | `.product_description` | Texto descritivo |
