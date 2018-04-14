import networkx as nx
from os import listdir
from numpy import mean
from statistics import stdev
from time import time
import gc

# Assume exchanges are the nodes in the 99th percentile for degree
def removeExchanges(G):
    nodeDegrees = list(G.degree(list(G.nodes())))
    onlyDegrees = [i[1] for i in nodeDegrees]
    cutoff = mean(onlyDegrees) + (3 * stdev(onlyDegrees))
    print("Cutoff: " + str(cutoff))

    removedNodesAndDegrees = dict()

    for node in nodeDegrees:
        if node[1] > cutoff:
            removedNodesAndDegrees[node[0]] = node[1]
            G.remove_node(node[0])

    removedNodesAndDegrees[-1] = cutoff
    return removedNodesAndDegrees



def removeSelfLoops(G):
    selfLoopNodes = list(nx.nodes_with_selfloops(G))
    for selfLoopNode in selfLoopNodes:
        G.remove_edge(selfLoopNode, selfLoopNode)

def numberOf2NodeNetworks(G):
    nodes = list(G.nodes())
    num2NodeNetworks = 0
    searchedNodes = set()
    for node in nodes:
        if node not in searchedNodes:
            searchedNodes.add(node)

            nodesEdges = G.edges(node)

            # If the current Node only has 1 neighbor
            if len(nodesEdges) == 1:
                neighborsEdges = G.edges(list(nodesEdges)[0])

                # If my neighbor also only has one neighbor, we are a network of 2
                if len(neighborsEdges) == 1:
                    num2NodeNetworks = num2NodeNetworks + 1

                # Since at this point we know if the neighbor is part of our 2 node network
                # or not we can add it to the searched list
                    searchedNodes.add(list(neighborsEdges)[0])

    return num2NodeNetworks


def compareAddressOverlap():
    # Import all the address maps
    files = listdir("Address Maps/")
    addressMaps = [dict() for i in range(0, len(files))]
    for fileIndex, fileName in enumerate(files):
        file = open("Address Maps/" + fileName, "r")
        line = file.readline()
        while line:
            line = line.split(" ")
            hashAddress = line[0]
            intAddress = line[1]
            addressMaps[fileIndex][hashAddress] = intAddress
            line = file.readline()

    overlapValues = [ [-1 for i in range(len(addressMaps))] for j in range(len(addressMaps))]
    for mapIndex, map1 in enumerate(addressMaps):
        for mapIndex2, map2 in enumerate(addressMaps):
            if mapIndex != mapIndex2 and overlapValues[mapIndex][mapIndex2] == -1:
                overlap = findOverlap(addressMaps[mapIndex], addressMaps[mapIndex2])
                overlapValues[mapIndex][mapIndex2] = overlap
                overlapValues[mapIndex2][mapIndex] = overlap
    file.close()
    return overlapValues

def findOverlap(Dict1, Dict2):
    counter = 0;
    for key1 in Dict1:
        if key1 in Dict2:
            counter += 1
    return counter

def averageDegree(G):
    total = 0
    for node in G.nodes():
        total += G.degree(node)

    return total / len(G.nodes())

def averagePageRank(G):
    pr = nx.pagerank(G)

    total = 0
    for key, value in pr.items():
        total += value
    return total / len(G.nodes())



files = listdir("Integer Graphs/")

allFeatures = [dict() for i in range(0, len(files))]
outFile = open("Output.txt", "w")
for fileIndex, file in enumerate(files):
    # Import the graph
    G = nx.read_edgelist("Integer Graphs/" + file, delimiter=',', nodetype=int)
    outFile.write(file + "\n")
    print(file)
    removeSelfLoops(G)

    outFile.write('\t' + "Using the regular sample graph:" + '\n')
    print("\tUsing regular graph")

    start = time()

    print("\t\tDegree")
    temp = averageDegree(G)
    allFeatures[fileIndex]["reg average degree"] = temp
    outFile.write('\t\t' + "Average Degree " + str(temp) + '\n')
    print('\t\t\t' + str(time() - start))

    print("\t\tNodes")
    temp = len(nx.nodes(G))
    allFeatures[fileIndex]["reg number nodes"] = temp
    outFile.write('\t\t' + "Number of Nodes: " + str(temp) + '\n')
    print('\t\t\t' + str(time() - start))

    print("\t\tpagerank")
    temp = averagePageRank(G)
    allFeatures[fileIndex]["reg pagerank"] = temp
    outFile.write('\t\t' + "Page Rank: " + str(temp) + '\n')
    print('\t\t\t' + str(time() - start))

    print("\t\t2node")
    temp = numberOf2NodeNetworks(G)
    allFeatures[fileIndex]["reg 2 node networks"] = temp
    outFile.write('\t\t' + "Number of 2 Node Sub-Networks: " + str(temp) + '\n')
    print('\t\t\t' + str(time() - start))

    print("\t\tEdges")
    temp = len(nx.edges(G))
    allFeatures[fileIndex]["reg number edges"] = temp
    outFile.write('\t\t' + "Number of Edges: " + str(temp) + '\n')
    print('\t\t\t' + str(time() - start))

    print("\tremoving exchanges")
    temp = removeExchanges(G)
    with open(str(file) + "removedNodes.txt", 'w') as exFile:
        exFile.write("The cutoff was " + str(temp[-1]) + '\n')
        exFile.write("Node Removed\tDegree\n")
        total = 0
        for key, value in temp.items():
            exFile.write(str(key) + "\t\t\t" + str(value) + '\n')
            total += value
        total /= len(temp)
        exFile.write("There were " + str(len(temp)) + " nodes removed with an average degree of " + str(total))



    outFile.write('\t' + "Using the same network with the Bitcoin Exchanges removed" + '\n')

    print("\t\tDegree")
    temp = averageDegree(G)
    allFeatures[fileIndex]["rem average degree"] = temp
    outFile.write('\t\t' + "Average Degree: " + str(temp) + '\n')
    print('\t\t\t' + str(time() - start))

    print("\t\tNodes")
    temp = len(nx.nodes(G))
    allFeatures[fileIndex]["rem number nodes"] = temp
    outFile.write('\t\t' + "Number of Nodes: " + str(temp) + '\n')
    print('\t\t\t' + str(time() - start))

    print("\t\tpagerank")
    temp = averagePageRank(G)
    allFeatures[fileIndex]["rem pagerank"] = temp
    outFile.write('\t\t' + "Page Rank: " + str(temp) + '\n')
    print('\t\t\t' + str(time() - start))

    print("\t\tedges")
    temp = len(nx.edges(G))
    allFeatures[fileIndex]["rem number edges"] = temp
    outFile.write('\t\t' + "Number of Edges: " + str(temp) + '\n')
    print('\t\t\t' + str(time() - start))

    gc.collect()

outFile.close()
