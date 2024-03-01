import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from keras.models import load_model
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def train_model():
    ## function to run the model
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
        optimizer=keras.optimizers.Adam(0.001),
        loss='mse',  # mean squared error
        metrics=['mae']  # mean absolute errormae sui
    )
    print ("Comenzando Entrenamiento...")
    # Train the model


    history = model.fit(X, y, epochs=15000, batch_size=1, verbose=1)
    model.save('model/model.h5')

    ## Plot
    plt.xlabel("# Repeticiones")
    plt.ylabel("# Magnitud de perdida")
    plt.plot(history.history["loss"])


def run_model( area, depth):
    modelo = load_model('model/model.h5')
    result = modelo.predict([[area, depth]])    
    price = result[0][0]
    return price
