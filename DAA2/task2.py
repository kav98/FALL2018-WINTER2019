#SOFE3770 Assignment 2
#Kavya Raman, 100615001
#Due: Nov 13th, 2018
#task2: Assignment problem
####
#Input: 5 x 5 matrix of non-negative values inidicating time cost of each job per employee
#Output: binary matrix coresponding to optimal employee for each job

import numpy as np


class AssignWork:

    def __init__(self):
        maintrix = np.array(input_matrix) #maintrix = main matrix
        self.input_matrix = np.array(input_matrix)

        self.cost_m = maintrix #duplicate maintrix for cost matrix
        self.size = len(maintrix)
        self.assignments = [] #resulting array with job assignments

    def calculate(self):
        if input_matrix is None and self.cost_m is None:
            print "error: invalid input"
        elif input_matrix is not None:
            self.__init__(input_matrix)


        result_m = self.cost_m.copy()


        #subtract row min from each row
        for index, row in enumerate(result_m):
            result_m[index] -= row.min()

        #subtract column min from each column
        for index, column in enumerate(result_m.T):#transpose matrix to make parsing easier
            result_m[,index] -= column.min()

        #use minimum lines to cover all zeros
        total_covered = 0
        while total_covered < self.size:
            cover_zeros = CoverZeros(result_m)
            rows_covered = cover_zeros.get_rows_covered
            columns_covered = cover_zeros.get_column
            total_covered = len(rows_covered) + len(columns_covered)

            #recalculates matrix values to reveal better solution, recalculates until there is at least one zero in each row
            if total_covered < self.size:
                result_m = matrix_adjust(result_m, rows_covered, columns_covered)


        #find single zeros in rows and columns and add them to the assignment, remove them after
        total_assignments = 5
        zero_loc = (result_m == 0)
        while len(self.assignments) != 5:
            row_matches, column_matches = self.find_matches(zero_loc)


    
    def matrix_adjust:
        #subtract x from every uncovered number and add x to any number covered twice
    def find_matches:
