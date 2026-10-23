import json
import urllib.request

# Substitua pela URL do webhook criado no n8n
WEBHOOK_URL = "http://localhost:5678/webhook-test/teste"


def enviar(dados):
    req = urllib.request.Request(
        WEBHOOK_URL,
        data=json.dumps(dados).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req) as resp:
        return resp.status, resp.read().decode("utf-8")


if __name__ == "__main__":
    print(enviar({"mensagem": "Olá, n8n!"}))
