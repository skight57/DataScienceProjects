#need to install pandas first. Try 'pip install pandas' in the terminal if using pycharm
import pandas as pd
import matplotlib.pyplot as plt

BCD = pd.read_csv('BreastCancerData.csv')

test_column = pd.DataFrame(columns=['SampleCodeID'])

print(test_column)

y = BCD.Madhesion
x = BCD.Class

# plotting the points
plt.plot(x, y)


# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('My first graph!')

