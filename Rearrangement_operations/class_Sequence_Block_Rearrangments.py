import numpy as np

class EdgeSeries:
    def __init__(self):
        pass

    def __del__(self):
        pass


    def GenerateEdgesSeries(self, filenameB):

        strB = np.loadtxt(filenameB, delimiter='\t', unpack=True, dtype=object)
        sequence_blocks = strB[0, :]
        edge_list = []

        for i in range(0, len(sequence_blocks)-1):
            if int(sequence_blocks[i+1]) - int(sequence_blocks[i]) == 1:
                pass
            elif int(sequence_blocks[i+1]) - int(sequence_blocks[i]) == -1:
                pass
            else:
                edge = (int(sequence_blocks[i]), int(sequence_blocks[i+1]))
                edge_list.append(edge)

        return edge_list

    def GenerateNewEdgesSeries(self, sequence_blocks):

        edge_list = []

        for i in range(0, len(sequence_blocks)-1):
            if int(sequence_blocks[i+1]) - int(sequence_blocks[i]) == 1:
                pass
            elif int(sequence_blocks[i+1]) - int(sequence_blocks[i]) == -1:
                pass
            else:
                edge = (int(sequence_blocks[i]), int(sequence_blocks[i+1]))
                edge_list.append(edge)
        print(edge_list)
        return edge_list

class MoveSequenceBlock:
    def __init__(self):
        pass

    def __del__(self):
        pass

    def MoveBlock(self, sequence_blocks_filename, current_edge):
        strB = np.loadtxt(sequence_blocks_filename, delimiter='\t', unpack=True, dtype=object)
        sequence_block_names = strB[0, :]


        sequence_blocks = []
        for i in range(0, len(sequence_block_names)):
            sequence_blocks.append(sequence_block_names[i])


        if current_edge[0] > current_edge[1]:
            lower_edge = current_edge[1]
            upper_edge = current_edge[0]
        else:
            lower_edge = current_edge[0]
            upper_edge = current_edge[1]

        lower_edge_position = sequence_blocks.index(str(lower_edge))
        upper_edge_position = sequence_blocks.index(str(upper_edge))


        lower_adjacent_edge = int(lower_edge) + 1
        lower_adjacent_edge_position = sequence_blocks.index(str(lower_adjacent_edge))

        upper_adjacent_edge = int(upper_edge) - 1
        upper_adjacent_edge_position = sequence_blocks.index(str(upper_adjacent_edge))

        if lower_adjacent_edge_position < upper_adjacent_edge_position:
            compatible_sequence_block = sequence_blocks[lower_adjacent_edge_position:upper_adjacent_edge_position + 1]
            compatible_sequence_block_start_position = lower_adjacent_edge_position
            compatible_sequence_block_end_position = upper_adjacent_edge_position + 1
        else:
            compatible_sequence_block = sequence_blocks[upper_adjacent_edge_position:lower_adjacent_edge_position + 1]
            compatible_sequence_block_start_position = upper_adjacent_edge_position
            compatible_sequence_block_end_position = lower_adjacent_edge_position + 1

        if int(compatible_sequence_block[0]) < int(compatible_sequence_block[len(compatible_sequence_block)-1]):
            pass
        else:
            compatible_sequence_block = list(reversed(compatible_sequence_block))

        new_sequence_blocks = sequence_blocks
        for i in range(0, len(compatible_sequence_block)):
            new_sequence_blocks.remove(compatible_sequence_block[i])

        new_lower_edge_position = new_sequence_blocks.index(str(lower_edge))
        new_upper_edge_position = new_sequence_blocks.index(str(upper_edge))

        if new_lower_edge_position < new_upper_edge_position:
            new_sequence_blocks = new_sequence_blocks[:int(new_lower_edge_position)+1] + compatible_sequence_block + new_sequence_blocks[int(new_upper_edge_position):]
        else:
            compatible_sequence_block = list(reversed(compatible_sequence_block))
            new_sequence_blocks = new_sequence_blocks[
                                  :int(new_upper_edge_position) + 1] + compatible_sequence_block + new_sequence_blocks[int(new_lower_edge_position):]

        return new_sequence_blocks


class WriteArrayToTextFile:
    def __init__(self):
        pass
    def __del__(self):
        pass

    def WriteToTxt(self, list, output_filename):
        text_file = open(output_filename, 'w')
        array = list
        text_file.write(str(array))
        text_file.close()
