def int_to_roman(numero):
    # Lista de tuplas (valor, símbolo) ordenada do maior para o menor
    valores = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    resultado = ''  # String que vai acumular o resultado final
    
    for valor, simbolo in valores:
        # Enquanto o número for maior ou igual ao valor atual
        while numero >= valor:
            resultado += simbolo  # Adiciona o símbolo romano ao resultado
            numero -= valor       # Subtrai o valor do número
    
    return resultado

# Testando a função com o número 3999
print(int_to_roman(3999))
