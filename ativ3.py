import json

with open('./json/dados.json') as arquivo:
    dados = json.load(arquivo)

menorValorDia = ""
menorValorValor = 0
maiorValorDia = ""
maiorValorValor = 0
mediaMensalNum = 0
mediaMensalCont = 0
numDias = 0
somaTotal = 0

if isinstance(dados, list):
    for item in dados:
        if 'dia' in item and 'valor' in item:

            if (menorValorValor == 0 or item['valor'] < menorValorValor):
                menorValorDia = item['dia']
                menorValorValor = item['valor']

            if (maiorValorValor == 0 or item['valor'] > maiorValorValor):
                maiorValorDia = item['dia']
                maiorValorValor = item['valor']

            if (item['valor'] > 0):
                somaTotal += item['valor']

mediaMensalNum = somaTotal / len(dados)

if isinstance(dados, list):
    for item in dados:
        if 'dia' in item and 'valor' in item:
            if (item['valor'] > mediaMensalNum):
                mediaMensalCont += 1

print(f"Menor valor: {round(menorValorValor, 2)} no dia {menorValorDia} (Ignorando finais de semana e feriados)")
print(f"Maior valor: {round(maiorValorValor, 2)} no dia {maiorValorDia}")
print(f"Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {mediaMensalCont}")