import matplotlib.pyplot as plt
 
# x-coordinates of left sides of bars 
left = [1, 2, 3, 4, 5,6,7,8,9,10]
 
# heights of bars
height = [4188, 3788, 3429, 3356, 3038, 2969, 2657, 2657, 2483, 2475]
 
# labels for bars
tick_label = ['iHeartAwards', 'people', 'know', 'love', 'BTS_twt', 'time', 'day', 'BestFanArmy', 'today', '2018']
 
# plotting a bar chart
#plt.bar(left, height, tick_label = tick_label,
#        width = 0.5, color = ['red', 'blue'])


# to plot scatter dotted plot
plt.scatter(tick_label,height ,label= "stars", color= "m", 
            marker= "*", s=30)

# naming the x-axis
plt.xlabel('most frequent words from tweets')
# naming the y-axis
plt.ylabel('no. of times they appeared')
# plot title
plt.title('twitter data analysis')
 
# function to show the plot
plt.show()