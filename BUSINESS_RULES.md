# 📋 Regras de Negócio

## Objetivos do Projeto

1. **Coleta de Dados** - Extrair informações de livros do Books to Scrape
2. **Organização** - Estruturar dados em formato CSV padronizado
3. **Acessibilidade** - Permitir análise dos dados coletados
4. **Educação** - Demonstrar técnicas de web scraping

## Regras de Validação

### Título do Livro
- ✅ Obrigatório
- ✅ Máximo 200 caracteres
- ✅ Sem caracteres especiais inválidos

### Preço
- ✅ Sempre em libras esterlinas (£)
- ✅ Formato: £XX.XX
- ✅ Não pode ser vazio

### Descrição
- ✅ Opcional
- ✅ Máximo 500 caracteres
- ✅ Se não encontrada, usa padrão

## Limite de Dados

- **Máximo de livros por execução:** 30 (configurável)
- **Intervalo entre requisições:** Imediato
- **Timeout de conexão:** 10 segundos

## Conformidade

- ✅ Respeita robots.txt do Books to Scrape
- ✅ Site autoriza scraping educacional
- ✅ Sem violação de termos de serviço
