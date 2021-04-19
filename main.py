import numpy
import matplotlib.pyplot as pyplot
from sklearn.metrics import r2_score

# data for the model
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

# graph order for the linear regression
graphOrder = 3

# building the model and graph
myModel = numpy.poly1d(numpy.polyfit(x,y,graphOrder))
myLine = numpy.linspace(1,18,100)

# plotting
pyplot.scatter(x,y)
pyplot.plot(myLine, myModel(myLine))
pyplot.show()

# R2 Score for validation
print('R2 Score: ', r2_score(y, myModel(x)))

# Prediction
x_val_for_prediction = 20
predicted_y = myModel(x_val_for_prediction)
print('predicted_y: ', predicted_y)
