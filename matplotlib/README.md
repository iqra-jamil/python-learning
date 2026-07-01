# Matplotlib — Bar chart, line graph, pie chart from real data

## What is Matplotlib?

Matplotlib is a Python library used for creating graphs and visualizations, like line charts, bar charts, scatter plots, and histograms. It's one of the most widely used plotting libraries in Python, especially for data analysis and scientific work, and it gives you fine control over how your charts look (colors, labels, styles, etc.).

## Pyplot

Most of the Matplotlib utilities lies under the pyplot submodule

## Bar Chart

- Definition: A bar chart represents data using rectangular bars whose length/height is proportional to the value they represent.
- Use: It's used to compare quantities across different categories (e.g., sales by month, population by country).

### Creating Bars

- we can use bar() function of pyplot to draw a bar graph
- The bar() function takes arguments that describes the layout of the bars.

### Horizontal Bars

- If we want the bars to be displayed horizontally instead of vertically, we can use the barh() function

### Bar Color

- The bar() and barh() take the keyword argument color to set the color of the bars
- we can use any of the 140 supported color names.

### Bar Width

- The bar() takes the keyword argument width to set the width of the bars
- The default width value is 0.8

### Bar Height

- The barh() takes the keyword argument height to set the height of the bars.

## line graph

- Definition: A line graph displays data points connected by straight lines, usually showing how values change over a continuous range (like time).
- Use: It's used to show trends or patterns over time (e.g., stock prices over months, temperature over days).

- we can give only one array ,when we will specify one array only the matplotlib will assume it's the y-values and automatically uses the index positions (0, 1, 2, 3...) as the x-values.

### Linestyle

- we can use the keyword argument linestyle, or shorter ls, to change the style of the plotted line

### Shorter Syntax

The line style can be written in a shorter syntax:

- linestyle can be written as ls.

- dotted can be written as :.

- dashed can be written as --.

### Line Color

- we can use the keyword argument color or the shorter c to set the color of the line

### Line Width

- we can use the keyword argument linewidth or the shorter lw to change the width of the line.

### Multiple Lines

we can also specify 2 x,2 y points for multiple lines

## pie chart

- Definition: A pie chart is a circular graph divided into slices, where each slice's size represents its proportion of the whole.
- Use: It's used to show the relative proportions or percentages of categories that make up a total (e.g., market share, budget allocation).

### Creating Pie Charts

- With Pyplot,we can use the pie() function to draw pie charts
- one piece of pie chart is called wedge
- pie chart draws one wedge for each value
- By default the plotting of the first wedge starts from the x-axis and moves anticlockwise

### Labels

- Add labels to the pie chart with the labels parameter.

- The labels parameter must be an array with one label for each wedge

### Start Angle

- the default start angle is at the x-axis, but we can change the start angle by specifying a startangle parameter.
- The startangle parameter is defined with an angle in degrees, default angle is 0

### Explode

- Maybe we want one of the wedges to stand out The explode parameter allows uss to do that.

- The explode parameter must be an array with one value for each wedge.

- Each value represents how far from the center each wedge is displayed

### Shadow

- Add a shadow to the pie chart by setting the shadows parameter to True

### Colors

- we can set the color of each wedge with the colors parameter.

- The colors parameter must be an array with one value for each wedge

### Legend

- To add a list of explanation for each wedge, use the legend() function

### Legend With Header

- To add a header to the legend, add the title parameter to the legend function
