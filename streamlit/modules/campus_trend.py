import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 



def plot_campus_trend (campus, clr, df):
    fig, ax =plt.subplots(figsize=(6,4))
    ax.bar(x= df[df['campus']==campus].groupby(['year'])['year'].count().index,
        height= df[df['campus']==campus].groupby(['year'])['year'].count().values,
       color=clr)
    plt.title("SP 2019 to SP 2024 Yearly Enrollment of {} ".format(campus))
    plt.xlabel('Year')
    plt.ylabel("Number of Students");
    st.pyplot(fig)



def plot_campus_trend_session_wise (campus, clr, df,session):
    session_to_num_dict = {
        'SP19' : 1,
        'FA19' : 2,
        'SP20' : 3,
        'FA20' : 4,
        'SP21' : 5,
        'FA21' : 6,
        'SP22' : 7,
        'FA22' : 8,
        'SP23' : 9,
        'FA23' : 10,
        'SP24' : 11,
    }
    if (session == True): 
        fig, ax =plt.subplots(figsize=(6,4))
        ax.bar(x= list(session_to_num_dict.keys()),
            height= df[df['campus']==campus].groupby(['num_session'])['num_session'].count().values,
        color=clr)
        plt.title("SP 2019 to SP 2024 Batch wise Enrollment of {} ".format(campus))
        plt.xlabel('session')
        plt.ylabel("Number of Students");
        st.pyplot(fig)
       