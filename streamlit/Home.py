import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from  modules.cui_overall import draw_overall
from  modules.campus_trend import plot_campus_trend, plot_campus_trend_session_wise

# set page layout to be wide
#st.set_page_config(layout="wide")
#
st.title("Multipage application demonstration")
campus = st.sidebar.selectbox('Select Campus', ['Overall CUI','Islamabad', 'Lahore','Abbottabad','Vehari', 'Wah', 'Attock'])
analysis_type = st.sidebar.selectbox('Select Analysis Type' ,[
    'CUI Admissions’ Overview',
    'Department Admission Analysis',
    'Campus Admission Trends',
    'CUI Undergraduate and Graduate Admission Trends',
    'Annual Program wise Admissions',
    'Gender Analysis of CUI Students',
    'Merit Trends of Undergraduate Program of CUI',
    'Department wise Acceptance Percentage',
    'Applicantions Analysis',
    'Campus Application Trend',
    'Campus Gaduate and Undergraduate Applications Trend',
    'Annual Program wise Applications',
    'Applicants Gender Analysis'
    ])

with open("CUI Admissions Analysis FA-19 to FA-23.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.sidebar.download_button(label="Export Full Report",
                    data=PDFbyte,
                    file_name="CUI Admissions Analysis FA-19 to FA-23.pdf",
                    mime='application/octet-stream')
colors = {
    'ISB':'#6e78ff',
    'LHR':'#ff7477',
    'ATD':'#f5e960', 
    'SWL':'#adf7b6',
    'WAH':'#bde0fe',
    'VHR':'#9cadce',
    'ATK':'#ffc09f'
}
campuses = {
    'Islamabad'  : 'ISB',
    'Lahore'     : 'LHR',
    'Abbottabad' : 'ATD', 
    'Sahiwal'    : 'SWL',
    'Wah'        : 'WAH',
    'Vehari'     : 'VHR',
    'Attock'     : 'ATK',
}

@st.cache_data
def get_data():
    admitted = pd.read_csv('../data/admitted.csv')
    dfr = pd.read_csv('../data/applicants.csv')
    dfm = pd.read_csv('../data/combined.csv')
    return admitted, dfr, dfm

admitted, dfr, dfm = get_data()

if(campus == 'Overall CUI'):
    draw_overall(admitted)
else:
    plot_campus_trend(campuses[campus],colors[campuses[campus]], admitted)

    plot_campus_trend_session_wise(campuses[campus],colors[campuses[campus]], admitted, True)