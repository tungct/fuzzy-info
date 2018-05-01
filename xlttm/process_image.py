import cv2
import numpy as np
from matplotlib import pyplot as plt
import networkx as nx

np.set_printoptions(threshold='nan')
arr_x = []
arr_y = []
def write_matrix_to_textfile(a_matrix, file_to_write):

    def compile_row_string(a_row):
        return str(a_row).strip(']').strip('[')

    with open(file_to_write, 'w') as f:
        for row in a_matrix:
            f.writelines(compile_row_string(row)+'\n')

    return True

def ConvertMatrix(a_matrix,x):
    for i in range(len(a_matrix)):
       for j in range(len(a_matrix[i])): 
           if a_matrix[i][j] >= x-3 & a_matrix[i][j] <= x+3:
               a_matrix[i][j] = 255 #white
           else :
               a_matrix[i][j] = 0    #black
    return a_matrix

def grayscale(file):
    image = cv2.imread(file)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('./gray_image/gray_image.png',gray_image)
    # write_matrix_to_textfile(gray_image,"matrix.txt")
    return gray_image
      
def scan(file):
    count = 0
    matrix = grayscale("./image/m12.png")
    while count < 256 : 
        # lower_black = np.array([0,0,0], dtype = "uint16")
        # upper_black = np.array([count,count,count], dtype = "uint16")
        # file_name = "./"+str(file)
        # image = cv2.imread(file_name)
        # black_mask = cv2.inRange(image, lower_black, upper_black)
        # cv2.imwrite('./image_scan/'+str(count)+'.png',black_mask)
        image = ConvertMatrix(matrix,count)
        cv2.imwrite('./image_scan/'+str(count)+'.png',image)
        count += 1

def printX(x,file):
    lower_black = np.array([0,0,0], dtype = "uint16")
    upper_black = np.array([x,x,x], dtype = "uint16")
    file_name = "./"+str(file)
    image = cv2.imread(file_name)
    black_mask = cv2.inRange(image, lower_black, upper_black)
    print black_mask.shape
    cv2.imwrite('./'+str(x)+'.png',black_mask)
def CheckFile():
    image = grayscale("./image/m.png")
    i = len(image)-1
    print image.shape
    while i >= 0:
        for j in range(len(image[i])): 
            if image[i][j] == 255:
                arr_y.append(len(image)-i-1)
                arr_x.append(j)
        i-=1        
    plt.plot(arr_x,arr_y, 'ro')
    plt.axis([0, 2000, 0, 2000])
    plt.show()
def graph():
    image = grayscale("./image/map_1.png")
    G = nx.DiGraph(image)
    pos = [[0,0], [0,1], [1,0], [1,1]]
    nx.draw(G,pos)
    plt.show()

scan("")