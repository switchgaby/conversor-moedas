TAXAS = {
    'USD': 5.25,  # Dólar para Real
    'EUR': 5.90,  # Euro para Real
    'BRL': 1.0    # Real (base)
}

def converter(valor, origem, destino):
    if origem not in TAXAS or destino not in TAXAS:
        raise ValueError("Moeda inválida. Use: USD, EUR ou BRL.")
    
    # Converte o valor para real primeiro
    valor_em_reais = valor / TAXAS[origem]
    
    # Depois converte do real para a moeda de destino
    convertido = valor_em_reais * TAXAS[destino]
    
    return round(convertido, 2)

if __name__ == "__main__":
    print("Moedas disponíveis: BRL (Real), USD (Dólar), EUR (Euro)")
    origem = input("Converter de: ").upper()
    destino = input("Converter para: ").upper()
    valor = float(input("Valor: "))
    
    try:
        resultado = converter(valor, origem, destino)
        print(f"{valor} {origem} = {resultado} {destino}")
    except ValueError as e:
        print(e)
