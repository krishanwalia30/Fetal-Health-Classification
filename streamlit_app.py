import pandas as pd
import streamlit as st
from FetalHealthC.pipeline.prediction import PredictionPipeline

class ClientApp:
    def __init__(self):
        self.filename = 'test.csv'
        self.classifier = PredictionPipeline(self.filename)

def main():
    # Set page title and favicon

    st.set_page_config(
    page_title="Fetal Health Monitor",
    page_icon="🏥",
    layout="centered",
    # menu_items={
    #     'Get Help': 'https://www.extremelycoolapp.com/help',
    #     'Report a bug': "https://www.extremelycoolapp.com/bug",
    #     'About': "# This is a header. This is an *extremely* cool app!",
    # }
)   

    st.title('Fetal Health Prediction')
    
    columns = ['baseline value','accelerations','fetal_movement','uterine_contractions','light_decelerations','severe_decelerations','prolongued_decelerations','abnormal_short_term_variability','mean_value_of_short_term_variability','percentage_of_time_with_abnormal_long_term_variability','mean_value_of_long_term_variability','histogram_width','histogram_min','histogram_max','histogram_number_of_peaks','histogram_number_of_zeroes','histogram_mode','histogram_mean','histogram_median','histogram_variance','histogram_tendency']

    # Form with 22 number fields
    with st.form('FetalHealthClassification'):
        # st.image('template/images/fetal_health.jpg', clamp=True, caption="Fetal Health")
        data = dict()
        for i in columns:
            data[i] = st.number_input(label=f'{i}', key= f'{i}')
            
        submit_button = st.form_submit_button(label='Submit')
        if submit_button:
            df = pd.DataFrame(data, index=[0])
            df.to_csv(clApp.filename, index=False)
            result = clApp.classifier.predict()
            print(result)
            st.write(result)
    

if __name__ == "__main__":
    clApp = ClientApp()
    main()
