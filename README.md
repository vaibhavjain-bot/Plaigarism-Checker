# Semantic Similarity Checker

The Semantic Similarity Checker is a machine learning-based system that compares a user-provided text with a pre-existing database of texts and provides a similarity score. The system is designed to detect potential cases of plagiarism by identifying texts that are semantically similar to the user-provided text. The system uses the OpenAI API to compute the semantic similarity between the user-provided text and the pre-existing texts in the database.

## Installation

To install the Semantic Similarity Checker, clone this repository and follow the instructions provided in the README file. The system requires Python 3.6 or later and the installation of various libraries such as Gradio, pandas, numpy, and OpenAI. 

1. Clone the repository

```
git clone https://github.com/username/semantic-similarity-checker.git
```

2. Install the necessary libraries using pip

```
pip install gradio pandas numpy openai
```

3. Run the Gradio interface

```
python app.py
```

4. Open the Gradio interface in a web browser

```
http://localhost:7878/
```

## Usage

To use the Semantic Similarity Checker, simply input the text you want to check in the Gradio interface and click on the "Check" button. The system will compare your text with the pre-existing texts in the database and provide the most similar text and its similarity score. Users can also update or replace the pre-existing texts in the database as necessary.

## Contributing

Contributions to the Semantic Similarity Checker are welcome! To contribute, please create a pull request with your proposed changes. 

## License

The Semantic Similarity Checker is licensed under the MIT license. Please see the LICENSE file for more information.
