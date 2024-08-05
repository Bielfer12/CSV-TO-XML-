import pandas as pd
import xml.etree.ElementTree as ET

# limitando em 5 linhas a leitura do panda com nrows
# criando um dataframe com o df
# execultando o csv
df = pd.read_csv('teste_csv_xml.csv', nrows=5)

# para cada index e informação em cada iteração de linhas faça -->
for index, row in df.iterrows():

    # Criar o elemento raiz do XML
    root = ET.Element('Root')
    
    # Adicionar os dados da linha como elementos XML
    for col in df.columns:
        child = ET.SubElement(root, col)
        child.text = str(row[col])
    
    #  Criando o xml, a arvore do XML completa
    tree = ET.ElementTree(root)
    
    # Salvar o XML em um arquivo separado para cada linha
    # Usar o índice da linha para nomear os arquivos
    filename = f'linha_{index + 1}.xml'
    tree.write(filename, encoding='utf-8', xml_declaration=True)
    
    print(f'Salvou {filename}')
