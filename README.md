# MD NLP

An NLP model which predicts an ailment given a description of symptoms.

## Table of Contents

- [Proposal](#proposal)
- [Building](#building)

## Proposal

Given the user has provided a description of the symptoms they are experiencing, the model should
correctly classify the ailment that most closely matches the provided information. Data would be scraped
from credible websites describing a particular health issue (such as the WebMD page for headaches). To
implement this functionality, we may use a Naive Bayes classifier or a Recurrent Neural Network **(RNN)**.

An example of this would go as such:

> Input: My heading is hurting.

> Output: HEADACHE

## Building

- To enter the development environment, execute `source venv/bin/activate`.
- To exit the development environment, execute `deactivate`.
- To ensure dependencies are installed, execute `pip install -r requirements.txt`.
- To ensure dependencies are added to requirements, execute `pip freeze > requirement.txt`.

## Resources

- [Auto Completion](https://modeling-languages.com/nlp-architecture-model-autocompletion-domain/)
- [LSTM](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)
- [`n`-gram](https://en.wikipedia.org/wiki/N-gram#:~:text=In%20the%20fields%20of%20computational,a%20text%20or%20speech%20corpus.)
