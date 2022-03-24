# XTern2020

## I) Overview
The XTern2020 dataset is a very interesting dataset. It has a lot of variables, such as ratings or average cost, to analyze the data and has many missing data. After analyzing the XTern2020 dataset, I draw 4 conclusions: 
  1) The longitude and latitude does not have affect on the rating, votes, reviews, average cost, minimum order, or cooking time. 
  2) Many people will tend to use the delivery system with different types of cuisines.
  3) The most trending delievery system is the one with 7 different cuisines.
  4) The optimized average cooking time is 40 minutes.

## II) Conclusion 1:
When I first comes to the data, I see that the data has a variety of different longitude and latitude. So I ask myself that can a particular zone be favored more than other zones? Therefore, I use Flourish ( an online data visualization which has similar mechanics to Tableau) to graph the longitude and latitude combining with other variables. 

![](ScatterPlot/Rating%20(%20Latitude%20and%20Longitude).png)
![](ScatterPlot/Votes%20(%20Longitude%20and%20Latitude).png)
![](ScatterPlot/Reviews%20(%20Longitude%20and%20Latitude).png)
![](ScatterPlot/Average%20Cost%20(%20Longitude%20and%20Latitude).png)
![](ScatterPlot/Minimum%20Order%20(%20Latitude%20and%20Longitude).png)
![](ScatterPlot/Average%20Cost%20(%20Longitude%20and%20Latitude).png)

Note: From the top to the bottom: rating, votes, reviews, average cost, minimum order, and cooking time

However, from all the scatterplots above, I could not see any relationships between the location and other factors.Therefore, I draw a hypothesis conclusion that the location from this data has no affect to the rating, votes, reviews, average cost, minimum order, or cooking time.

 Also, one aspect I notice in the scatter plot 2 and scatter plot 3 is that they are not really different much. Maybe, their correlation is really close to 1.

## III) Conclusion 2:
### 1) Analysis of the rating, reviews, and votes:
Leaving the longitude and latitude behind, I find the Cuisines variable very interesting. It has a lot of unique values and has different combinations. So, I create dummy variable "Count_Cuisines" to calculate the different types of cuisines a delivery system has in each delivery system. Then, I create a pivot table with the Count_Cuisines as the index and average of ratings, votes, and reviews to see how do people think about the different delivery system.

![](ScatterPlot/Reviews%20and%20Cost.png)
![](ScatterPlot/Average%20Rating.png)

The first scatter plot shows the relationship of the average of votes and average of reviews. In the graph, the votes dots and the reviews dots are really close to each other. Therefore, I calculate the correlation of the votes and the reviews. The result is 0.9644514962195193. It is really close to one. Therefore, their relation ship are really close to perfectly linear. In other words, they are highly related to each other and do not different from each other a lot. I can use votes to predict reviews and vice versa if either of them is hidden. Therefore, I choose to use the average of votes.

On the right hands, the scatter plot of the average ratings is very interesting. Similar to the first scatter plot, the average rating of delivery system with 1, 2, 3 cuisines are lower compared to the other delivery systems, especially the delivery system with 6 and 7 different cuisines. Both of them has the highest average ratings and highest average votings as well as the highest average reviews. 

However, two question appears in my head. What if many people use 1 or 2 cuisines delivery system and don't give ratings, votes, or reviews? What if not many people use 6 or 7 cuisines delivery systems? I think that to use the ratings and votes to determine a delivery system good or bad, we need a larger sample or have the same votes or reviews to avoid the most bias in the analysis. Therefore, it is still a little bias to say from this data that based on the average rating and average votes, people tend to use delivery system with more different cuisines rather than 1 or 2 cuisines 

### 2) Analysis of the average cost and minimum order:
To make my conclusion that people prefer delivery system with diverse cuisines more trustworthy, I analysis the average cost and minimum order. Therefore, I draw the graph with the x-axis is the count of cuisines, while the mean of the average cost (orange dots) and the mean of minimum order (blue dots) are the y axis.

![](ScatterPlot/AC%20and%20MO.png)

I cannot see much the difference from this scatter plot. Therefore, I create another variable which is to calculate the difference between the average cost (AC) and minimum order (MO). The scatter plot below demonstrate the count of cuisines and difference between AC and MO.

![](ScatterPlot/Difference%20in%20AC%20and%20MO.png)

From this scatter plot, I can strengthen my statement that people tend to buy from the delivery systems with more different cuisines. If you want to use a food with a delivery system, you might want to buy a lot of food without worrying more extra tips and services. Therefore, I think if the difference between AC and MO is near 0 means that your order only contains food and might get free deliveries. Lookiing at the scatter plot, the mean of difference between AC and MO of 1, 2, and 3 cuisines is the highest. I assume that they charge a lot of services fee. Therefore, they don't get the rating as high as other delivery systems like 6, 7, or 8 different cuisines.

Therefore, from the difference between AC and MO, average ratings, and average votes, I see that people tend to prefer the service with least difference in AC and MO. And they might think that diverse food cuisines can be better.

## III) Conclusion 3:
This is just my hypothesis. Since looking at the mean of difference between AC and MO, average ratings and average votes, the delivery system with 6 cuisines are always perform better than others. Also, this type of delivery system has the fairly low cooking time compared to other. 

![](ScatterPlot/Average%20Cooking%20Time.png)

## IV) Conclusion 4:
From the chart above and from conclusion 2 and 3, I think the most optimize cooking time will be around 40 and 41. Cooking too fast may reduce the quality of the food. Cooking too long will make many people wait and nobody want to wait.

## V) Further improvement:
I think my analysis has many flaws, but this is my first time and I use all my knowledge here. Another way to think of is to compare each type of food to see what type of food has higher ratings or an overrall of  food quality will improve this analysis.
