# Web Scraping FMU - Books to Scrape

Um projeto de web scraping educacional que coleta dados de livros do site **Books to Scrape** e os exporta para um arquivo CSV.

## 📋 Sobre o Projeto

Este projeto demonstra técnicas práticas de web scraping usando Python, coletando informações de livros incluindo:
- **Título** do livro
- **Preço** em libras esterlinas
- **Descrição** completa do produto

Os dados coletados são salvos em um arquivo CSV para análise posterior.

## 🎯 Funcionalidades

✅ Raspagem de dados de múltiplas páginas do site Books to Scrape  
✅ Coleta de informações detalhadas (título, preço e descrição)  
✅ Tratamento robusto de erros e exceções  
✅ Suporte a URLs relativas e absolutas  
✅ Exportação automática para CSV com encoding UTF-8  
✅ Limite configurável de produtos coletados  

## 🛠️ Tecnologias Utilizadas

- **Python 3.7+**
- **Requests** - Biblioteca para fazer requisições HTTP
- **BeautifulSoup4** - Parser HTML/XML para extração de dados
- **Pandas** - Manipulação e exportação de dados para CSV
- **urllib.parse** - Tratamento de URLs relativas

## 📦 Instalação

### Pré-requisitos
- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

2. Crie um ambiente virtual (recomendado)
bash
python -m venv venv



3. Ative o ambiente virtual
Sem janelas:




bash
venv\Scripts\activate

Sem macOS/Linux:

bash
source venv/bin/activate




4. Instale as marcações
bash
pip install -r requirements.txt
Ou instale este:

bash
pip install requests beautifulsoup4 pandas

🚀 COMO USAR:

Executar o script principal
bash
python scraper.py
Aguarde a coleta de dados



O script fará requisições ao site e coletará os dados
Uma barra de progresso mostrará o status da coleta
Abra o arquivo gerado




Os dados serão salvos emlivros_test.csv
Você pode abrir o arquivo com Excel, Google Sheets ou qualquer editor de texto



📄 Estrutura do Arquivo CSV


O arquivo livros_test.csvgerado contém as seguintes colunas:

Nome do produto	Preço	Descrição
Uma Luz no Sótão	£ 51,77	"É difícil imaginar um mundo sem 'Uma Luz no Sótão'..."
Virando o Veludo	£ 53,74	"Tipping the Velvet é, em sua essência, uma história de amor..."
...	...	...


🔧 Configurações


Você pode ajustar as seguintes configurações no script:

Limite de Produtos
Python
if len(livros) >= 30: # Altere 30 para o número desejado
    break
    
URL do site
Python
url = 'https://books.toscrape.com/' # Altere conforme necessário

Nome do Arquivo de lid
Python
df.to_csv('livros_test.csv', ...) # Altere o nome do arquivo

📊 Exemplo de sorteio:


Código
Sucesso! 30 livros coletados e salvos em "livros_test.csv"!

🐛 Tratamento de grupos:


O script possui tratamento robusto de erros:

AttributeError : Pula itens com estrutura HTML inesperada
Exceção genérica : Captura e exibe qualquer outro erro durante o processamento
Descrição não disponível : Exibe mensagem padrão se a descrição não for encontrada

⚠️Considerações Importantes
Respeite robots.txt : Antes de fazer scraping em qualquer site, verifique se é permitido
Rate Limiting : O site Books to Scrape é apenas para prática educacional e permite scraping
Desempenho : Para grandes volumes de dados, considere adicionar atrasos entre requisições
Legal : Sempre verifique os termos de serviço do site antes de fazer raspagem

💡 Melhores Futuras
 Adicionar suporte a várias páginas
 Implementar sistema de cache para evitar requisições duplicadas
 Adicionar registro detalhado
 Criar interface de linha de comando (CLI)
 Adicionar testes automatizados
 Implementar raspagem assíncrona com aiohttp
 
📚 Recursos Educacionais
Documentação BeautifulSoup
Solicitações de documentação
Documentação Pandas
Ética na Extração de Dados da Web

👨‍💻 Autor
Eduardo Viana, Vinicius Galoa, Manuella Santana 

GitHub: @dudurviana
📝 Licença
Este projeto é fornecido para fins educacionais. Use livremente e respeite os termos de serviço dos sites que você faz scraping.

🤝 Contribuindo
Contribuições são bem-vindas! Sinta-se à vontade para:

Fazer um Fork do projeto
Crie um branch para seu feature ( git checkout -b feature/MinhaFeature)
Comprometa suas mudanças ( git commit -m 'Adiciona MinhaFeature')
Empurre para um ramo ( git push origin feature/MinhaFeature)
Abrir um Pull Request
