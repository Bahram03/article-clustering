
# Article Clustering

This repository provides tools to gather, preprocess, and cluster articles based on their content. The main focus is to retrieve article data from web sources, clean and embed the text, and apply clustering techniques to group similar articles. This project can be useful for research, content management, or recommendation systems.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
  - [1. Collecting Article Links](#1-collecting-article-links)
  - [2. Retrieving Article Data](#2-retrieving-article-data)
  - [3. Preprocessing Titles](#3-preprocessing-titles)
  - [4. Generating Embeddings](#4-generating-embeddings)
  - [5. Clustering Articles](#5-clustering-articles)
- [Files](#files)
- [Dependencies](#dependencies)
- [License](#license)

## Overview

The project workflow includes:
1. **Web Scraping**: Extract links to articles, download content, and parse it.
2. **Data Preprocessing**: Normalize, tokenize, and clean article titles.
3. **Embedding**: Convert titles into embeddings for clustering.
4. **Clustering**: Apply clustering algorithms on the embeddings to group articles.

## Installation

To run this project, clone the repository and install the dependencies:

```bash
git clone https://github.com/Bahram03/article-clustering.git
cd article-clustering
pip install -r requirements.txt
```

## Usage

Follow these steps to perform article clustering.

### 1. Collecting Article Links

The script `find_articles_links.py` is used to collect links to articles from a specified website. Run this file to extract links to various volumes and issues.

```bash
python find_articles_links.py
```

### 2. Retrieving Article Data

After obtaining article links, use `get_articles.py` to download and parse each article, including title, authors, abstract, and keywords. This data is saved in a CSV file (`articles.csv`).

```bash
python get_articles.py
```

### 3. Preprocessing Titles

Clean and tokenize the article titles using `title_cleaner.py`. This script normalizes titles, tokenizes them, and removes unnecessary words based on their parts of speech. The cleaned titles are saved for later embedding.

```bash
python title_cleaner.py
```

### 4. Generating Embeddings

Run `embedding.py` to generate embeddings from the cleaned titles using Word2Vec. The embeddings will be used for clustering similar articles.

```bash
python embedding.py
```

### 5. Clustering Articles

Use the `clustering.ipynb` notebook to load the embeddings, apply clustering algorithms, and visualize the clustered groups of articles. Open the notebook in Jupyter to explore clustering interactively.

```bash
jupyter notebook clustering.ipynb
```

## Files

- **`find_articles_links.py`**: Scrapes article links from specified volumes and issues on the website.
- **`get_articles.py`**: Downloads article details (title, abstract, authors, keywords) and stores them in `articles.csv`.
- **`title_cleaner.py`**: Normalizes and tokenizes article titles, filtering out unnecessary parts of speech.
- **`embedding.py`**: Generates embeddings for titles using Word2Vec, storing these embeddings for clustering.
- **`clustering.ipynb`**: A Jupyter notebook for performing and visualizing clustering on the article embeddings.

## Dependencies

- Python 3.x
- `gensim`
- `pandas`
- `numpy`
- `beautifulsoup4`
- `requests`
- `hazm` (for Persian text processing)
- `scikit-learn` (for clustering)

Install dependencies with:

```bash
pip install gensim pandas numpy beautifulsoup4 requests hazm scikit-learn
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
