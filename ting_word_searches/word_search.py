from ting_file_management.queue import Queue


def exists_word(word, queue: Queue):
		"""Aqui irá sua implementação"""
		list_of_exists_word = list()

		for position in range(len(queue._queue)):
			search_word = queue.search(position)

			result = {
				"palavra": word,
				"arquivo": search_word["nome_do_arquivo"],
				"ocorrencias": [
					{
						"linha": ind + 1
					}
					for ind, row in enumerate(search_word["linhas_do_arquivo"])
					if word in row.lower()
				]
			}

			if not len(result["ocorrencias"]):
				return []

			list_of_exists_word.append(result)
			return list_of_exists_word


def search_by_word(word, queue: Queue):
		"""Aqui irá sua implementação"""
