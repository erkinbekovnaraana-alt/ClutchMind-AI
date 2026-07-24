import pandas as pd
import matplotlib.pyplot as plt

# Example dataset
data = {
    "stress_level": [1,2,3,4,5,6,7,8,9,10],
    "performance": [50,55,60,65,70,72,71,68,60,50]
}

df = pd.DataFrame(data)

# Plot
plt.plot(df["stress_level"], df["performance"], marker='o')
plt.xlabel("Stress Level")
plt.ylabel("Performance")
plt.title("Performance under Pressure")
plt.savefig("result.png")
plt.show()
