import matplotlib.pyplot as plt
# plot blank chart
fig, ax= plt.subplots()
plt.show()

# define values
x = [1,2,3,4,5,6]
y = [1,2,3,4,5,6]
z = [2,4,6,8,10,12]

# plot line chart
plt.plot(x,y)
plt.show()
# plot bar chart
plt.bar(x,y)
plt.show()
# plot scatter chart
plt.scatter(x,y)
plt.show()
# plot multiple chart together
plt.scatter(x,y)
plt.plot(x,z)
plt.show()
# change line style
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
plt.plot(x,z, linestyle="dashed")
plt.show()
# change marker
# https://matplotlib.org/stable/api/markers_api.html
plt.plot(x,z, marker="v")
plt.show()
# change color
# https://matplotlib.org/stable/gallery/color/named_colors.html
plt.plot(x,z, color="r")
plt.show()
# implement chart from real time data
plt.plot(x,z, linestyle="dashed",marker="o",color="r")
plt.show()
