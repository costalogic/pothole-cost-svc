import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from keras.models import load_model
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def train_model(material):
    ## function to run the model
    data = {'sqrfoot': [], 'depth': [], 'value': []}
    
    ## Train According to the material
    if material == 'ASPHALT':
        file = 'asphalt.csv'
    elif material == 'CONCRETE':
        file = 'concrete.csv'
    elif material == 'COLDPATCH':
        file = 'coldpatch.csv'
    
    print (os.path.join('data', file))
    df = pd.read_csv(os.path.join('model', 'data', file))
    print(df)
    # Encoding categorical variables
    df['depth'] = df['depth'].astype('category').cat.codes
    print(df)
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
    model.save(os.path.join('model', 'data', f'{material}.h5'))

    ## Plot
    plt.xlabel("# Repeticiones")
    plt.ylabel("# Magnitud de perdida")
    plt.plot(history.history["loss"])
    # Save the plot to an image file
    plt.savefig('plot'+material+'.png')
    
 ##['ASPHALT', 'CONCRETE', 'COLDPATCH'],
def run_model( area, depth, material):
    if material == 'ASPHALT':
        modelo = load_model('model\data\ASPHALT.h5')
    elif material == 'CONCRETE':
        modelo = load_model('model\data\CONCRETE.h5')
    elif material == 'COLDPATCH':        
        modelo = load_model('model\data\COLDPATCH.h5')   
    
    result = modelo.predict([[area, depth]])    
    price = result[0][0]
    return price
