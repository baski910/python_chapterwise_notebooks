class FileManager():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
         
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
     
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()
 
# loading a file
file_descriptors = []
for x in range(10000):
    with FileManager('test{x}.txt', 'w') as f:
        file_descriptors.append(f)