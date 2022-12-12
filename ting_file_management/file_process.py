import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, queue: Queue):
    """Aqui irá sua implementação"""
    if path_file in str(queue._queue):
        return None
    file_txt = txt_importer(path_file)

    file_of_dicts = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_txt),
        "linhas_do_arquivo": file_txt
    }

    queue.enqueue(file_of_dicts)
    print(file_of_dicts, file=sys.stdout)


def remove(queue: Queue):
    """Aqui irá sua implementação"""
    if not len(queue._queue):
        return sys.stdout.write("Não há elementos\n")

    remove = queue.dequeue()
    path_file = remove["nome_do_arquivo"]
    print(f"Arquivo {path_file} removido com sucesso", file=sys.stdout)


def file_metadata(queue: Queue, position):
    """Aqui irá sua implementação"""
    try:
        result = queue.search(position)
        print(f"{result}", file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
