import pandas as pd
import streamlit as st
import pickle

from numpy.f2py.cb_rules import cb_rout_rules

st.title("IPL Win Predictor")
teams=['Kolkata Knight Riders', 'Mumbai Indians', 'Rajasthan Royals',
       'Royal Challengers Bangalore', 'Kings XI Punjab',
       'Chennai Super Kings', 'Delhi Capitals', 'Sunrisers Hyderabad']

city=['Delhi', 'Kolkata', 'Ahmedabad', 'Jaipur', 'Bengaluru',
       'Visakhapatnam', 'Hyderabad', 'Indore', 'Mumbai', 'Ranchi',
       'Durban', 'Chandigarh', 'Pune', 'Chennai', 'Bangalore', 'Mohali',
       'Port Elizabeth', 'East London', 'Bloemfontein', 'Rajkot', 'Kochi',
       'Sharjah', 'Johannesburg', 'Dharamsala', 'Abu Dhabi', 'Cape Town',
       'Cuttack', 'Centurion', 'Nagpur', 'Kanpur', 'Kimberley', 'Raipur']

with open('pipe.pkl', 'rb') as f:
    pipe = pickle.load(f)
col1,col2=st.columns(2)
with col1:
       bating_teams=st.selectbox("select the bating teams",teams)
with col2:
       bolling_teams=st.selectbox("select the bolling teams",teams)

selected_city=st.selectbox("select host city",city)
target=st.number_input("target")

col3,col4,col5=st.columns(3)
with col3:
       score=st.number_input("score")
with col4:
       over=st.number_input("over completed")
with col5:
       wicket=st.number_input("wicket out")
if st.button("Prediction"):
       run_left=target-score
       ball_left=120-(over*6)
       remaing_wicket=10-wicket
       crr=score/over
       rrr=(run_left*6)/ball_left
       df=pd.DataFrame({"batting_team":[bating_teams],"bowling_team":[bolling_teams],"city":[selected_city],"currect_score":[score],"run_left":[run_left],"ball_left":[ball_left],"remaing_wicket":[remaing_wicket],"total_runs_x":[target],"crr":[crr],"rrr":[rrr]})
       result=pipe.predict_proba(df)
       st.header(bating_teams+"-" + str(round(result[0][1]*100))+"%")
       st.header(bolling_teams+ "-"+ str(round(result[0][0] * 100))+ "%")

