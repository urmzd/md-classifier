> **Archived.** This was a group project / final assessment for [CSCI 4152/6509 — Natural Language Processing](https://web.cs.dal.ca/~vlado/csci6509/) at Dalhousie University, part of the [Artificial Intelligence & Intelligent Systems certificate](https://www.dal.ca/faculty/computerscience/undergraduate-programs/program-planning/certificates.html) (undergraduate/graduate mixed course). It is no longer actively maintained.

# MD Classifier

A convolutional neural network (CNN) that predicts medical conditions from natural language symptom descriptions. Given a text input like *"My head is hurting"*, the model returns the most probable diagnosis (e.g., **Migraine**).

Built as a research project at Dalhousie University, achieving **90% recall** across three conditions: **Migraine**, **Depression**, and **Tetanus**.

## How It Works

Two CNN implementations are compared, each with a different text preprocessing strategy:

| Approach | Preprocessing | Accuracy | Recall |
|----------|--------------|----------|--------|
| **One-Hot Encoding** | Tokenize, stem, generate synthetic samples via Witten-Bell distribution, encode as binary vectors | 93% | 90% |
| **FastText Embeddings** | Tokenize sentences, train unsupervised word embeddings, pad via max/min pooling | 73% | 70% |

Training data is scraped from medical encyclopedias (Mayo Clinic, UpToDate, Healthline, NHS, etc.) and processed through custom pipelines in the Jupyter notebooks.

## Documents

- [**Research Paper**](./report.pdf) -- Full methodology, results, and analysis
- [**Proposal**](./p1.pdf) -- Problem statement and initial approach (CNN vs N-Gram)
- [**Presentation**](./presentation/presentation.pdf) -- Slide deck

## Project Structure

```
src/
  one-hot-encoding.ipynb   # One-Hot + CNN implementation
  fast-text.ipynb          # FastText + CNN implementation
resources/data/
  sources/                 # CSV files with scraping targets (URLs + DOM selectors)
  targets/                 # Processed training text per condition
docs/                      # LaTeX source for paper and proposal
scripts/
  compile-latex.sh         # Build PDFs from LaTeX
```

## Getting Started

**Requirements:** Python 3.7+, pip

```bash
# Create and activate a virtual environment
python -m virtualenv venv
source venv/bin/activate

# Install dependencies
pip install --no-deps -r requirements.txt

# Set up Jupyter kernel
pip install ipykernel
python -m ipykernel install --user --name=mdnlp
```

Then open either notebook in `src/` (locally or via Google Colab) and run the cells sequentially. Each notebook handles data collection, preprocessing, model training, and evaluation end-to-end.

## License

[Apache 2.0](./LICENSE)
