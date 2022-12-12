import sys

def txt_importer(path_file):
    """Aqui irá sua implementação"""
    try:
        read_file = list()
        if path_file.endswith('.txt'):
            with open(path_file, 'r') as files:
                for file in files:
                    read_file.append(file.replace('\n', ''))

            return read_file
        if not path_file.endswith('.txt') :
            print('Formato inválido', file=sys.stderr)
    except FileNotFoundError:
        print(f'Arquivo {path_file} não encontrado', file=sys.stderr)
