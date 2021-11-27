# MD NLP

An NLP model which predicts an ailment given a description of symptoms.

## Table of Contents

- [Proposal](#proposal)
- [Building](#building)
- [Testing](#testing)

## Proposal

Given the user has provided a description of the symptoms they are experiencing, the model should
correctly classify the ailment that most closely matches the provided information. Data would be scraped
from credible websites describing a particular health issue (such as the WebMD page for headaches). To
implement this functionality, we may use a Naive Bayes classifier or a Recurrent Neural Network **(RNN)**.

An example of this would go as such:

> Input: My heading is hurting.

> Output: HEADACHE

## Project Plan

## Building

### Set Up 
```bash
  python -m virtualenv venv
  source venv/bin/activate
  pip install --no-deps -r requirements.txt
  pip install ipykernel
  pip install jupyter-tabnine
  python -m ipykernel install --user --name=mdnlp
  jupyter contrib nbextension install --user
  jupyter nbextension install --py --user jupyter_tabnine
  jupyter nbextension enable --py --user jupyter_tabnine 
  jupyter serverextension enable --py jupyter_tabnine
```

### Tear Down
```bash
  pip freeze > requirements.txt 
  deactivate
  jupyter kernelspec uninstall mdnlp
```

## Testing

This project uses `pytest` for its unit-tests.
To find more information about the configuration used, check `./pytest.ini`.

In general, all tests must be prefixed with `given_` under the `tests` directory (found in the root dir)
and within a file which started with the `test_` prefix.

To run the tests, ensure you are in the virtual enviroment and execute `pytest`

## Resources

- [Auto Completion](https://modeling-languages.com/nlp-architecture-model-autocompletion-domain/)
- [LSTM](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)
- [n-gram](https://en.wikipedia.org/wiki/N-gram#:~:text=In%20the%20fields%20of%20computational,a%20text%20or%20speech%20corpus.)
- [Context Analysis](http://www.lexalytics.com/lexablog/context-analysis-nlps)
- [Kurup G., Shetty S.D.](https://link.springer.com/chapter/10.1007/978-981-16-2543-5_22)
- [Baker et al.](https://aclanthology.org/W16-5101.pdf)
- [Limsopatham and Collier](https://aclanthology.org/P16-1096.pdf)
- [Problem Statement](https://www.wect.com/2019/06/24/study-finds-us-citizens-turn-google-before-their-doctor/)
