"""
    This file aims to count the number of times the word
    bitch has been used in each episode of breaking bad and 
    then plot a graph of it.
"""

from os import listdir
#For getting the all the things in the folder
from os.path import isfile, join
#To get only files in the subtitles folder
import matplotlib.pyplot as plt 
from pylab import *


def count_bitch(folder = "subtitles"):
    """
        This function would count the number of bitch in each episode
        as well as plot the graph
    """
    
    #Find the list of all files in the subtitiles folder
    files = [ f for f in listdir(folder) if isfile(join(folder,f)) ]
    files.sort()
    
    data_list = []
    #Create the data for the y axis
    for f in files:
        file_name = "subtitles/" + f
        counter = 0
        with open(file_name, 'r') as searchfile:
            for line in searchfile:
                if 'bitch' in line:
                    counter +=1
        data_list.append(counter)
        
    labels_list = []
    #Create the label
    for i in range(7):
        labels_list.append("1x" + str(i+1))
    for j in range(3):
        for i in range(13):
            labels_list.append(str(j+2) + "x" + str(i+1))
    for i in range(16):
        labels_list.append("5x" + str(i+1))
    
    labels = tuple(labels_list)
    
    
    F = gcf()
    Size = F.get_size_inches()
    F.set_size_inches(Size[0]*3, Size[1]*2)
    #Size is set
    plt.plot(data_list)
    plt.xticks(range(len(labels)), labels, rotation=90)
    plt.xlabel("Episode")
    plt.ylabel("Number of bitch word")
    plt.subplots_adjust(bottom=0.2)
    #title
    plt.title("Jesse's bitch count")
    plt.savefig("/home/isthegeek/Web/bitch.png")
    #Save the file
    
    plt.clf()
def main():
    count_bitch()
    
if __name__=="__main__":
    main()
    

    