import time


empresa_data = {
    "Matriz": {
        "TI": {
            "Infraestrutura": {
                "Servidores": 50000,
                "Seguranca": 30000
            },
            "Desenvolvimento": {
                "Frontend": 20000,
                "Backend": 25000,
                "DevOps": 15000
            }
        },
        "RH": {
            "Recrutamento": 10000,
            "Treinamento": 12000,
            "Cultura": {
                "Eventos": 5000,
                "Brindes": 2000
            }
        },
        "Financeiro": 40000
    }
}


def auditor(funcao):
    def wrapper(*args, **kwargs):
        print("=== Auditoria iniciada ===")
        print("Setores ignorados:", args[1:])
        print("Configurações:", kwargs)

        inicio = time.time()
        resultado = funcao(*args, **kwargs)
        fim = time.time()

        print("Tempo de execução:", round(fim - inicio, 5), "segundos")
        print("=== Auditoria finalizada ===")

        return resultado

    return wrapper


@auditor
def calcular_orcamento(dados, *ignorados, **kwargs):
    total = 0

    for setor, valor in dados.items():

        if setor in ignorados:
            print("Setor ignorado:", setor)
            continue

        if isinstance(valor, dict):
            total += calcular_orcamento(valor, *ignorados, **kwargs)
        else:
            total += valor

    taxa = kwargs.get("taxa_cambio", 1)

    return total * taxa


resultado = calcular_orcamento(
    empresa_data,
    "RH",
    moeda_destino="BRL",
    taxa_cambio=1
)

print("Orçamento total: R$", resultado)
