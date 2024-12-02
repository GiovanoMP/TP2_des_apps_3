import requests

def test_translation():
    url = "http://localhost:8000/translate"
    texts = [
        "Hello world",
        "How are you?",
        "This is a test"
    ]

    print("\n=== Iniciando testes de tradução ===")
    
    for text in texts:
        try:
            print(f"\nTestando tradução de: '{text}'")
            response = requests.post(
                url,
                json={"text": text}
            )
            
            # Adiciona mais informações de debug
            print(f"Status Code: {response.status_code}")
            
            if response.status_code == 200:
                result = response.json()
                print(f"Texto original: {text}")
                print(f"Tradução: {result['translated_text']}")
            else:
                print(f"Erro na requisição: {response.text}")
                
        except requests.exceptions.ConnectionError:
            print(f"Erro de conexão: Verifique se o servidor está rodando em {url}")
        except Exception as e:
            print(f"Erro inesperado: {str(e)}")

def test_error_cases():
    url = "http://localhost:8000/translate"
    
    print("\n=== Testando casos de erro ===")
    
    # Teste com texto vazio
    try:
        response = requests.post(
            url,
            json={"text": ""}
        )
        print(f"\nTeste com texto vazio - Status: {response.status_code}")
        print(f"Resposta: {response.json()}")
    except Exception as e:
        print(f"Erro no teste com texto vazio: {e}")

    # Teste com JSON inválido
    try:
        response = requests.post(
            url,
            json={}
        )
        print(f"\nTeste com JSON inválido - Status: {response.status_code}")
        print(f"Resposta: {response.text}")
    except Exception as e:
        print(f"Erro no teste com JSON inválido: {e}")

if __name__ == "__main__":
    print("Iniciando testes da API de tradução...")
    print("Certifique-se de que o servidor está rodando em http://localhost:8000")
    
    # Executa os testes
    test_translation()
    test_error_cases()


if __name__ == "__main__":
    test_translation()
