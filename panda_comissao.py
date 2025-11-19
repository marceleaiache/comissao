import msvcrt

# ==========================
# CADASTRO FIXO DE FUNCIONÁRIOS
# ==========================

equipes = {
    "ATENDIMENTO": [
        "RAFA", "ERI", "NAARIS", "GABY", "ISA", "MARCELE", "THAINA", "RHUANNA", "HIGOR"
    ],
    "COZINHA": [
        "RONNY", "PEDRO", "RENATIN", "ZEQUINHA", "CALINE", "SANDRA", "STEFANIE", "NARJA", "THAYNARA"
    ],
    "OUTROS": [
        "ELIANE", "RAQUEL", "ELIZA"
    ]
}

# ==========================
# CONFIGURAÇÃO DO SISTEMA
# ==========================

dias = ["segunda", "quarta", "quinta", "sexta", "sábado", "domingo"]
valores = {}
pessoas_dia = {}
totais = {}

# ==========================
# MOSTRAR EQUIPE COM NÚMEROS FIXOS
# ==========================
def mostrar_equipes():
    print("\n=== LISTA DE FUNCIONÁRIOS ===")
    contador = 1
    mapa_pessoas = {}
    for setor, nomes in equipes.items():
        print(f"\n{setor}:")
        for nome in nomes:
            print(f"  [{contador}] {nome}")
            mapa_pessoas[contador] = nome
            contador += 1
    return mapa_pessoas

# ==========================
# INÍCIO DO SISTEMA
# ==========================

print("=== CADASTRO DOS VALORES DE 10% ===")
for dia in dias:
    entrada = input(f"Digite o valor dos 10% de {dia}: R$ ").replace(",", ".")
    try:
        valor = float(entrada)
    except ValueError:
        print("Valor inválido! Use apenas números. Exemplo: 250.50")
        exit(1)
    valores[dia] = valor

# Mostrar lista de funcionários numerados
mapa = mostrar_equipes()

# ==========================
# SELEÇÃO DE FUNCIONÁRIOS POR DIA — ENTER inclui, ESC pula
# ==========================
for dia in dias:
    print(f"\n--- {dia.upper()} ---")
    print("Para cada funcionário:")
    print("  ENTER = trabalhou")
    print("  ESC   = não trabalhou\n")

    lista_pessoas = []

    for indice in sorted(mapa.keys()):
        pessoa = mapa[indice]
        print(f"{pessoa}: ", end="", flush=True)

        while True:
            tecla = msvcrt.getch()

            if tecla == b'\r':  # ENTER → inclui
                lista_pessoas.append(pessoa)
                print("✔ Incluído")
                break

            elif tecla == b'\x1b':  # ESC → não inclui
                print("✖ Ignorado")
                break

            else:
                # Se apertar outra tecla, não avança
                print("\nUse apenas ENTER ou ESC.")
                print(f"{pessoa}: ", end="", flush=True)

    pessoas_dia[dia] = lista_pessoas

    if not lista_pessoas:
        print(f"\nNenhum funcionário trabalhou na {dia}.")
        continue

    valor_total = valores[dia]
    valor_por_pessoa = valor_total / len(lista_pessoas)

    for pessoa in lista_pessoas:
        totais[pessoa] = totais.get(pessoa, 0) + valor_por_pessoa

# ==========================
# MOSTRAR TOTAL SEMANAL
# ==========================

print("\n=== TOTAL SEMANAL ===")
print("-" * 30)
for pessoa, total in sorted(totais.items()):
    print(f"{pessoa:<15} R$ {total:>7.2f}")
print("-" * 30)

# ==========================
# SALVAR RESULTADO
# ==========================

salvar = input("\nDeseja salvar o resultado em um arquivo? (s/n): ").lower()
if salvar == "s":
    with open("resultado_10_porcento.txt", "w", encoding="utf-8") as f:
        f.write("=== RESULTADO DOS 10% ===\n\n")
        for pessoa, total in sorted(totais.items()):
            f.write(f"{pessoa:<15} R$ {total:>7.2f}\n")
    print("✅ Arquivo 'resultado_10_porcento.txt' salvo com sucesso!")
