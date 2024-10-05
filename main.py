import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm

email = pd.read_csv('emails.csv')
print(email.head())

x = email['text']
y = email['spam']

x_train, x_test,y_train, y_test =train_test_split(x,y,test_size=0.2,random_state = 1000)

print("")
print('X_train : ')
print(x_train.head())
print(x_train.shape)

print('')
print('X_test : ')
print(x_test.head())
print(x_test.shape)

print('')
print('y_train : ')
print(y_train.head())
print(y_train.shape)

print('')
print('y_test : ')
print(y_test.head())
print(y_test.shape)

cv = CountVectorizer()
features = cv.fit_transform(x_train)

print(cv)
print(features)

linear_model = svm.SVC()
linear_model.fit(features, y_train)

feature_test = cv.transform(x_test)
print(f"Accuraccy : {linear_model.score(feature_test,y_test)}")


def predict_email(text):
  text_feature = cv.transform([text])
  prediciting_email = linear_model.predict(text_feature)
  return prediciting_email[0]

print("====================================================================")
while True :
  email_text = input("Enter the email text : ")
  prediction = predict_email(email_text)
  print("\n")
  if email_text == "exit()":
    break
  print(f"\nThe email is {'Ham' if prediction == 0 else 'Spam'}")
  
  print("\n")
  

print(" Bye Bye !! ")
