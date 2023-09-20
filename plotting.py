from matplotlib import pyplot as plt

x = [1, 2, 3, 4]
y = [10, 100, 34, 33]
maxmarks = [100 for x in x]
minmarks = [33 for x in x]
plt.plot(x, y)
plt.scatter(x, y)
plt.plot(x, maxmarks)
plt.plot(x, minmarks)
plt.title("Marks")
plt.xlabel("Subject No")
plt.ylabel("Marks")

# plt.show()
plt.bar(x, y,color="pink")
plt.legend(["Marks", "Marks", "Max Marks", "Pass Marks", "Marks"])
plt.show()
