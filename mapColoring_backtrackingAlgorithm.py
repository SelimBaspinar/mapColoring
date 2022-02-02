import plotly.express as px
import numpy as matrix

countries = ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Falkland Islands", "Guyana", "Paraguay",
             "Peru", "Suriname", "Uruguay", "Venezuela"]

colors = ["blue", "green", "red", "yellow"]


def isCorrect(neighbor, color):
    
    # check for every edge
    for i in range(13):
        for j in range(i + 1, 13):
            if (neighbor[i][j] and color[j] == color[i]):
                return False
    return True
  

def mapColoring(neighbor, m, i, color):

    # if current index reached end
    if (i == 13):
  
        # if coloring is safe
        if (isCorrect(neighbor, color)):
  
            # Print the solution
            printSolution(color)
            return True
        return False
  
    # Assign each color from 1 to m
    for j in range(1, m + 1):
        color[i] = j
        # Recur of the rest vertices
        if (mapColoring(neighbor, m, i + 1, color)):
            return True
        color[i] = 0
    return False

  
def printSolution(color):
    print("\nSolution Exists:" " Following are the assigned colors ")
    for i in range(13):
        if color[i]==1:
            color[i]=colors[0]
        elif color[i]==2 :
            color[i]=colors[1]
        elif color[i]==3:    
            color[i]=colors[2]
        elif color[i]==4:
            color[i]=colors[3]
        elif color[i]==0 :  
            color[i]="white"
     
        print(color[i],end=" ")
    plot_choropleth(color)

  
def plot_choropleth(colormap):
  fig=px.choropleth(locationmode="country names",
                  locations=countries,
                  color=countries,
                  color_discrete_sequence=colormap,
                  scope="south america")
  fig.show()    
  
  


if __name__ == "__main__":

#border neighborhoods of the countries, Index refers to the country array
    neighbor = [
        [ 0, 1, 1, 1 ,0,0,0,0,1,0,0,1,0], 
        [ 1, 0, 1, 1 ,0,0,0,0,1,1,0,0,0], 
        [ 1, 1, 0, 0 ,1,0,0,1,1,1,1,1,1], 
        [ 1, 1, 0, 0 ,0,0,0,0,0,1,0,0,0], 
        [ 0, 0, 1, 0 ,0,1,0,0,0,1,0,0,1], 
        [ 0, 0, 0, 0 ,1,0,0,0,0,1,0,0,0], 
        [ 0, 0, 0, 0 ,0,0,0,0,0,0,0,0,0], 
        [ 0, 0, 1, 0 ,0,0,0,0,0,0,1,0,1], 
        [ 1, 1, 1, 0 ,0,0,0,0,0,0,0,0,0], 
        [ 0, 1, 1, 1 ,1,1,0,0,0,0,0,0,0], 
        [ 0, 0, 1, 0 ,0,0,0,1,0,0,0,0,0], 
        [ 0, 0, 1, 0 ,0,0,0,1,0,0,0,0,0], 
        [ 0, 0, 1, 0 ,1,0,0,1,0,0,0,0,0], 
    ]
    c = 4 # Number of colors
   
    color = [0 for i in range(13)]
  
    if (not mapColoring(neighbor, c, 0, color)):
        print ("Solution does not exist")
    colormap_test = {"Argentina": "blue", "Bolivia": "red", "Brazil": "yellow", "Chile": "yellow", "Colombia": "red",
                     "Ecuador": "yellow", "Falkland Islands": "yellow", "Guyana": "red", "Paraguay": "green",
                     "Peru": "green", "Suriname": "green", "Uruguay": "red", "Venezuela": "green"}    
    
    color_discrete_sequence=[colormap_test[c] for c in countries]
    if (not isCorrect(neighbor,color_discrete_sequence)):
        print ("\nSolution does not exist")
    else:    
        printSolution(color_discrete_sequence)





    

