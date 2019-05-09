import matplotlib.pyplot as plt

"""line chart"""
input_value = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_value,squares,linewidth = 5)   # arguments: (data of x-axis,data of y-axis,linewidth)

plt.title("Square Numbers", fontsize = 24)    #arguments: (name of the chart,fontsize)
plt.xlabel("Value",fontsize = 14)             #arguments: (name of the x-axis,fontsize)
plt.ylabel("Square of value", fontsize = 14)  #arguments: (name of the y-axis,fontsize)
plt.tick_params(axis = 'both',labelsize = 14) #arguments: (axis = "x/y/both",labelsize = numeber)
plt.show()  # show the chart

"""scatter diagram"""

plt.scatter(input_value,squares,s = 100)  # arguments: s-->the size of the dots

plt.title("Square Numbers", fontsize = 24)    #arguments: (name of the chart,fontsize)
plt.xlabel("Value",fontsize = 14)             #arguments: (name of the x-axis,fontsize)
plt.ylabel("Square of value", fontsize = 14)  #arguments: (name of the y-axis,fontsize)
plt.tick_params(axis = 'both',labelsize = 14) #arguments: (axis = "x/y/both",labelsize = numeber)
plt.show()  # show the chart

"""1000 dots"""
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values,y_values,edgecolor = 'none',c = 'green',s = 2)  # edgecolor-->change the outline of the line;
                                                                     # c-->change the color of the line,the color can be done by names or RGB-->(0,0,0.8)

plt.title("Square Numbers", fontsize = 24)    #arguments: (name of the chart,fontsize)
plt.xlabel("Value",fontsize = 14)             #arguments: (name of the x-axis,fontsize)
plt.ylabel("Square of value", fontsize = 14)  #arguments: (name of the y-axis,fontsize)
plt.tick_params(axis = 'both',labelsize = 14) #arguments: (axis = "x/y/both",labelsize = numeber)
plt.axis([0,1100,0,1100000])                  # set the range of the x and y axis-->[Min of x,Max of x,Min of y,Max of y]
plt.show()


"""use colormap"""
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values,y_values,edgecolor = 'none',c = y_values,cmap = plt.cm.Reds,s = 2)  # edgecolor-->change the outline of the line;
                                                                     # c-->change the color of the line,the color can be done by names or RGB-->(0,0,0.8)
                                                                     # c = y_values,amap = plt.cm.Reds-->make the trend of varing more visualizable
plt.title("Square Numbers", fontsize = 24)    #arguments: (name of the chart,fontsize)
plt.xlabel("Value",fontsize = 14)             #arguments: (name of the x-axis,fontsize)
plt.ylabel("Square of value", fontsize = 14)  #arguments: (name of the y-axis,fontsize)
plt.tick_params(axis = 'both',labelsize = 14) #arguments: (axis = "x/y/both",labelsize = numeber)
plt.axis([0,1100,0,1100000])                  # set the range of the x and y axis-->[Min of x,Max of x,Min of y,Max of y]
plt.show()

"""save the chart as image"""
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values,y_values,edgecolor = 'none',c = y_values,cmap = plt.cm.Reds,s = 2)  # edgecolor-->change the outline of the line;
                                                                     # c-->change the color of the line,the color can be done by names or RGB-->(0,0,0.8)
                                                                     # c = y_values,amap = plt.cm.Reds-->make the trend of varing more visualizable
plt.title("Square Numbers", fontsize = 24)    #arguments: (name of the chart,fontsize)
plt.xlabel("Value",fontsize = 14)             #arguments: (name of the x-axis,fontsize)
plt.ylabel("Square of value", fontsize = 14)  #arguments: (name of the y-axis,fontsize)
plt.tick_params(axis = 'both',labelsize = 14) #arguments: (axis = "x/y/both",labelsize = numeber)
plt.axis([0,1100,0,1100000])                  # set the range of the x and y axis-->[Min of x,Max of x,Min of y,Max of y]
# plt.savefig('1.png',bbox_inches = 'tight')  # save the chart as images; bbox_inches = 'tight'-->cut the excessive blank spaces
