# Lang-AI 🌐

Lang-AI is a professional Natural Language Processing (NLP) application designed to automatically detect the language of any given text and translate it into a user-specified target language in real-time. By leveraging Machine Learning for language identification and a translation API for conversion, Lang-AI provides a seamless cross-lingual communication experience.

---

## 🎯 Project Objectives
* **Accurate Detection:** Build a machine learning model capable of precisely identifying text across 22 different languages.
* **Interactive UI:** Implement a user-friendly Streamlit web interface for real-time detection and translation.
* **Methodology Demonstration:** Showcase the effectiveness of traditional NLP techniques like TF-IDF and Multinomial Naive Bayes for multilingual classification.

---

## 🛠️ Technologies Used

| Category | Technology / Library |
| :--- | :--- |
| **Core Language** | Python |
| **Web Interface** | Streamlit |
| **Machine Learning**| scikit-learn (Multinomial NB), joblib |
| **NLP & Preprocessing**| NLTK (SnowballStemmer), Regex (`re`) |
| **Data Handling** | Pandas, NumPy |
| **Translation API** | `translate` library |

---

## 📊 Dataset Description

* **File Name:** `language.csv`
* **Dataset Size:** 22,000 rows × 2 columns
* **Columns:**
  * `Text`: The input sentence or phrase.
  * `language`: The corresponding ground-truth language label.
* **Distribution:** Balanced dataset with exactly 1,000 instances for each of the 22 supported languages.

### 🌐 Supported Languages for Detection
Estonian, Swedish, Thai, Tamil, Dutch, Japanese, Turkish, Latin, Urdu, Indonesian, Portuguese, French, Chinese, Korean, Hindi, Spanish, Pushto, Persian, Romanian, Russian, English, Arabic.

---

## ⚙️ Data Preprocessing & Feature Engineering

To ensure clean data input for the machine learning model, the following pipeline was implemented:

1. **Text Cleaning:** Removed special characters, punctuation, and numerals using Regular Expressions (Regex).
2. **Lowercasing:** Converted all text to lowercase for uniformity.
3. **Tokenization & Stemming:** Extracted root words using NLTK's `SnowballStemmer` to handle multiple language families.
4. **TF-IDF Vectorization:** Converted text tokens into numerical features using `TfidfVectorizer` with the following configurations:
   * `ngram_range=(1, 2)` (Captures both unigrams and bigrams)
   * `max_features=10000`
   * `stop_words='english'`

---

## 🤖 Model Architecture

The application utilizes an end-to-end Machine Learning pipeline combining feature extraction and classification:
* **Classifier:** Multinomial Naive Bayes (chosen for its speed and high efficiency in text classification tasks).
* **Pipeline:** Bundled together using scikit-learn's `make_pipeline`.
* **Hyperparameter Tuning:** Applied Laplace smoothing with `alpha=0.01`.
* **Persistence:** The trained model pipeline is saved using `joblib` for optimized, cached loading in production.

---

## 🚀 Streamlit Web Application & Translation

* **Optimized Loading:** Utilizes Streamlit's caching mechanism to load the machine learning model instantly without latency.
* **User Experience:** Features an intuitive text area for input, instantly displaying the detected language.
* **Translation Module:** Powered by the `translate` Python package. An internal dictionary maps the detected language names to standard ISO codes, enabling seamless translation to supported target languages (including *Pushto, Persian, Romanian, Russian, English, and Arabic*).

---

## 📈 Results & Output

* **High Accuracy:** The model achieves a **95% accuracy rate** across diverse language groups during testing.
* **Low Latency:** Real-time predictions and translation feedback loop with minimal computing overhead.

---

## ⚠️ Challenges Faced

* **Multilingual Stemming:** Finding a balanced stemming approach that accurately works across fundamentally different language families.
* **Unicode Handling:** Resolving encoding and rendering challenges for non-Latin scripts such as Urdu, Arabic, and Chinese.
* **Feature Dependency:** Managing model reliability since performance is highly dependent on the quality of TF-IDF vocabulary.

---

## 🔮 Future Enhancements

- [ ] Upgrade the classifier to Deep Learning models (e.g., LSTMs or Transformer-based models like BERT).
- [ ] Integrate Audio Input functionality alongside multilingual Speech-to-Text conversion.
- [ ] Implement advanced translation backends like Google Translate API or HuggingFace Transformers.
- [ ] Containerize the application using Docker and deploy on cloud platforms.

---

## 📜 Conclusion

**Lang-AI** demonstrates that traditional NLP methods (TF-IDF + Naive Bayes), when paired with rigorous data preprocessing and a modern UI framework like Streamlit, can deliver a highly effective, production-ready solution for language detection and translation.