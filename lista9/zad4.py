import matplotlib.pyplot as plt

rank = ["C","Java","Python","C++","C#","Visual Basic","JavaScript","PHP","R","Groovy"]
rating  = [17.38,11.96,11.72,7.56,3.95,3.84,2.2,1.99,1.9,1.84]

plt.figure(figsize=(10, 5))

plt.bar(rank, rating, color='blue')
plt.ylabel("Popularność w %")
plt.xlabel("Języki programowania")
plt.suptitle("Wykres popularności języków programowania")
plt.show()