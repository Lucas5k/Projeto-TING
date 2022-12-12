class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self._queue = list()

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self._queue)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self._queue.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        if len(self._queue) == 0:
            return None

        return self._queue.pop(0)

    def search(self, index):
        """Aqui irá sua implementação"""
        if 0 <= index < len(self._queue):
            return self._queue[index]
        raise IndexError('index not found')


if __name__ == '__main__':
    queue = Queue()

    queue.enqueue(42)


    print(queue.search(0))

    print(queue.interactive())
