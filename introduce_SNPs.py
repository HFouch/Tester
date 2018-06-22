from class_Genome_Mutation import GenomeMutation
from class_Genome_Mutation import WriteOutputFile
from class_FastA import FastA

if __name__ == "__main__":
    input_filename = '/home/18969577/Documents/Genolve/Data_manipulation/Test_Data/Test_Genome_sequence.fasta'
    input_file = FastA()
    number_of_sequences = input_file.ReadFastA(input_filename)
    print("sequences = ", number_of_sequences)
    mutate_genome = GenomeMutation()
    path, *remainder = input_filename.rpartition('/')
    for index, sequence in enumerate(input_file):
        mutated_sequence = mutate_genome.SNPIntroduction(sequence, 20)
        print(mutated_sequence[0:20])
        out_file = input_file.GetContigName(index)
        sequence_name = out_file + '_MUTATED'
        print(sequence_name)
        out_file = path + '/' + out_file + '_MUTATED' + '.fasta'
        output_file = WriteOutputFile()
        output_file.WriteOutputFastA(out_file, sequence_name, mutated_sequence)

