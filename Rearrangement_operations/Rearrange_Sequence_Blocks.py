import numpy as np
from class_Sequence_Block_Rearrangments import EdgeSeries
from class_Sequence_Block_Rearrangments import MoveSequenceBlock
from class_Sequence_Block_Rearrangments import WriteArrayToTextFile
from class_Check_edge_list import CheckEdgeList

if __name__ == "__main__":

    filenameB = '/home/18969577/Documents/Genolve/Shuffling/Sequence_block_rearrangements/GenomeB_names_positions'

    #Generation of list of sequence blocks
    names_and_positions_of_sequence_blocks = np.loadtxt(filenameB, delimiter='\t', unpack=True, dtype=object)
    sequence_block_names = names_and_positions_of_sequence_blocks[0, :]
    sequence_blocks = []
    for i in range(0, len(sequence_block_names)):
        sequence_blocks.append(sequence_block_names[i])
    print(sequence_blocks)

    #Generation of series of edges
    generate_edge_list = EdgeSeries()
    edge_list = generate_edge_list.GenerateEdgesSeries(filenameB)
    print(edge_list)

    # Removal of edges that falls within their compatible sequence blocks
    remove_nonviable_edge = CheckEdgeList()
    exclude_edge = remove_nonviable_edge.RemoveNonViableEdges(edge_list, sequence_blocks)
    edge_list = exclude_edge

    #Generation of new edge list after performing the applicable rearrangments
    new_edge_series = []
    for i in range(0, len(edge_list)):
        edge_number = int(i)
        current_edge = edge_list[edge_number]
        print(current_edge)

        #Execution of all possible rearrangment operations
        moving_sequence_blocks = MoveSequenceBlock()
        execute_sequence_block_shift = moving_sequence_blocks.MoveBlock(filenameB, current_edge)
        #Edge list generated from new intermediate genome
        new_edge_list = generate_edge_list.GenerateNewEdgesSeries(execute_sequence_block_shift)
        #List containing the list of edges for all intermediate genome possiblities
        new_edge_series.append(new_edge_list)

        #Generation of output files
        path, *remainder = filenameB.rpartition('/')
        output_filename = path + '/' + 'Sequence_blocks_moved_EdgeNumber_' + str(edge_number + 1) + '.txt'
        output_file = WriteArrayToTextFile()
        output_file.WriteToTxt(execute_sequence_block_shift, output_filename)

    #Generation of list containing, for each intermediat genome, the genome number and number of edges
    len_new_edge_lists = []
    for i in range(0, len(new_edge_series)):
        edge_list_number = int(i)
        edge_list_length = len(new_edge_series[edge_list_number])
        len_new_edge_lists.append((edge_list_number, edge_list_length))
    print(len_new_edge_lists)
    print(edge_list)
    print('New sequence block list written to ', path)
