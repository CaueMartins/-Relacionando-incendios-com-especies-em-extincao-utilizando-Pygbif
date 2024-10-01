import pandas as pd
from pygbif import species, occurrences

# Ler o arquivo CSV
caminho_csv = 'C:\\Users\\caue\\Documents\\phyton\\PI\\extincao.csv'
dados = pd.read_csv(caminho_csv)

# Remover espaços em branco dos nomes das colunas
dados.columns = dados.columns.str.strip()

# Usar a coluna "Espécie ou Subespécie"
for especie in dados['Espécie ou Subespécie']:
    taxa_info = species.name_suggest(especie)
    
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
            print(f"Nenhuma ocorrência encontrada para a espécie: {especie}")
    else:
        print(f"Nenhuma sugestão encontrada para a espécie: {especie}")
