#!/usr/bin/env python
import csv
import sys

def read_matrix (name) :
    #file object
    f = open (name, "r")
    matrix = []
    rows = csv.reader (f, delimiter = ",", quotechar = "|")

    for row in rows :
        new_row = []
        for col in row :
            #add col to row
            new_row.append (int(col))
        #add row to matrix
        matrix.append (new_row)

    return matrix

def square_check (matrix) :
    flag = True
    #check rows
    n_rows = matrix.__len__()
    for row in matrix :
        n_cols = row.__len__()
        if n_cols != n_rows :
           flag = False

    return flag

def unit_check (matrix) :
    flag = True
    if (square_check (matrix)) :
        #Ok to continue
        n_rows = matrix.__len__()
        for i in range (n_rows) :
            for j in range (n_rows) :            
                if ( i ==j ) :
                    if (matrix[i][j]!=1):
			flag = False
                else :
                    if (matrix[i][j] != 0) :
                        print("-no unit")
                        flag = False
        return flag

def zero_check (matrix) :
    flag = True
    if (square_check (matrix)) :
        #Ok to continue
        n_rows = matrix.__len__()
        for i in range (n_rows) :
            for j in range (n_rows) :            
                if (matrix[i][j]!=1):
                    print("-no zero matrix")
                    flag = False
        return flag

def transpose (matrix) :
    n_rows = matrix.__len__()
    n_cols = 0
    for i in range(n_rows) :
	if (matrix[i].__len__() > n_cols) :
	   n_cols = matrix[i].__len__()
	
    new_matrix = [None] * n_cols

    for i in range(n_cols):
	new_matrix[i] = [None] * n_rows
    for i in range (n_cols) :
            for j in range (n_rows) :  
		try :
	          new_matrix[i][j] = matrix[j][i]  
		except :
		  new_matrix [i][j] = 0
		print new_matrix[i][j]," " ,
	    print "\n"

def multiply_scalar (matrix, scalar) :
    n_rows = matrix.__len__()
    print n_rows
    n_cols = 0

    for i in range(n_rows) :
       if (matrix[i].__len__() > n_cols) :
	   n_cols = matrix[i].__len__()

    print n_cols
    print n_rows
    for row in range(n_rows) :
	#	print row
        for col in range(n_cols) :
	#	print col
		try :
#		   new_matrix [row][col] = matrix[row][col]
	           print scalar*matrix[row][col]," " ,
		except :
#		  new_matrix [row][col] = 0
		  print 0,
	print "\n"

if __name__ == '__main__' :
	file = sys.argv[1]
	mat =read_matrix (file)
	print "this is your transpose matrix:"
	transpose(mat)
	number = int(raw_input("Scalar: "))
	multiply_scalar(mat, number)
	if square_check(mat) :
	   print "-square matrix"
	if unit_check(mat) :
	   print "-unit matrix"        
	if zero_check(mat):
	   print "-zero matrix"       
