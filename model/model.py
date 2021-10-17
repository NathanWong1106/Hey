import tensorflow as tf
import numpy as np
import pandas as pd
from tensorflow import keras
from tensorflow.keras import layers
from typing import Tuple, List
import csv


def compile_training_data() -> Tuple[List[list], list]:
    """ 
    Returns a tuple of features and labels to be used for training
    """

    features = []
    labels = []

    with open("./model/data/data.csv") as file:
        reader = csv.reader(file, delimiter=",")

        for row in reader:

            to_append = []
            for num in row[0:len(row) - 1]:
                to_append.append(float(num))

            features.append(to_append)
            labels.append(0 if row[len(row) - 1] == "raised" else 1)

    return (features, labels)


# Theoretically this is a binary classification problem...
def train_on_data():
    features, labels = compile_training_data()
    features = np.array(features)
    labels = np.array(labels)

    model = keras.Sequential(
        [
            layers.Dense(34, activation='relu'),
            layers.Dropout(0.25),
            layers.Dense(17, activation = 'relu'),
            layers.Dense(1, activation='sigmoid')
        ]
    )

    model.compile(optimizer='adam', loss="binary_crossentropy", metrics=['accuracy'])
    model.fit(features, labels, epochs=10, batch_size=32)
    model.save("./model/trained_model")

if __name__ == "__main__":
    # df = pd.read_csv("./model/data/data.csv")
    # print(np.array(df))
    train_on_data()