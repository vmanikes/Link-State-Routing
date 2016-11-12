import matplotlib.pyplot as plt
import networkx as nx
from collections import defaultdict
import matplotlib.animation as animation
import sys
import numpy as np


def close_event():
    plt.close() #timer calls this function after 3 seconds and closes the window



node_list = []          # Field to hold the list of nodes


def creating_node_list(matrix):
    #This method creates a list of nodes on which we will iterate upon
    matrix = np.array(matrix)
    for i in range(1,len(matrix)+1):
        node_list.append(i)


#Method to remove the minimum element from the dictionary
def extract_min(temp_dict):

    min = float("inf")
    lowest_key = None
    for key in temp_dict:
        if temp_dict[key] < min:
            min = temp_dict[key]
            lowest_key = key
    del temp_dict[lowest_key]       #Method to remove the element from the dictionary
    return lowest_key

def dijkstra(source,matrix):

    matrix_dict = defaultdict(list)
    distance_dict = defaultdict()
    prev_dict = defaultdict()
    temp_dict = defaultdict()

    #Neighbors with distances
    #This gets the neighbors of the graph with keys as nodes and a list of tuples as their neighbors, where each tuple
    #contains neighbpors and distances
    #{0: [(1, 4), (3, 2)], 1: [(0, 4), (2, 8), (4, 5)], 2: [(1, 8), (3, 3)], 3: [(0, 2), (2, 3), (4, 4)], 4: [(1, 5), (3, 4)]}
    for i in matrix:
        k = 1
        for j in i:
            if int(j) > 0:
                matrix_dict[matrix.index(i)+1].append((k,int(j)))
            k += 1

    #Initialiazing each nodes distance to -1
    for i in node_list:
        distance_dict[i] = float("inf")

    prev_dict[source] = '-'

    #Initialiazing Source to 0
    distance_dict[source] = 0

    #Creating a temporary dictionary which will help to perform the deletion operations
    for key in distance_dict.keys():
        temp_dict[key] = distance_dict[key]

    while temp_dict:
        lowest_key = extract_min(temp_dict)         #Extract the minimum element
        for value in matrix_dict[lowest_key]:       #Iterating over the minimum element's neighbors

            temp_distance = distance_dict[lowest_key] + value[1]
            #if the distance is better than what we had replace it
            if temp_distance < distance_dict[value[0]]:

                temp_dict[value[0]] = temp_distance
                distance_dict[value[0]] = temp_distance
                #add the previous distance
                prev_dict[value[0]] = lowest_key

    return distance_dict,prev_dict


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
    print("(5) Add a Router")
    print("(6) Remove a Router")
    print("(7) Best Router for Broadcast")
    print("(8) Exit")
    print("----------------------------------")
    print(" ")
    user_input = input("Please enter the command:")


#TODO Making user input the file1

    if user_input == str(1):
        matrix = []  # Field to store the input matrix
        try:
            config_file = open("matrix.txt",'r')    #Opening the input file
            for line in config_file:
                matrix.append(line.strip("\n").split()) #Transforming the input file to a matrix

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
            #Entering the source node and calculating the Dijkstra and shortest path to all nodes from the source
            source_input = int(input("Enter the source Router:"))
            distance,prev = dijkstra(source_input,matrix)
            #Using the copy of the prev for building the connection table
            conn_previous = prev.copy()
            print("CONNECTION TABLE")
            print("================")
            for key,value in conn_previous.items():
                if value == source_input:
                    conn_previous[key] = key
                print(key,"\t\t",distance[key],"\t\t\t",conn_previous[key])

            #Some exceptions to handle the faulty inputs from the user
        except Exception:
            print("Please Enter a valid Router within the range 1,",len(node_list))
        except ValueError:
            print("Please Enter a number")

    elif user_input == str(4):
        try:
            #Entering the placeholders for the source and destination to find the path from
            print("Select Router from the range 1,",len(node_list))
            path_source = int(input("Enter the source Router you wish to find the path:"))
            path_dest = int(input("Enter the Destination Router you wish to find the path:"))

            temp = path_dest
            #If the source and destination exceeds the number of nodes program breaks
            if path_source > len(node_list) or path_dest > len(node_list):
                break
            path = []
            #Appending paths from prev to the list
            path.append(path_dest)
            while True:
                #If source and destination are the same break
                if path_source == path_dest:
                    break
                if path_dest in prev:

                    path.append(prev[path_dest])
                    path_dest = prev[path_dest]

                    if path_dest == path_source:
                        break

            print("The shortest path from router ",path_source," to router ",temp,"is ",path[::-1],"with the cost of ",distance[temp])
        except Exception:
            print("Please Enter a valid node within the range 1,", len(node_list))

    elif user_input == str(5):

        print("Select the router from the range 1",len(node_list))
        add_router = int(input("Enter the source Router you wish to find the path:"))



    elif user_input == str(6):
        # Code block to remove a router from the matrix
        print(("Select the router from the range 1", len(node_list)))
        remove_router = int(input("Enter the Router you want to remove:"))
        matrix = np.array(matrix)
        # Removing the row and column specific to the input given
        matrix = np.delete( matrix, remove_router-1, 0)
        matrix = np.delete( matrix, remove_router-1, 1)

        print("\nThe updated Router Topology is:")
        print("=================================")
        print(matrix)
        node_list.clear()

        #Updating the nodelist
        for i in range(1,len(matrix)+1):
            node_list.append(i)

        print("\nThe list of Routers are:")
        print(node_list)
        matrix = matrix.tolist()


    elif user_input == str(7):
        broadcast_path = defaultdict(list)
        for i in range(len(node_list),0,1):
            broadcast_path[i].append(i)

