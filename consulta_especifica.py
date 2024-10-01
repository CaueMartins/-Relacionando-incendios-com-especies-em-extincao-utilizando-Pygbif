import pandas as pd
from pygbif import species, occurrences

# Nome da espécie que você deseja buscar
especie_desejada = "Hyalella imbya"  # Coloque o nome desejado aqui

# Usar a biblioteca pygbif para buscar informações
taxa_info = species.name_suggest(especie_desejada)

if taxa_info:
    taxon_key = taxa_info[0]['key']  # Pega a primeira sugestão
    resultado = occurrences.search(taxonKey=taxon_key)

    # Processar o resultado conforme necessário
    if resultado['count'] > 0:
        for ocorrencia in resultado['results']:
            # Verificar se as chaves existem
            especie_nome = ocorrencia.get('species', 'Espécie desconhecida')
            latitude = ocorrencia.get('decimalLatitude', 'Latitude não disponível')
            longitude = ocorrencia.get('decimalLongitude', 'Longitude não disponível')
            
            print(f"Espécie: {especie_nome}, Local: {latitude}, {longitude}")
    else:
        print(f"Nenhuma ocorrência encontrada para a espécie: {especie_desejada}")
else:
    print(f"Nenhuma sugestão encontrada para a espécie: {especie_desejada}")
