import keras as k
import pandas as pd
import numpy as np

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
    raw_input = data_frame[input_names] #получаем данные с файла
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

def create_model(data):
    supervised = make_supervised(data_frame)
    encoded_inputs = np.array(encode(supervised["inputs"]))
    encoded_outputs = np.array(encode(supervised["outputs"]))

    train_x = encoded_inputs[:600]
    train_y = encoded_outputs[:600]

    text_x = encoded_inputs[600:]
    text_y = encoded_outputs[600:]

    model = k.models.load_model('ii_model/model')
    model.evaluate(text_x,text_y)

    predited_test = model.predict(np.array(encode(data)))
    return predited_test[0][0]


def send_model(data):
    for value in data.keys():
        if value == 'Sex':
            data[value] = data[value].split(' ')
        else:
            data[value] = [int(data[value])]
    answ = create_model(data)
    return {'data':round(answ*100)}

# print(send_model({'Age':[99/100],'Pclass':[3],'Sex':['male']}))

#0.2440869
#0.2540417