# MD NLP

> A collection of Convolutional Neural Networks (CNNs) that attempt to classify the
> ailment an individual is attempting to describe using the symptoms provided.

## Table of Contents

- [Proposal](#proposal)
- [Contributing](#contributing)
  - [Prerequisities](#prerequisities)
  - [Building](#building)
  - [Testing](#testing)

## Proposal

> TLDR; The [proposal](./p1.pdf) describes the problem and two possible approaches. One involves the use of CNN,
> and the other describes a solution which uses an N-Gram model. In the end, we decided to only pursue the
> CNN due to time-constraints.

An example scenario would go as follows:

> Input: My heading is hurting.
>
> Output: You likely have a **Migraine**.

### Research Project Paper

> In this paper, we address the challenges experienced in the preliminary research phase
> of ailment diagnosis performed by many individuals prior to visiting a
> healthcare professional. Due to the large quantity of varying results appearing
> once someone searches their current symptoms, we developed a convolutional
> neural network (CNN) that reduces this clutter by returning only the most
> probable medical condition given the user's description.
> To address the problem, we introduce two CNN implementations with different
> preprocessors. The first implementation explores the use of a One Hot Encoder,
> while the second implementation utilizes a FastText model trained via
> unsupervised learning. Through the retrieval of open source data from various medical platforms such
> as UpToDate and Mayo Clinic, a recall value of 90\% is achieved.

The full research paper can be found under [`report.pdf`](./report.pdf)

## Contributioning

### Prerequisities

- Optional - Google Collab
- Mandatory - Python3.7+
- Mandatory - Pip3

### Building

#### Set Up

```bash
  # Create the virtual enviroment.
  python -m virtualenv venv
  # Enter the environment.
  source venv/bin/activate
  # Install the dependencies.
  pip install --no-deps -r requirements.txt
  # Install a jupyter kernel to allow different for different Python environments.
  pip install ipykernel
  # Add current environment to jupyter.
  python -m ipykernel install --user --name=mdnlp
```

#### Tear Down

```bash
  # Track dependencies.
  pip freeze > requirements.txt
  # Retain dependencies in `git`
  git add requirements.txt
  git commit -m "[verb] - description of action"
  git push
  deactivate
  # Only use this command when you're certain
  # that you no longer want to reference the environment.
  jupyter kernelspec uninstall mdnlp
```

### Testing

> This project original included `pytest` unit tests, however, this is no longer the case. As the project was interactive in nature, we opted to use 'Google Collab'. However, this is not to say the code is untestable, most of it was written of using the functional programming paradigm, and can be easily refactored into a script.

This project uses `pytest` for its unit-tests.
To find more information about the configuration used, check `./pytest.ini`.

In general, all tests must be prefixed with `given_` under the `tests` directory (found in the root dir)
and within a file which started with the `test_` prefix.

To run the tests, ensure you are in the virtual enviroment and execute `pytest`
