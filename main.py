import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Elderly Project",
    page_icon="🧓🏼",
    layout="wide")

st.title("Modgut's Elderly Project")
st.write('Filter data to find healthy people with following criteria:')

df = pd.read_csv('data.csv')

#'Alpha Fetoprotein (AFP) IU/ml','FBS (mg/dL)','HbA1C %','Cholesterol (total)','HDL-Cholesterol','Triglyceride (lipid-TG)','LDL-Cholesterol (direct)','Globulin (Total protein-albumin)','Total protein','Albumin','Bilirubin (Total)','Bilirubin (Direct)','SGOT (AST)','SGPT (ALT)','Alkaline Phosphatase (ALP)','red cell count','Hemoglobin(HGB)','Hematocrit (HCT)','Platelets counts','White cell count','Neutrophils %','Prothrombin Time (sec)','Normal Plasma (sec)','INR','Creatinine (mg/dL) Blood','Thai eGFR (mL/min/1.73m2) Blood ','uric acid','ยาไขมัน','ยาความดัน','ยาเบาหวาน','อื่นๆ','CAP (dB/m)','CAP_group','TE (kPa)','TE_group','Coronary Calcium Scan (CAC)','CAC_group','LMA','LAD','LCX','RCA'

BMI_group = st.multiselect('Select BMI Group:', ('underweight','normal','overweight','obese','severe obese'))
st.write('BMI:', BMI_group)

#BMI_group = st.selectbox('Select BMI Group:', ('underweight','normal','overweight','obese','severe obese'))
#st.write('You criteria:', BMI_group)

TMAO_group = st.slider("Select Normal Range of TMAO:", df['ผล plasma TMAO (umol/l)'].min(), df['ผล plasma TMAO (umol/l)'].max(), (0.0, 6.0))
st.write('TMAO:', TMAO_group)

st.write('Number of persons:', df.shape[0])