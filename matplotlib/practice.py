import matplotlib.pyplot as plt
import numpy as np
list_x=[1,2,3]
list_y=[4,5,6]
plt.plot(list_x,list_y)
plt.show()

# BAR CHART

list_x=["X","Y","Z"]
list_y=[4,5,6]

arr_1=np.array(list_x)
arr_2=np.array(list_y)

plt.bar(arr_1,arr_2 ,color="red" ,width=0.1)
plt.show()

plt.barh(arr_1,arr_2,height=0.1)
plt.show()

# LINE GRAPH (plot())
y1points=np.array([3,8,1,10])
y2points = np.array([6, 2, 7, 11])
plt.plot(y1points, c="r" ,ls="dotted")
plt.plot(y2points, c="r")
plt.show()


#PIE CHART
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
my_explode=[0.2,0.5,0,0]
my_Colors=["black", "hotpink", "b", "#4CAF50"]
plt.pie(y , labels=mylabels, startangle=0, explode=my_explode,shadow=True,colors=my_Colors)
plt.legend(title='fruits')
plt.show()
