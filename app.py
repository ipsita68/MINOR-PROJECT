from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
from sklearn.calibration import CalibratedClassifierCV

# Load the existing CSV file into a DataFrame
df_existing = pd.read_csv('spam.csv', header=None, names=['label', 'text'])

# Load the additional CSV file into a DataFrame
df_additional = pd.read_csv('spam_ham_dataset.csv')

# Combine the two DataFrames
df_combined = pd.concat([df_existing, df_additional])

# Convert labels to numerical values
label_encoder = LabelEncoder()
df_combined['label'] = label_encoder.fit_transform(df_combined['label'])

# Balance the data using RandomOverSampler and RandomUnderSampler
ros = RandomOverSampler(random_state=42)
rus = RandomUnderSampler(random_state=42)
X_resampled, y_resampled = rus.fit_resample(*ros.fit_resample(
    df_combined['text'].values.reshape(-1, 1), df_combined['label']))

# Vectorizing the emails using TF-IDF Vectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X_resampled.ravel())
y = y_resampled

# Training the Naive Bayes classifier
clf = MultinomialNB()
clf.fit(X, y)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/classify', methods=['POST'])
def classify():
    try:
        message = request.form['message']
        vectorized_message = vectorizer.transform([message])

        prediction = clf.predict(vectorized_message)[0]
        prediction_label = label_encoder.inverse_transform([prediction])[0]

        return render_template('result.html', message=message, prediction=prediction_label)

    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render_template('error.html', error_message=error_message)


if __name__ == '__main__':
    app.run(debug=True)
