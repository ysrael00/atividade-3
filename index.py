import xml.etree.ElementTree as ET

# Função do faturamento
def processar_faturamento(arquivo_xml):
    tree = ET.parse(arquivo_xml)
    root = tree.getroot()

    menor_faturamento = float('inf')
    maior_faturamento = float('-inf')
    total_faturamento = 0
    dias_com_faturamento = 0

    # Iterando sobre os dias
    for dia in root.findall('dia'):
        valor = int(dia.find('valor').text)
        
        # ignore valores negativos
        if valor > 0:
            if valor < menor_faturamento:
                menor_faturamento = valor  
            if valor > maior_faturamento:
                maior_faturamento = valor  
            total_faturamento += valor  
            dias_com_faturamento += 1  

    # Calculando a média mensal 
    media_mensal = total_faturamento / dias_com_faturamento if dias_com_faturamento > 0 else 0

    # calculando o número de dias superiores à média
    dias_superiores_a_media = 0

    # Repetindo a iteração para contar dias superiores à média
    for dia in root.findall('dia'):
        valor = int(dia.find('valor').text)
        if valor > media_mensal:
            dias_superiores_a_media += 1

    # mostrando o resultado
    print("Menor faturamento: R$ {:.2f}".format(menor_faturamento))
    print("Maior faturamento: R$ {:.2f}".format(maior_faturamento))
    print("Número de dias com faturamento acima da média: {}".format(dias_superiores_a_media))

# executando
processar_faturamento('faturamento.xml')
