import csv
import random

# Function to generate a random message


def generate_message():
    words = ["Hey", "Hello", "Congratulations", "URGENT", "Free", "Click", "Claim",
             "Meeting", "Lunch", "Winner", "Prize", "Update", "Password", "Account", "Compromised"]
    message = " ".join(random.choices(words, k=random.randint(5, 20)))
    return message


# Generate dataset
dataset = []
for _ in range(300):
    category = random.choice(["spam", "ham"])
    message = generate_message()
    dataset.append([category, message])

# Write dataset to CSV file
with open("spam_ham_dataset.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Category", "Message"])
    writer.writerows(dataset)

print("Dataset generated successfully.")
