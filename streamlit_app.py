import os
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
    layout="wide",
    # menu_items={
    #     'Get Help': 'https://www.extremelycoolapp.com/help',
    #     'Report a bug': "https://www.extremelycoolapp.com/bug",
    #     'About': "# This is a header. This is an *extremely* cool app!",
    # }
)   

    
    columns = ['baseline value','accelerations','fetal_movement','uterine_contractions','light_decelerations','severe_decelerations','prolongued_decelerations','abnormal_short_term_variability','mean_value_of_short_term_variability','percentage_of_time_with_abnormal_long_term_variability','mean_value_of_long_term_variability','histogram_width','histogram_min','histogram_max','histogram_number_of_peaks','histogram_number_of_zeroes','histogram_mode','histogram_mean','histogram_median','histogram_variance','histogram_tendency']
    column_labels = ['Baseline Value', 'Accelerations', 'Fetal Movement', 'Uterine Contractions', 'Light Deceleration', 'Severe Decelerations', 'Prolonged Deceleration', ' Abnormal Short Term Variability', 'Mean Value of Short Term Variability', 'Percentage of Time With Abnormal Long Term Variability', 'Mean Value of Long Term Variability', 'Histogram Width', 'Histogram Minimum', 'Histogram Maximum', 'Histogram Number of Peaks', 'Histogram Number of Zeroes', 'Histogram Mode','Histogram Mean', 'Histogram Median', 'Histogram Variances', 'Histogram Tendency']

    st.title('👩🏻‍🍼:grey[Fetal Health Prediction]', anchor=False)

    # col1, col2 = st.columns([1,3])
    # with col1:
    #     st.write()
    
    # with col2:
    st.write("Reduction of child mortality is reflected in several of the United Nations' Sustainable Development Goals and is a key indicator of human progress. The UN expects that by 2030, countries end preventable deaths of newborns and children under 5 years of age, with all countries aiming to reduce under‑5 mortality to at least as low as 25 per 1,000 live births. \n\n Parallel to notion of child mortality is of course maternal mortality, which accounts for 295,000 deaths during and following pregnancy and childbirth (as of 2017). The vast majority of these deaths (94%) occurred in low-resource settings, and most could have been prevented.In light of what was mentioned above, Cardiotocograms (CTGs) are a simple and cost accessible option to assess fetal health, allowing healthcare professionals to take action in order to prevent child and maternal mortality. The equipment itself works by sending ultrasound pulses and reading its response, thus shedding light on fetal heart rate (FHR), fetal movements, uterine contractions and more.")
        



    col3, col4 = st.columns([1.7,1])
    

    col3.subheader('📄:green[Enter Details in the form below]', anchor=False)
    with col3.form('FetalHealthClassification', border=False):

        # Form with 22 number fields
        data = dict()
        for i in range(len(column_labels)):
            data[columns[i]] = st.number_input(label=f":orange[{column_labels[i]}]", key= f'{columns[i]}', format='%f')
            
        submit_button = st.form_submit_button(label='Submit', use_container_width=True, type='primary')
        if submit_button:
            df = pd.DataFrame(data, index=[0])
            df.to_csv(clApp.filename, index=False)

            result = clApp.classifier.predict()
            # print(result)
            if result == 1:
                st.subheader(":green[Result:] The baby is normal")
            elif result == 2:
                st.subheader(":blue[Result:] The health of the baby is suspecious")
                st.write("It is highly recommended to visit the doctor as a preventive measure to take care of the health of both the mother and the baby.")
            else:
                st.subheader(":red[Result:] The baby is pathological")
                st.write("It is highly recommended to visit the doctor as a preventive measure to take care of the health of both the mother and the baby.")
    
    col4.subheader('', anchor=False)
    with col4:
        accuracy_models = [
            ['Support Vector Machine', 93.42,93,93,93,635],
            ['Random Forest', 91.5,93,94,93,635],
            ['Decision Tree', 92.95,93,95,93,635],
            ['K Nearest Neighbors', 92.01,93,96,93,635],
        ]

        st.image('template/images/fetal_health.jpg', clamp=True, caption="Fetal Health")
        st.subheader(':green[Introduction]')
        st.write("Fetal and maternal health have a close correlation. Reducing the fetal death rate and monitoring fetal health conditions are essential formaintaining good health for both mother and child. CTG or electronic fetal monitoring (EFM) is the prenatal test for monitoring uterine contrac-tions and fetal heartbeat during pregnancy and childbirth.")
        
        df = pd.DataFrame(accuracy_models, columns=['Model', 'Accuracy', 'Precision', 'Recall', 'F1-Score', 'Support'], index=[1,2,3,4])
        st.subheader(":green[Machine Learning]")
        st.write("Machine Learning (ML) techniques can help medical experts make early decisions during complex situations like diagnosis, effectively decreasingthe MMR and high complications during labour. Classifying the stages of fetal health is a challenging task, but this can be outstandingly handledby ML classification techniques.\n\n Several Machine Learning models were developed and optimized for more accurate predictions in the fetal health classification. The models developed and the score obtained from the model developed are as follows:")
        st.table(df)

        st.subheader(":green[Conclusion]")
        st.write("Analyzing the scores of the classification done on the test data. Among all the machine learning models, it has been found that **Support Vector Machine** has given the best results.")

        st.subheader(":green[References]")
        st.write("The following references have been used for this project:")

        st.markdown("""- <html>
                    <head></head>
                    <body>
                        <div>
                            <a href="https://www.researchgate.net/publication/356666279_Fetal_health_classification_from_cardiotocographic_data_using_machine_learning"> Fetal Health Classification From CTG </a>
                        </div>
                    </body>
                    </html>""",unsafe_allow_html=True)
        
        st.markdown("""- <html>
                    <head></head>
                    <body>
                        <div>
                            <a href="https://www.kaggle.com/datasets/andrewmvd/fetal-health-classification"> Fetal Health Classification Dataset </a>
                        </div>
                    </body>
                    </html>""",unsafe_allow_html=True)
        
        st.markdown("""- <html>
                    <head></head>
                    <body>
                        <div>
                            <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10417593/"> Early Diagnosis and Classification of Fetal Health Status </a>
                        </div>
                    </body>
                    </html>""",unsafe_allow_html=True)

if __name__ == "__main__":
    clApp = ClientApp()
    main()