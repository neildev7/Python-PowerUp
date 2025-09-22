import pyautogui
import time
import pandas 

# Configuração inicial do pyautogui para adicionar um pequeno intervalo entre as ações
pyautogui.PAUSE = 0.3

# Passo 1: Abrir o navegador Chrome
pyautogui.press("win")  # Pressiona a tecla Windows para abrir o menu iniciar
time.sleep(0.3)
pyautogui.write("chrome")  # Digita "chrome" para buscar o navegador
pyautogui.press("enter")  # Pressiona Enter para abrir o Chrome

# Acessar o site de login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")  # Pressiona Enter para acessar o site

# Aguarda o site carregar
time.sleep(3)

# Passo 2: Fazer login no site
# selecionar o campo de email
pyautogui.click(x=668, y=375)
# escrever o seu email
pyautogui.write("seu_email@exemplo.com")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("sua_senha")
pyautogui.click(x=784, y=536) # clique no botao de login

# Aguarda o login ser processado
time.sleep(3)

# Lê a tabela de produtos a partir de um arquivo CSV
tabela = pandas.read_csv("produtos.csv")

# Exibe a tabela no console para conferência
print(tabela)

# Passo 3: Inserir os produtos no sistema
for linha in tabela.index:
    pyautogui.click(x=652, y=258) # clicar no botao de produtos

    # Preenche o código do produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # Preenche a marca do produto
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    # Preenche o tipo do produto
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    # Preenche a categoria do produto
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    # Preenche o preço unitário do produto
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    # Preenche o custo do produto
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    # Preenche observações, se houver
    obs = tabela.loc[linha, "obs"]
    if pandas.notna(obs):   # evita erro se estiver vazio
        pyautogui.write(str(obs))

    pyautogui.press("tab")
    pyautogui.press("enter") # salvar o produto

    # Faz um scroll para cima para garantir que o próximo produto esteja visível
    pyautogui.scroll(1000) # scroll para cima