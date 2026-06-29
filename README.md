**Project Overview**

Lang-AI is a natural language processing application designed to automatically detect the language of a given text input and translate it into a user-specified target language. It utilizes machine learning for language identification and a translation API for real-time text translation.



**Project Objectives**

•	To build a model that can accurately detect the language of an input sentence.
•	To implement an interactive Streamlit web app that enables users to detect and translate text.
•	To demonstrate the effectiveness of TF-IDF and Naive Bayes for multilingual text classification.




**Technologies Used**

•	Programming Language: Python
•	Web Interface: Streamlit
•	Libraries:
o	scikit-learn (for modeling)
o	nltk (for preprocessing)
o	joblib (for model persistence)
o	translate (for translation)
o	pandas, numpy, re (for data handling)
•	Model Deployment: Streamlit interface with cached model loading



**Dataset Description**

•	Dataset Name: language.csv
•	Columns:
o	2 columns and 22,000 rows
o	Text and Language
o	Text: the sentence or phrase
o	language: the corresponding language label
•	Languages Detected:  22 Languages
o	Estonian
o	Swedish
o	Thai
o	Tamil
o	Dutch
o	Japanese
o	Turkish
o	Latin
o	Urdu
o	Indonesian
o	Portugese
o	French
o	Chinese
o	Korean
o	Hindi
o	Spanish
o	Pushto
o	Persian
o	Romanian
o	Russian
o	English
o	Arabic

Each Language consists of 100 instances.


**Data Preprocessing**

Preprocessing steps included:
•	Text cleaning: 
Removal of special characters and numerals using regex.
•	Lowercasing
•	Tokenization
•	Stemming: 
Using SnowballStemmer from NLTK for root word extraction.


**Feature Engineering**

•	Used TF-IDF Vectorizer with:
o	ngram_range=(1, 2) for unigram and bigram features
o	max_features=10000
o	stop_words='english'

•	These features were used as inputs to the classifier.


**Model Architecture**

•	Classifier: Multinomial Naive Bayes
•	Pipeline: Combined TfidfVectorizer and MultinomialNB using make_pipeline
•	Hyperparameter:
o	alpha=0.01 for smoothing
•	The model was trained on preprocessed text data and saved using joblib.


 


**Streamlit Web Application**

•	Model Loading
•	User Input: Text area for entering the sentence to detect
•	Output:
o	Displays detected language
o	Allows selecting a target language from a dropdown
o	Provides translation using translate.Translator

 


**Translation Functionality**

•	Used translate Python module
•	Mapping from detected language name to ISO codes handled using a dictionary
•	Translates from detected language to user-specified target language
Supported languages include: Pushto, Persian, Romanian, Russian, English, Arabic.



**Results and Output**

•	The system successfully:
o	Detects languages with accuracy of 95%
o	Translates between diverse language pairs
•	Integrated real-time UI with minimal latency


**Challenges Faced**

•	Ensuring accurate stemming for multiple language families
•	Handling Unicode characters for languages like Chinese, Urdu, and Arabic
•	Model performance depends on the quality of TF-IDF features and preprocessing


**Future Enhancements**

•	Add a deep learning-based classifier (e.g., LSTM or BERT)
•	Support audio input and multilingual speech-to-text.
•	Integrate Google Translate or HuggingFace Transformers for more robust translation.
•	Expand to mobile app using Streamlit sharing or Docker


**Conclusion**

Lang-AI is a robust and interactive web application for multilingual language detection and translation. It demonstrates the power of traditional NLP methods (TF-IDF + Naive Bayes) when combined with a clean UI for practical use. With a few enhancements, it can become a highly useful tool for cross-lingual communication.

