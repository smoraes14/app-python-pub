import requests
with open("url.txt") as file:
    lista_urls = file.read()
    lista_urls = lista_urls.splitlines()

def testar_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"A URL {url} está acessível.")
        else:
            print(f"A URL {url} retornou um código de status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro ao acessar a URL {url}: {e}")

# Lista de URLs para teste
#lista_urls = ["https://www.google.com", "https://www.invalidurl.com"]

# Testar cada URL na lista
for url in lista_urls:
    testar_url(url)
