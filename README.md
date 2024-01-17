
#  👩🏻‍🍼 Fetal Health Classification Pipeline Project

Reduction of child mortality is reflected in several of the United Nations' Sustainable Development Goals and is a key indicator of human progress. The UN expects that by 2030, countries end preventable deaths of newborns and children under 5 years of age, with all countries aiming to reduce under‑5 mortality to at least as low as 25 per 1,000 live births.

Parallel to the notion of child mortality is of course maternal mortality, which accounts for 295,000 deaths during and following pregnancy and childbirth (as of 2017). The vast majority of these deaths (94%) occurred in low-resource settings, and most could have been prevented. In light of what was mentioned above, Cardiotocograms (CTGs) are a simple and cost accessible option to assess fetal health, allowing healthcare professionals to take action in order to prevent child and maternal mortality. The equipment itself works by sending ultrasound pulses and reading its response, thus shedding light on fetal heart rate (FHR), fetal movements, uterine contractions, and more.



## 🛣️ Development Stages

1. **Data Ingestion Stage**
_Ingesting the dataset from the souce URL provided._

2. **Data Validation Stage**
_Checking the structure of the ingested dataset, and validating it.Based on the validation, a validation file is generated saving the reference of the result of validation._

3. **Data Transformation Stage**
_Transforming the dataset to be feed into the model._

4. **Model Training Stage**
_Modeling various machine learning algorithms and then passing the dataset thorugh the model for training the model._

5. **Model Evaluation Stage**
_After the model has been trained, evaluating the model based on the unknown dataset and then evaluating the accuracy of the model._



 ## ⚒️ Workflows

 1. Update config.yaml
 2. Update parmas.yaml
 3. Update entity
 4. Update the configuration manager in the src config
 5. Update the components
 6. Update the pipeline
 7. Update the main.py
 8. Update the app.py



## ⚙️ Tech Stack

**Programming Language:** Python

**Package used:** Scikit-Learn, Pandas, Numpy, Matplotlib, Seaborn, Streamlit, Scipy, Flask, pyYAML, catBoost, ensure, python_box

## Metrics of the Developed Models

| Model Name | Accuracy | Precision | Recall | F1 Score | Support |
|---|---|---|---|---|---|
| Support Vector Machine | 93.4200 | 93 | 93 | 93 | 635 |
| Random Forest | 91.500 | 93 | 94 | 93 | 635 |
| Decision Tree | 92.950 | 93 | 95 | 93 | 635 |
|K Nearest Neighbors| 92.0100 | 93 | 96 | 93 | 635 |

The accuracy of **SVM model** is the highest accuracy, hence used in the pipeline for prediction


## 💻 How to run?

#### **STEPS,-**

**Step 1:** Clone this repository
```bash
https://github.com/krishanwalia30/Fetal-Health-Classification
```

**Step 2:** Create a conda environment inside the repository
```bash
conda create -n FHC python=3.9 -y
```
```bash
conda activate FHC
```

**Step 3:** Install the requirements
```py
pip install -r requirements.txt
```
```py
# Finally run the following command
python streamlit_app.py
```

**Step 4:** See the project running

```bash
open the link in the terminal [usually at port 8501]
```



## 📏 Outcome

- Learned to create an end-to-end machine learning pipeline.
- Created different modules and components for different stages in pipeline development
- Discovered the functionalities of Streamlit.
- Deployed the webapp successfully on Streamlit.
- Developed Continuous Integration and Development pipeline.



## ⭐ Features

- Machine learning model with an accurcy of __93.42__
- Live Prediction, in minimum time.
- Train Endpoint integration on the webapp



## 🚀 Deployment

The project is deployed as a webapp using Streamlit
Link: https://fetal-health-classification.streamlit.app/




## 📑 Appendix

#### Running the DVC:
Run the following command in the main project command prompt,-
```py
dvc init
dvc repro
```

#### 📖 References:
- https://www.researchgate.net/publication/356666279_Fetal_health_classification_from_cardiotocographic_data_using_machine_learning
- https://www.kaggle.com/datasets/andrewmvd/fetal-health-classification
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10417593/
