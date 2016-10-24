import matplotlib.pyplot as plt
import networkx as nx
import sys
import numpy as np


# Menu of the Link State Routing Simulator
# Keeping it in a infinite loop; breaks only if the user enters 6
while(1):
    print(" ")
    print("CS542 LINK STATE ROUTING SIMULATOR")
    print("----------------------------------")
    print("(1) Create a Network Topology ")
    print("(2) Build a Connection Table")
    print("(3) Shortest Path to Destination Router")
    print("(4) Modify a Topology")
    print("(5) Best Router for Broadcast")
    print("(6) Exit")
    print("----------------------------------")
    print(" ")
    user_input = input("Please enter the command:")

    if user_input == str(1):

        matrix = []
        config_file = open("matrix.txt",'r')
        for line in config_file:
            matrix.append(line.strip("\n").split())

        k = np.matrix(matrix)
        print(k)

    else:
        break


