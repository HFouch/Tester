class WriteOutputFile:
    def __init__(self):
        pass

    def __del__(self):
        pass

    def WriteOutputFastA(self, filename, sequence_name, sequence):

        f = open(filename, 'w')
        f.write(">" + sequence_name + "\n")
        f.write(sequence)
        f.close()
