__author__ = 'weiqisong'


class Store:
    def __init__(self, data_path, meta_path):
        self.chunk_file_count = 1
        self.data_path = data_path
        self.meta_path = meta_path
        self.chunk_files = []
        self.cold_start()

    def read_data_to_buf(self, chunk_id, offset, size):
        chunk = self.chunk_files[chunk_id]
        if chunk is None:
            raise Exception("chunk {chunk} is not exist".format(chunk=chunk_id))
        chunk.seek(offset)
        return chunk.read(size)

    def write_data(self, chunk_id, offset, data):
        chunk = self.chunk_files[chunk_id]
        if chunk is None:
            raise Exception("chunk {chunk} is not exist".format(chunk=chunk_id))

        chunk.seek(offset)
        chunk.write(data)

    def cold_start(self):
        for i in range(self.chunk_file_count):
            chunk_file = self.data_path + "\\" + str(i)
            file = open(chunk_file, mode='r+b')
            if file is None:
                return
            self.chunk_files.append(file)


# f = open("C:\\Users\\Administrator\\Desktop\\download2\\1.txt", "r+b")
# f.seek(5)
# print(f.read(200))

# store = Store("C:\\Users\\Administrator\\Desktop\\download2\\", "C:\\Users\\Administrator\\Desktop\\download2\\")
# data = bytes("test", "utf-8")
# print(len(data))
# store.write_data(0, 0, bytes("test", "utf-8"))
# print(store.read_data_to_buf(0, 0, 4))
