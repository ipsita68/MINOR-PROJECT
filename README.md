
---

# Spam Detector

**Description:**
This repository contains a Flask web application for classifying emails as spam or ham (non-spam) using a Naive Bayes classifier trained on a combined dataset from existing CSV files and additional CSV files. The application utilizes techniques such as TF-IDF vectorization, label encoding, data balancing using RandomOverSampler and RandomUnderSampler, and Multinomial Naive Bayes classification.

**File Structure:**
- `app.py`: Python script containing the Flask application code.
- `index.html`: HTML template for the main page of the web application.
- `result.html`: HTML template for displaying classification results.
- `error.html`: HTML template for displaying error messages.
- `spam.csv`: CSV file containing existing spam email data.
- `spam_ham_dataset.csv`: Additional CSV file containing spam and ham email data.
- `README.md`: README file containing instructions and information about the repository.

**Setup:**
1. Clone this repository to your local machine.
2. Ensure you have Python installed.
3. Install the required Python libraries by running:
   ```
   pip install flask pandas scikit-learn imbalanced-learn
   ```
4. Run the Flask application by executing `app.py`.
5. Open a web browser and navigate to `http://localhost:5000` to access the web application.

**Usage:**
1. Upon accessing the web application, you will see a text area where you can input an email message.
2. Enter an email message and click the "Classify" button.
3. The application will classify the input message as either spam or ham and display the result.

**Notes:**
- Ensure that the CSV files `spam.csv` and `spam_ham_dataset.csv` are present in the repository directory.
- The application utilizes techniques to handle class imbalance in the dataset.
- Any errors encountered during classification or execution of the application will be displayed on the error page.

**Contributors: [IPSITA/ipsita68]**
