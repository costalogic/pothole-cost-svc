# Import the necessary modules
import cost_estimation as model

## Entrenar el modelo
materials = ['ASPHALT', 'CONCRETE', 'COLDPATCH']
for material in materials:
    model.train_model(material)
