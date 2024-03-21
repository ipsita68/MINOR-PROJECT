
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

**Example test-statements that you can use to copy/paste and test the working of the Spam Detector:**

   - Here are some examples of non-spam (ham) emails:
        - "Hi John, just wanted to follow up on our meeting from yesterday. Could you please review the attached document and let me know your thoughts? Thanks."
        - "Dear Customer, thank you for your recent purchase. Your order (#123456) has been processed and will be shipped out within the next 24 hours. You can track your order using the link provided below."
        - "Hey Sarah, how was your weekend? I hope you had a great time at the party on Saturday. Let's catch up soon over coffee."
        - "Reminder: Your appointment with Dr. Smith is scheduled for tomorrow at 10:00 AM. Please remember to bring any necessary documents or test results with you."
        - "Hello team, just a quick heads up that our weekly meeting has been rescheduled to Thursday at 3:00 PM. Please update your calendars accordingly."

**These emails contain typical content found in legitimate correspondence, such as meeting reminders, order confirmations, personal messages, and updates on appointments or events.**

   - Here are some examples of spam emails:
        - "Congratulations! You've been selected as a winner of our monthly prize draw. Click here to claim your prize of $1000 cash!"
        - "Special offer: Get 50% off on all purchases at our online store. Limited time only! Click here to shop now."
        - "URGENT: Your account has been compromised. Click here to verify your identity and secure your account."
        - "Make money fast with our proven investment strategy. Start earning thousands of dollars per week from the comfort of your own home."
        - "You've won a free vacation to a tropical paradise! Claim your trip now by clicking the link below."

**These emails often contain offers that seem too good to be true, urgent requests for action, or prompts to click on links that may lead to phishing websites or malware downloads.**
You are free to use any other data you want to test!
---
# *Note: The classification results provided by the application might not be 100% accurate as it depends on the quality and diversity of the dataset used for training the classifier.*
---
**Contributors: [IPSITA/ipsita68]**
