from readerwriterlock import rwlock


class Bus():
    def __init__(self):
        self.msg = None
        self.lock = rwlock.RWLockWriteD()

    def write(self, msg):
        """
        Function to write message value to the instantiated bus
        :param msg: The bus class
        """
        with self.lock.gen_wlock():
            self.msg = msg

    def read(self):
        """
        Function to read and return message value from the instantiated bus
        """
        with self.lock.gen_rlock():
            msg = self.msg
        return msg
