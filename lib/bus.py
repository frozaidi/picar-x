from readerwriterlock import rwlock


class Bus():
    def __init__(self):
        self.msg = None
        self.lock = rwlock.RWLockWriteD()

    def write(self, msg):
        with self.lock.get_wlock():
            self.msg = msg

    def read(self):
        with self.lock.get_rlock():
            msg = self.msg
        return msg
