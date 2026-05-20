# 🚀 Guia de Deployment

## Pré-requisitos
- Python 3.7+
- pip (gerenciador de pacotes)
- Git (opcional)

## Passos de Instalação

### 1. Clone o Repositório
git clone https://github.com/dudurvianacomo/web-scraping-fmu.git
cd web-scraping-fmu

### 2. Crie Ambiente Virtual
- python -m venv venv

### 3. Ative o Ambiente Virtual

Windows:
venv\Scripts\activate

macOS/Linux:
source venv/bin/activate

### 4. Instale Dependências
pip install -r requirements.txt

### 5. Execute o Script
python scraper.py

### 6. Verifique o Resultado
ls livros_test.csv

## Possíveis Problemas
- ModuleNotFoundError: Execute pip install -r requirements.txt
- Connection error: Verifique internet e permissões do firewall
- Permission denied: Use python em vez de python3
