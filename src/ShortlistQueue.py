__author__ = 'Lambert Justo'

class ShortlistQueue:
    def __init__(self):
        self.queue = []

    def get_queue(self):
        return self.queue

    def push(self, entry):
        self.queue.append(entry)
        print("added", entry, "to the queue")

    def fetch(self, elem, ret=False):
        val = self.queue.pop(self.queue.index(elem))
        if ret:
            return val

    def fetch_by_index(self, index, ret=False):
        if (index >= len(self.queue) or index < 0):
            return
        val = self.queue.pop(index)
        if ret:
            return val

    def fetch_by_text(self, text, ret=False):
        index = None
        for i in range(len(self.get_queue())):
            if self.get_queue()[i].get_text() == text:
                index = i
        if index is not None:
            res = self.queue.pop(index)
            if ret:
                return res
            else:
                return
