import matplotlib.pyplot as plt
import networkx as nx
from collections import defaultdict
import matplotlib.animation as animation
import sys
import numpy as np


def close_event():
    plt.close() #timer calls this function after 3 seconds and closes the window


matrix = []             # Field to store the input matrix
node_list = []

def creating_node_list(matrix):
    #This method creates a list of nodes on which we will iterate upon
    for i in range(0,len(matrix)):
        node_list.append(i)

def extract_min(temp_dict):
    min = float("inf")
    lowest_key = None
    for key in temp_dict.keys():
        if temp_dict[key] < min:
            min = temp_dict[key]
            lowest_key = key

    del temp_dict[lowest_key]
    return lowest_key


def dijkstra(source,matrix):

    matrix_dict = defaultdict(list)
    distance_dict = defaultdict()
    prev_dict = defaultdict()
    temp_dict = defaultdict()
    #Dictionary to hold the graph neighbors
    neighbors_set = defaultdict(list)

    #Neighbors with distances
    #This gets the neighbors of the graph with keys as nodes and a list of tuples as their neighbors, where each tuple
    #contains neighbpors and distances
    #{0: [(1, 4), (3, 2)], 1: [(0, 4), (2, 8), (4, 5)], 2: [(1, 8), (3, 3)], 3: [(0, 2), (2, 3), (4, 4)], 4: [(1, 5), (3, 4)]}
    for i in matrix:
        k = 0
        for j in i:
            if int(j) > 0:
                matrix_dict[matrix.index(i)].append((k,int(j)))
            k += 1

    #Neighbors of the nodes:
    #This gets the neighbors of the graph with keys as nodes and a list of values as their neighbors
    #For example it will be of the form
    #{0: [1, 3], 1: [0, 2, 4], 2: [1, 3], 3: [0, 2, 4], 4: [1, 3]})
    for i in matrix:
        k = 0
        for j in i:
            if int(j) > 0:
                neighbors_set[matrix.index(i)].append(k)
            k += 1


    #Initialiazing each nodes distance to -1
    for i in node_list:
        distance_dict[i] = float("inf")
    #Initialiazing all previous_dicr to -1
    for i in node_list:
        prev_dict[i] = float("inf")

    #Initialiazing Source to 0
    distance_dict[source] = 0
    for key in distance_dict.keys():
        temp_dict[key] = distance_dict[key]




    #Doing this loop to add all distances from the souce to its neighbors
    k = 0
    for i in matrix:
        if matrix.index(i) == source:
            for j in i:
                if int(j) > 0:
                    distance_dict[k] = int(j)
                k += 1

    extract_min(temp_dict)





    print(distance_dict)


    #while len(temp_nodelist) != 0:


    

# Menu of the Link State Routing Simulator
# Keeping it in a infinite loop; breaks only if the user enters 6
while(1):
    print(" ")
    print("CS542 LINK STATE ROUTING SIMULATOR")
    print("----------------------------------")
    print("(1) Create a Network Topology ")
    print("(2) Draw Graph of Input Topology")
    print("(3) Build a Connection Table")
    print("(4) Shortest Path to Destination Router")
    print("(5) Modify a Topology")
    print("(6) Best Router for Broadcast")
    print("(7) Exit")
    print("----------------------------------")
    print(" ")
    user_input = input("Please enter the command:")


#TODO Making user input the file1

    if user_input == str(1):

        matrix = []
        try:
            config_file = open("matrix.txt",'r')    #Opening the input file
            for line in config_file:
                matrix.append(line.strip("\n").split())

            path = []
            matrix_row_length = len(matrix[0])

        except:
            print("Please enter a valid filepath.....")

        creating_node_list(matrix)  # Creating a list of nodes

    elif user_input == str(2):
        G = nx.Graph()  # Initialiazing graph
        fig = plt.figure()
        timer = fig.canvas.new_timer(
            interval=5000)  # creating a timer object and setting an interval of 3000 milliseconds
        timer.add_callback(close_event)
        for i in matrix:
            k = 0
            for j in i:
                if int(j) > -1:
                    G.add_edge(matrix.index(i) + 1, k + 1, weight=j)  # Adding edges to the graph
                k += 1

        nx.draw(G, with_labels=True)  # Drawing Graph
        timer.start()
        plt.show()  # Showing the graph

    elif user_input == str(3):
        try:
            source_input = int(input("Enter the source node:"))
            distance,prev = dijkstra(source_input,matrix)


        except ValueError:
            print("Please Enter a number")


