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
            print("error: invalid input")
        elif input_matrix is not None:
            self.__init__(input_matrix)


        result_m = self.cost_m.copy()


        #subtract row min from each row
        for index, row in enumerate(result_m):
            result_m[index] -= row.min()

        #subtract column min from each column
        for index, column in enumerate(result_m.T):#transpose matrix to make parsing easier
            result_m[:,index] -= column.min()

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

        for row in row_matches:
            zero_loc[row] = False
        for column in column_matches:
            zero_loc[:, column] = False

        result_list = zip(row_matches,column_matches)
        self.assignments.append(result_list)
    
    def matrix_adjust(self, result_matrix, covered_rows, covered_columns):
        #subtract x from every uncovered number and add x to any number covered twice
        items = []
        for index_row, row in enumerate(result_m):
            if index_row not in rows_covered:
                for index, item in enumerate(row):
                    if index not in columns_covered:
                        items.append(item)
        min_num_uncovered = min(item)

        adjusted_m = result_m
        for row in rows_covered:
            adjusted_m(row) += min_num_uncovered
        for column in columns_covered:
            adjusted_m[:, column] += min_num_uncovered

        temp_m = np.ones(maintrix.shape, dtype=int) * min_num_uncovered
        adjusted_m -= temp_m

        return adjusted_m

    def find_matches(self, zero_loc):#retrun rows/columns with matches
        marked_rows = np.array([], dtype=int)
        marked_columns = np.array([], dtype=int)

        for index, row in enumerate(zero_loc):
            row_index = np.array([index])
            if np.sum(row) == 1:
                column_index, = np.where(row)
                marked_rows, marked_columns = self.mark_rowcolumns(marked_rows, marked_columns, row_index, column_index)

        for index, column in enumerate(zero_loc.T):
            column_index = np.array([index])
            if np.sum(column) == 1:
                row_index, = np.where(column)
                marked_rows, marked_columns = self.mark_rowcolumns(marked_rows, marked_columns, row_index, column_index)

        return marked_rows, marked_columns

    def mark_rowcolumns(marked_rows, marked_columns, row_index, column_index):
        temp_rows = marked_rows
        temp_columns = marked_columns


class CoverZeros:

    def __init__(self, matrix):
        
        


if __name__ == '__main__':
    profit_matrix = [
        [10, 5 13, 15, 16],
        [3, 9, 18, 13, 6],
        [10, 7, 2, 2, 2],
        [7, 11, 9, 7, 12],
        [7, 9, 10, 4, 12]
    ]
    assign = AssignWork(profit_matrix)
    assign.calculate()
