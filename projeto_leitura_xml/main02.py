import csv

# Nome do arquivo CSV de entrada
input_file = 'XML.csv'

# Número máximo de linhas que você deseja processar
max_lines = 30000  # Altere este valor conforme necessário

# Função para criar um novo CSV a partir de uma linha
def write_line_to_csv(line, index):
    output_file = f'linha_{index}.csv'
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(line)

# Lendo o arquivo CSV de entrada
with open(input_file, 'r') as file:
    reader = csv.reader(file)
    
    # Itera sobre cada linha do arquivo CSV de entrada
    for index, row in enumerate(reader):
        if index >= max_lines:
            break
        write_line_to_csv(row, index)