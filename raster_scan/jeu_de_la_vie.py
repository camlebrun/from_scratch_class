import numpy
import time
import os


frame = numpy.array([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]])

def compute_number_alive_neighbor(paded_frame, index_line, index_column):
    number_alive_neighbor = paded_frame[index_line-1][index_column-1] + paded_frame[index_line-1][index_column] + paded_frame[index_line-1][index_column+1] +\
                            paded_frame[index_line][index_column-1]                                             + paded_frame[index_line][index_column+1] +\
                            paded_frame[index_line+1][index_column-1] + paded_frame[index_line+1][index_column] + paded_frame[index_line+1][index_column+1] 


    return number_alive_neighbor





def compute_next_frame(frame):
    paded_frame = numpy.pad(frame, 1, mode="constant")

    for index_line in range(0, frame.shape[0]): #abscisse donc 0
        for index_column in range(0, frame.shape[1]): #ordonné donc 1
            number_alive_neighbor = compute_number_alive_neighbor(paded_frame, index_line+1, index_column+1)
            
            if frame[index_line][index_column] == 0 and number_alive_neighbor == 3:
                frame[index_line][index_column] = 1

            elif frame[index_line][index_column]==1 and not (number_alive_neighbor==2 or number_alive_neighbor==3):
                frame[index_line][index_column] = 0


while True:
    os.system("clean")
    print(frame)
    time.sleep(1)
    compute_next_frame(frame)