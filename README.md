# What Symptom?

A model which predicts an ailment given a description of symptoms.

## Table of Contents

### 1. [Proposal](#proposal)

## Proposal

Given the user has provided a description of the symptoms they are experiencing, the model should
correctly classify the ailment that most closely matches the provided information. Data would be scraped
from credible websites describing a particular health issue (such as the WebMD page for headaches). To
implement this functionality, we may use a Naive Bayes model or a Recurrent Neural Network **(RNN)**.

An example of this would go as such:

> Input: My heading is hurting.
> Output: HEADACHE
