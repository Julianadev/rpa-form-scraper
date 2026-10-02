# 🤖 Web Scraper: Extrator de Dados com Selenium

Um robô de automação construído em Python utilizando a biblioteca Selenium. Este projeto tem como objetivo acessar um portal web, raspar dados dinâmicos de formulários (Nome, Profissão, Signo e Gênero) e consolidar os resultados em um arquivo Excel (.xlsx), lidando de forma resiliente com possíveis falhas de execução.

# Destaques e Boas Práticas (Features)

Orientação a Objetos (POO): Código modularizado em classe (RobotExtraiDados), facilitando manutenção e leitura.

Resiliência e Tratamento de Erros: Blocos try/except garantem que o robô não pare a execução inteira caso um único registro falhe. Registros com erro são salvos com uma flag de falha.

Espera Explícita (Explicit Waits): Utiliza WebDriverWait e Expected Conditions para aguardar o carregamento dinâmico dos elementos da página, otimizando o tempo de execução (sem o uso do engessado time.sleep).

Sistema de Logs Customizado: Substitui o clássico print pela biblioteca colorlog, gerando logs coloridos e com timestamps precisos no terminal (Níveis de INFO, ERROR, etc).

Gestão Segura de Recursos: Bloco finally garante que a sessão do navegador (WebDriver) seja sempre encerrada, evitando processos fantasmas consumindo memória do sistema.

# 🛠️ Tecnologias Utilizadas

Python 3.x

Selenium WebDriver - Para automação e interação com o navegador.

Pandas - Para estruturação dos dados extraídos e exportação.

Colorlog - Para a formatação visual dos logs.

# 🚀 Como instalar e executar

## Pré-requisitos

Certifique-se de ter o Python instalado na sua máquina e o navegador Google Chrome atualizado.

## 1. Clone o repositório

```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO
```

## 2. Crie um ambiente virtual (Opcional, mas recomendado)

```bash
python -m venv venv
# Para ativar no Windows:
venv\Scripts\activate
# Para ativar no Linux/Mac:
source venv/bin/activate
```

## 3. Instale as dependências

Crie um arquivo requirements.txt na raiz do projeto com o seguinte conteúdo, ou instale diretamente via pip:

```bash
pip install selenium pandas colorlog openpyxl
```

(Nota: a biblioteca openpyxl é necessária para o pandas conseguir exportar arquivos .xlsx)

## 4. Execute o robô

```bash
python nome_do_seu_arquivo.py
```

# 📊 Estrutura do Arquivo de Saída

Após a execução bem-sucedida, um arquivo chamado dados_pessoas.xlsx será gerado na raiz do projeto contendo as seguintes colunas:

Nome

Profissao

Signo

Genero

Status (Sucesso ou ERRO)

Mensagem (Caso ocorra erro, exibe o motivo)


# 👤 Autor

Criado por Juliana Ramos - 
Sinta-se à vontade para se conectar comigo 
