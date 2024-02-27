import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Creating a DataFrame from the provided table
data = {
    'sqrfoot': [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3],
    'depth': ['0-2', '2.1-4', '4.1-6', '6.1-8', '8.1-10', '10.1-12'] * 3,
    'value': [1660.88, 1697.56, 1737.24, 1780.56, 1828.48, 1882.2] * 3
}

df = pd.DataFrame(data)

# Encoding categorical variables
df['depth'] = df['depth'].astype('category').cat.codes

# Splitting data into features (X) and target (y)
X = df[['sqrfoot', 'depth']]
y = df['value']

# Define the model
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=[2]),
    layers.Dense(64, activation='relu'),
    layers.Dense(1)
])

# Compile the model
model.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mse',  # mean squared error
    metrics=['mae']  # mean absolute error
)

print ("Comenzando Entrenamiento...")

# Train the model
history = model.fit(X, y, epochs=5000, batch_size=1, verbose=1)
print ("Modelo Entrenado!")

plt.xlabel("# Repeticiones")
plt.ylabel("# Magnitud de perdida")
plt.plot(history.history["loss"])

print ("Prediccion")
# Reshape the input and use a value within the range of the 'sqrfoot' feature
resultado = model.predict(np.array([[3, 2]]))
print("El Resultado del valor es "+str(resultado))