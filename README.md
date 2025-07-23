# 🏏 IPL Win Predictor
A machine learning-powered Streamlit web app that predicts the winning probability of an IPL team based on real-time match conditions such as score, overs, wickets, and venue.

## 📌 Project Description
This project predicts the probability of a team winning an IPL match using **logistic regression**. It processes historical IPL match data to extract key features, then uses a trained model to estimate the winning chances during a live match scenario.


## 🔍 Features

- Select batting and bowling teams
- Choose host city and target score
- Input current match conditions (score, overs, wickets)
- Display real-time winning probabilities for both teams
- Trained model with **82% accuracy**
- Web interface built using **Streamlit**


## 📊 Data Source
Dataset used:
- [IPL Matches and Deliveries Dataset](https://www.kaggle.com/datasets/haroon669/ipl-matches-and-deliveries-dataset)

Files:
- `matches.csv`
- `deliveries.csv`


## 🛠️ Data Preprocessing

### Extracted Features:
The following features were created by combining and preprocessing the match and delivery datasets:

- `currect_score`: Current team score
- `run_left`: Runs remaining to win
- `ball_left`: Balls remaining (out of 120)
- `remaing_wicket`: Wickets left (out of 10)
- `total_runs_x`: Target score
- `crr`: Current Run Rate = runs / overs
- `rrr`: Required Run Rate = (run_left * 6) / balls_left
- `result`: 1 if batting team won, else 0

### Techniques used:
- `ColumnTransformer` for categorical and numerical preprocessing
- `LogisticRegression` classifier
- Binary classification setup (win or loss)


## 🤖 Machine Learning Model

- **Algorithm**: Logistic Regression
- **Type**: Binary Classification
- **Pipeline**: 
  - Feature encoding with `ColumnTransformer`
  - Logistic Regression model in `scikit-learn` pipeline
- **Accuracy**: ~82%


## 🚀 How to Run
### 1. Clone the Repository

```bash
git clone https://github.com/your-username/IPL-Win-Predictor.git
cd IPL-Win-Predictor
