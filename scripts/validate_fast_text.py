#!/usr/bin/env python3
"""Validate FastText CNN — reads sentence data, trains FastText embeddings, builds CNN."""

import os
import sys
import random
import warnings

import numpy as np
import tensorflow as tf
from gensim.models.fasttext import FastText
from nltk import tokenize
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer
from sklearn import metrics

warnings.filterwarnings("ignore")
random.seed(42)
np.random.seed(42)
tf.random.set_seed(42)

# Config
WORD_LIMIT = 56
VECTOR_SIZE = 32
TEST_SIZE = 0.3
EPOCHS = 5

RESOURCE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "resources")
TARGET_DIR = os.path.join(RESOURCE_DIR, "data", "targets", "fast-text")


def load_sentence_data(target_dir):
    """Load sentences from target files."""
    data = {}
    for filename in sorted(os.listdir(target_dir)):
        if not filename.endswith(".txt"):
            continue
        label = os.path.splitext(filename)[0]
        with open(os.path.join(target_dir, filename)) as f:
            sentences = [s.strip() for s in f.readlines() if s.strip()]
        data[label] = sentences
    return data


def train_fasttext(data):
    """Train FastText model on all sentences."""
    # Write corpus to temp file
    corpus_path = os.path.join(RESOURCE_DIR, "data", "_validation_corpus.txt")
    with open(corpus_path, "w") as f:
        for sentences in data.values():
            for sentence in sentences:
                f.write(sentence + "\n")

    model = FastText(vector_size=VECTOR_SIZE)
    model.build_vocab(corpus_file=corpus_path)
    model.train(
        corpus_file=corpus_path,
        epochs=model.epochs,
        total_examples=model.corpus_count,
        total_words=model.corpus_total_words,
    )

    os.remove(corpus_path)
    return model


def pad_sequence(sequence, limit=WORD_LIMIT):
    seq = np.copy(sequence)
    if seq.shape[0] == limit:
        return seq
    if seq.shape[0] < limit:
        mins = np.minimum.reduce(seq)
        maxs = np.maximum.reduce(seq)
        paddings = []
        for i in range(limit - seq.shape[0]):
            paddings.append(mins if i % 2 == 0 else maxs)
        return np.vstack((seq, paddings))
    return seq[:limit]


def encode_sentence(sentence, ft_model, word_limit=WORD_LIMIT):
    tokens = tokenize.wordpunct_tokenize(sentence)
    vectors = np.vstack([ft_model.wv[token] for token in tokens])
    padded = pad_sequence(vectors, word_limit)
    return padded.reshape((*padded.shape, 1))


def get_x_y(data, ft_model):
    label_encoder = LabelBinarizer()
    label_encoder.fit(sorted(data.keys()))

    xs, ys = [], []
    for label, sentences in sorted(data.items()):
        for sentence in sentences:
            x = encode_sentence(sentence, ft_model)
            y = label_encoder.transform([label])
            xs.append(x)
            ys.append(y)

    return np.array(xs), np.vstack(ys), label_encoder


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

    model = keras.Model(inputs=inp, outputs=out, name="fast_text_cnn")
    model.compile(
        optimizer=keras.optimizers.Adam(0.001),
        loss=keras.losses.binary_crossentropy,
        metrics=["accuracy", keras.metrics.Recall()],
    )
    return model


def main():
    print("Loading sentence data...")
    data = load_sentence_data(TARGET_DIR)
    for label, sentences in sorted(data.items()):
        print(f"  {label}: {len(sentences)} sentences")

    print("\nTraining FastText model...")
    ft_model = train_fasttext(data)

    print("Encoding sentences...")
    x, y, label_encoder = get_x_y(data, ft_model)
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
    y_pred_labels = label_encoder.inverse_transform(y_pred)
    y_true_labels = label_encoder.inverse_transform(y_test)

    labels = sorted(data.keys())
    cm = metrics.confusion_matrix(y_true_labels, y_pred_labels, labels=labels)
    print(f"\nConfusion Matrix:\n{cm}")
    print(f"Labels: {labels}")


if __name__ == "__main__":
    main()
