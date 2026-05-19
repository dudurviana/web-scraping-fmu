# 🤝 Guia de Contribuição

Obrigado por considerar contribuir para o **Web Scraping FMU**! Este documento fornece diretrizes e instruções para contribuir.

## 📋 Código de Conduta

Por favor, seja respeitoso e profissional ao interagir com outros contribuidores.

## 🐛 Relatando Bugs

Antes de abrir uma issue sobre um bug:
1. Verifique se o bug já foi reportado
2. Verifique a seção FAQ do README
3. Teste em diferentes versões do Python

Quando reportar um bug, inclua:
- Sistema operacional
- Versão do Python
- Stack trace completo
- Passos para reproduzir o problema
- Comportamento esperado vs. real

## 💡 Sugerindo Melhorias

Sugestões de melhorias são bem-vindas! Para sugerir uma melhoria:
1. Use um título descritivo
2. Forneça uma descrição clara e detalhada
3. Liste exemplos do comportamento atual e esperado
4. Explique por que essa melhoria seria útil

## 🔧 Processo de Desenvolvimento

1. Faça um Fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Faça commits descritivos (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

## 📝 Estilo de Código

- Siga a [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use nomes descritivos para variáveis e funções
- Adicione comentários para código complexo
- Mantenha linhas com no máximo 80 caracteres

## 🧪 Testando Localmente

```bash
# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Execute o script
python scraper.py
