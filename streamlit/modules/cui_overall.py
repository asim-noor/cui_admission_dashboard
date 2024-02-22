import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

def draw_overall(admitted):
    fig, ax = plt.subplots(figsize=(6,4))
    ax.bar(x= admitted.groupby(['year'])['campus'].count().index,
        height= admitted.groupby(['year'])['campus'].count().values)
    plt.title("SP-19 to SP24 CUI Annual New Admission")
    plt.xlabel('Year')
    plt.ylabel("Number of Students")
    st.pyplot(fig)

    st.write(admitted.groupby(['campus','year'])['campus'].count().sort_values().unstack().to_markdown())

    st.markdown(

        '''
        Overall significantly less student take admission in CUI during Spring Semester compared to fall semester. The highest % is seen in Islabamabad campus where the the ratio is 36% for last five years. Whereas, Wah and Vehari exhibits lowest ration which is 27%. Some campus heavily rely on Engineering programs for admissions. Engineering programs are now only offered in Fall semester.  

        
     

        |Campus|Spring as % of Total Admissions|
        |:-|:-:|
        |Islamabad (ISB)|36%|
        |Lahore (LHR)|29%|
        |Abbottabad (ATD)|28%|
        |Sahiwal (SWL'|25%|
        |Wah (WAH)|27%|
        |Vehari (VHR)|27%|
        |Attock (ATK)|31%|
     
'''
    )
 