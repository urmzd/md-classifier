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

## Neural Networks Writeup

Neural Networks provide a promising method of determining the user’s ailment given a description of their symptoms. There are, however, several variations in which the model can be constructed. Kurup and Shetty developed a chatbot that would prompt the user to provide descriptions of their experienced symptoms. Based on this input, they utilized a sequential model with alternating dense and dropout layers followed by a softmax dense layer to classify the most likely illness. A highlighted issue, however, was in obtaining a dataset. Due to privacy concerns and a large variation in disease symptoms and severity, finding a large enough dataset to train the neural network could prove challenging. Kurup and Shetty [1] utilized a medical database which included descriptions of illnesses, however the efficacy of the model may be impacted through the use of informal terminology by users of what they are experiencing. Another model developed by Baker et al. [2] involved the use of a Convolutional Neural Network (CNN) trained with biomedical publication abstracts that would conduct multi-label classification to determine whether the text contained any of a selected ten hallmarks of cancer. In this paper, the CNN’s performance was compared to that of a Support Vector Machine (SVM), and found to be more accurate. The added benefit of using a CNN would be the effective pattern recognition capabilities they provide through their convolution and pooling layers, leading to their frequent use in image and text classification. This advantage means that we are most likely going to implement a CNN as our model. There are, however, extra considerations we will have to take into account with this form of Neural Network. When constructing our model, we will have to determine the filter size used in the convolution layers. When attempting to increase the accuracy of their model, Baker et al. maintained a constant total of filters at 300 while testing the performance of their model at varying filter sizes. We will have to undergo a similar process when developing our model in order to optimize its performance.

## Project Plan
Going forward, we have developed a schedule to keep us on track for the remainder of the semester. We aim to have gathered and cleaned a usable dataset by November 12. This process may require more manual involvement in gathering usable data due to a lack of a preexisting dataset containing informal medical descriptions classified by their illness. Next, our aim is to have a completed and functioning model by November 26. One week later on December 3, we expect to have completed our report and on the following day, December 4, we want to have completed our presentation. We do plan to have started work on our report before completion of our model, however, as there will be sections that aren’t dependent on information from its performance. This is to provide ourselves with enough time to create the report without a time crunch. In addition to continuous independent work, the two of us wish to call 2 times a week to bring each other up to date on our progress, as well as pair program should that be required.

## Building

- To enter the development environment, execute `source venv/bin/activate`.
- To exit the development environment, execute `deactivate`.
- To ensure dependencies are installed, execute `pip install -r requirements.txt`.
- To ensure dependencies are added to requirements, execute `pip freeze > requirement.txt`.

## Resources

- [Auto Completion](https://modeling-languages.com/nlp-architecture-model-autocompletion-domain/)
- [LSTM](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)
- [n-gram](https://en.wikipedia.org/wiki/N-gram#:~:text=In%20the%20fields%20of%20computational,a%20text%20or%20speech%20corpus.)
- [Context Analysis](http://www.lexalytics.com/lexablog/context-analysis-nlps)
- [Kurup G., Shetty S.D.](https://link.springer.com/chapter/10.1007/978-981-16-2543-5_22)
- [Baker et al.](https://aclanthology.org/W16-5101.pdf)
- [Limsopatham and Collier](https://aclanthology.org/P16-1096.pdf)
