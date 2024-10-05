# Spam Detection using SVM

This project is a simple spam detection program that classifies emails as either "spam" or "ham" (non-spam) using a Support Vector Machine (SVM) model. The program uses text data from a CSV file to train the model, which can then be used to classify new emails based on their content.

## Features

- **Data Preprocessing:** Uses a `CountVectorizer` to convert email text into a matrix of token counts.
- **Model Training:** Trains a Support Vector Machine (SVM) using the email text as features and their spam classification as labels.
- **Email Prediction:** Takes user input for email content and predicts whether the email is spam or ham.

## Requirements

- Python 3.x
- Pandas
- Scikit-learn

To install the necessary libraries, run the following command:

```bash
pip install pandas scikit-learn
```

## Dataset

The program expects a CSV file named `emails.csv` containing two columns:

- `text`: The email text.
- `spam`: A label where 1 represents spam and 0 represents ham (non-spam).

## How to Run

1. Place the `emails.csv` file in the same directory as the script.
2. Run the script using Python:

```bash
python main.py
```

3. After the training is completed, you can input the text of an email, and the program will classify it as either spam or ham.

4. To exit the program, type `exit()`.

## Example

```bash
Enter the email text: "Congratulations! You've won a prize!"
The email is Spam

Enter the email text: "Meeting tomorrow at 10 AM"
The email is Ham
```
