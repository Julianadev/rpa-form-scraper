from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import logging
import colorlog
import pandas as pd
import openpyxl

handler = colorlog.StreamHandler()
handler.setFormatter(
    colorlog.ColoredFormatter("%(log_color)s%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S",
        log_colors={'DEBUG': 'cyan', 'INFO': 'green', 'WARNING': 'yellow', 'ERROR': 'red', 'CRITICAL': 'bold_red', }))

logger = colorlog.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)

class RobotExtraiDados:
    def __init__(self):
        opcoes = Options()

        opcoes.add_argument("--headless=new")
        opcoes.add_argument("--disable-gpu")
        opcoes.add_argument("--no-sandbox")
        opcoes.add_argument("--window-size=1920,1080")

        self.driver = webdriver.Chrome(options=opcoes)

        self.wait = WebDriverWait(self.driver, 10)
        self.url = "https://curso-web-scraping.pages.dev/#/exemplo/1"

        self.dados = []
        self.nome_arquivo_salvo = r"dados_pessoas.xlsx"

    def abrir_site(self):
        """
        Acessando o site
        """
        try:
            self.driver.get(self.url)
            logger.info(f'Site {self.driver.current_url} acessado com sucesso!')
            self.driver.maximize_window()
        except TimeoutException as e:
            logger.error(f"Tempo excedido ao acessar o site: {self.driver.current_url}, {e}")
        except Exception as e:
            logger.error(f"Ocorreu um erro ao acessar o site: {self.driver.current_url}. {e}")

    def extrair_dados(self):
        """
        Extrai os dados do formulário
        """
        for i in range(50):
            try:
                # Nome
                nome = self.wait.until(EC.presence_of_element_located((By.ID, 'user'))).get_property("value")

                # Profissão
                profissao = self.driver.find_element(By.ID, "user").get_property("value")

                # Signo
                signo = self.driver.find_element(By.ID, "zodiac").get_property("value")

                # Genero
                genero = self.driver.find_element(By.ID, "gender").get_property("value")

                pessoa = {
                    "Nome": nome,
                    "Profissao": profissao,
                    "Signo": signo,
                    "Genero": genero,
                    "Status": "Sucesso"
                }

                self.dados.append(pessoa)

                logger.info(f"Registro {i+1} salvo com sucesso!")
            except TimeoutException as e:
                logger.error(f"Ocorreu um tempo de execução: {e}")
            except Exception as e:
                pessoa = {"Nome": None,
                          "Profissao": None,
                          "Signo": None,
                          "Genero": None,
                          "Status": "ERRO",
                          "Mensagem": str(e)
                          }

                self.dados.append(pessoa)

                logger.error(f"Falha ao extrair registro")
            finally:
                self.driver.refresh()

    def salvar_dados(self):
        """
        Salva os dados em um arquivo .xlsx
        :return:
        """
        try:
            if self.dados:
                df = pd.DataFrame(self.dados)
                if self.nome_arquivo_salvo.endswith('xlsx'):
                    df.to_excel(self.nome_arquivo_salvo, index=False)
                    logger.info(f"{self.nome_arquivo_salvo} salvo com sucesso!")
                else:
                    logger.error("A extensão do arquivo deverá ser '.xlsx'")
            else:
                logger.error('Arquivo vazio')
        except Exception as e:
            logger.error(f"Ocorreu um erro: {e}")

    def fechar_site(self):
        self.driver.quit()

    def executar(self):
        """
        Executa a aplicacao
        :return:
        """
        self.abrir_site()
        self.extrair_dados()
        self.salvar_dados()


if __name__ == "__main__":
    robo = None

    try:
        robo = RobotExtraiDados()
        robo.executar()
    except Exception as e:
        logger.error(f"Ocorreu um erro: {e}")
    finally:
        if robo:
            robo.fechar_site()



