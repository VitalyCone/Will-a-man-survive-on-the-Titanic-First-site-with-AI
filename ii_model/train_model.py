import keras as k
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_frame = pd.read_csv("ii_model/titanic.csv") 
input_names = ["Age","Sex","Pclass"]
output_names = ["Survived"]

max_age = 100 
encoders ={
    "Age": lambda age: [age/max_age],
    "Sex": lambda gen: {
        "male":[0],
        "female":[1]}.get(gen),
    "Pclass": lambda pclass: {
        1:[1,0,0],
        2:[0,1,0],
        3:[0,0,1]}.get(pclass),
    "Survived": lambda s_value:[s_value]
    }
def dataframe_to_dict(df):
    resoult = dict()
    for column in df.columns:
        values = data_frame[column].values
        resoult[column] = values
    return resoult

def make_supervised(df):
    raw_input = data_frame[input_names]
    raw_output = data_frame[output_names]
    return {'inputs': dataframe_to_dict(raw_input),
            'outputs': dataframe_to_dict(raw_output)}

def encode(data):
    vectors = []
    for data_name, data_values in data.items():
        encoded = list(map(encoders[data_name], data_values))
        vectors.append(encoded)
    formatted = []
    for vector_raw in list(zip(*vectors)):
        vector = []
        for element in vector_raw:
            for e in element:
                vector.append(e)
        formatted.append(vector)
    return formatted


supervised = make_supervised(data_frame)
print(data_frame,"                     ",make_supervised(data_frame))
encoded_inputs = np.array(encode(supervised["inputs"]))
encoded_outputs = np.array(encode(supervised["outputs"]))

#закончили сбор данных

train_x = encoded_inputs[:600]
train_y = encoded_outputs[:600]

text_x = encoded_inputs[600:]
text_y = encoded_outputs[600:]

model = k.Sequential()
model.add(k.layers.Dense(units=5,activation="relu")) 
model.add(k.layers.Dense(units=1, activation="sigmoid")) 

model.compile(loss="mse",optimizer="sgd",metrics=["accuracy"]) 
fit_results = model.fit(x=train_x,y=train_y,epochs=1000,validation_split=0.2)


plt.title("loses train validation")
plt.plot(fit_results.history["loss"],label="Train")
plt.plot(fit_results.history["val_loss"],label="Validation")
plt.legend()
plt.show()

plt.title("accuracies train validation")
plt.plot(fit_results.history["accuracy"],label="Train")
plt.plot(fit_results.history["val_accuracy"],label="Validation")
plt.legend()
plt.show()

predited_test = model.predict(text_x)
real_data = data_frame.iloc[600:][input_names+output_names] #iloc если взять определенный срез по явному индексу
real_data["PSurvived"] = predited_test
print(real_data)