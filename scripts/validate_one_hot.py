#!/usr/bin/env python3
"""Validate one-hot encoding CNN — reads processed word data, generates synthetic samples, trains CNN."""

import os
import sys
import random
import warnings

import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, LabelBinarizer
from sklearn import metrics
from nltk.probability import WittenBellProbDist, FreqDist

warnings.filterwarnings("ignore")
random.seed(42)
np.random.seed(42)
tf.random.set_seed(42)

# Config
WORD_LIMIT = 56
N_SAMPLES = 750
TEST_SIZE = 0.2
EPOCHS = 5

RESOURCE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "resources")
TARGET_DIR = os.path.join(RESOURCE_DIR, "data", "targets", "one-hot-encoding")


def load_word_data(target_dir):
    """Load word lists from target files."""
    data = {}
    for filename in sorted(os.listdir(target_dir)):
        if not filename.endswith(".txt"):
            continue
        label = os.path.splitext(filename)[0]
        with open(os.path.join(target_dir, filename)) as f:
            words = [w.strip() for w in f.readlines() if w.strip()]
        data[label] = words
    return data


def unpack_dict_list(d):
    return [v for vals in d.values() for v in vals]


def generate_sample(population, label, n_unique_words, word_limit=WORD_LIMIT):
    freq_dist = FreqDist(population)
    prob_dist = WittenBellProbDist(freq_dist, n_unique_words)
    samples = [prob_dist.generate() for _ in range(word_limit)]
    return np.array([*samples, label]).reshape(-1, 1)


def generate_samples(data, n_samples=N_SAMPLES):
    n_unique_words = len(set(unpack_dict_list(data)))
    return np.array([
        np.array([generate_sample(data[k], k, n_unique_words) for _ in range(n_samples)])
        for k in sorted(data.keys())
    ])


def get_encoders_and_data(data):
    samples = generate_samples(data)

    # Split into x (words) and y (labels)
    x = samples[:, :, :-1]
    y = samples[:, :, -1]
    y = y.reshape(y.shape[0] * y.shape[1], 1)

    # One-hot encoder for input words
    all_words = np.array(list(set(unpack_dict_list(data)))).reshape(-1, 1)
    input_encoder = OneHotEncoder(handle_unknown="ignore")
    input_encoder.fit(all_words)

    # Label encoder for output
    output_encoder = LabelBinarizer()
    output_encoder.fit(y)

    # Encode
    encoded_x = np.stack([
        input_encoder.transform(x[lbl_idx, smpl_idx]).toarray()
        for lbl_idx in range(x.shape[0])
        for smpl_idx in range(x.shape[1])
    ], axis=0)
    encoded_y = output_encoder.transform(y)

    # Add channel dim
    encoded_x = encoded_x.reshape((*encoded_x.shape, 1))

    return encoded_x, encoded_y, output_encoder


def build_cnn(input_shape, n_classes):
    from tensorflow import keras
    from tensorflow.keras import layers, regularizers

    inp = keras.Input(shape=input_shape)
    x = layers.Conv2D(3, (3, 3), strides=1, activation="relu")(inp)
    x = layers.MaxPool2D((2, 2), padding="same")(x)
    x = layers.Conv2D(3, (3, 3), strides=2, activation="relu")(x)
    x = layers.MaxPool2D((2, 2), padding="same")(x)
    x = layers.Dense(64, activation="relu", bias_regularizer=regularizers.l1_l2(0, 1.7))(x)
    x = layers.Dropout(0.5)(x)
    x = layers.Dense(64, activation="relu", bias_regularizer=regularizers.l1_l2(0, 1.8))(x)
    x = layers.Dropout(0.5)(x)
    x = layers.Dense(64, activation="relu",
                     kernel_regularizer=regularizers.l1_l2(0, 1.2),
                     bias_regularizer=regularizers.l1_l2(0, 1e-11))(x)
    x = layers.Dropout(0.5)(x)
    x = layers.Dense(128, activation="relu",
                     kernel_regularizer=regularizers.l1_l2(0, 4e-7),
                     bias_regularizer=regularizers.l1_l2(0, 0.9))(x)
    x = layers.Dropout(0.5)(x)
    x = layers.Flatten()(x)
    out = layers.Dense(n_classes, activation="softmax")(x)

    model = keras.Model(inputs=inp, outputs=out, name="one_hot_cnn")
    model.compile(
        optimizer=keras.optimizers.Adam(0.001),
        loss=keras.losses.binary_crossentropy,
        metrics=["accuracy", keras.metrics.Recall()],
    )
    return model


def main():
    print("Loading word data...")
    data = load_word_data(TARGET_DIR)
    for label, words in sorted(data.items()):
        print(f"  {label}: {len(words)} words")

    print(f"\nGenerating {N_SAMPLES} synthetic samples per class...")
    x, y, output_encoder = get_encoders_and_data(data)
    print(f"  x shape: {x.shape}, y shape: {y.shape}")

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=TEST_SIZE, random_state=42
    )

    model = build_cnn(x_train.shape[1:], y_train.shape[-1])
    model.summary()

    print(f"\nTraining for {EPOCHS} epochs...")
    model.fit(
        x_train, y_train,
        batch_size=2,
        epochs=EPOCHS,
        validation_split=TEST_SIZE,
    )

    print("\nEvaluating on test set...")
    test_scores = model.evaluate(x_test, y_test, verbose=2)
    print(f"Test accuracy: {test_scores[1]:.2%}")

    # Confusion matrix
    y_pred = model.predict(x_test)
    y_pred_labels = output_encoder.inverse_transform(y_pred)
    y_true_labels = output_encoder.inverse_transform(y_test)

    labels = sorted(data.keys())
    cm = metrics.confusion_matrix(y_true_labels, y_pred_labels, labels=labels)
    print(f"\nConfusion Matrix:\n{cm}")
    print(f"Labels: {labels}")


if __name__ == "__main__":
    main()
