import random

class GenomeMutation:
    def __init__(self):
        pass

    def __del__(self):
        pass

    def SNPIntroduction(self, template_sequence, SNP_frequency):
        random.seed()
        new_sequence = template_sequence
        SNP_count = 0
        SNP_changes = []
        number_of_windows = int(len(new_sequence)/SNP_frequency)
        print(number_of_windows)
        for i in range (0, number_of_windows-1):
            position = random.randint(i*SNP_frequency, i*SNP_frequency+SNP_frequency-1)

            while True:
                SNP = random.choice('ACTG')

                if new_sequence[position] == SNP:
                    continue

                if new_sequence[position] != SNP:
                    new_sequence = new_sequence[0:position] + SNP + new_sequence[position+1:]
                    SNP_count += 1
                    SNP_changes.append((position, SNP))
                    break

        return new_sequence

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

