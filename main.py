import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Elderly Project",
    page_icon="🧓🏼",
    layout="wide")

# Inject Custom CSS
st.markdown("""
    <style>
        /* Select all divs that contain a <p> tag (label container) */
        div:has(> p) {
            font-size: 18px !important;
            font-weight: bold !important;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Modgut's Elderly Project")
st.subheader('Filter data to find healthy people with following criteria:')

df = pd.read_csv('data.csv')

col1, spacer1, col2, spacer2, col3 = st.columns([1, 0.1, 1, 0.1, 1])

with col1:
    BMI_list = st.multiselect('Select BMI Group:', ('underweight','normal','overweight','obese','severe obese'),('underweight','normal','overweight'))
    TE_range = st.slider("Select Normal Range of TE (kPa):", 0, int(df['TE (kPa)'].max())+1, (0, 7))
    FBS_range = st.slider("Select Normal Range of FBS (mg/dL):", 0, int(df['FBS (mg/dL)'].max())+1, (int(df['FBS (mg/dL)'].min())-1, int(df['FBS (mg/dL)'].max())+1))
    HDL_range = st.slider("Select Normal Range of HDL-Cholesterol:", 0, int(df['HDL-Cholesterol'].max())+1, (int(df['HDL-Cholesterol'].min())-1, int(df['HDL-Cholesterol'].max())+1))
    Globulin_range = st.slider("Select Normal Range of Globulin:", 0, int(df['Globulin (Total protein-albumin)'].max())+1, (int(df['Globulin (Total protein-albumin)'].min())-1, int(df['Globulin (Total protein-albumin)'].max())+1))
    Bilirubin_T_range = st.slider("Select Normal Range of Bilirubin (Total):", 0, int(df['Bilirubin (Total)'].max())+1, (int(df['Bilirubin (Total)'].min())-1, int(df['Bilirubin (Total)'].max())+1))
    ALT_range = st.slider("Select Normal Range of SGPT (ALT):", 0, int(df['SGPT (ALT)'].max())+1, (int(df['SGPT (ALT)'].min())-1, int(df['SGPT (ALT)'].max())+1))
    HGB_range = st.slider("Select Normal Range of Hemoglobin(HGB):", 0, int(df['Hemoglobin(HGB)'].max())+1, (int(df['Hemoglobin(HGB)'].min())-1, int(df['Hemoglobin(HGB)'].max())+1))
    White_range = st.slider("Select Normal Range of White Cell Count:", 0, int(df['White cell count'].max())+1, (int(df['White cell count'].min())-1, int(df['White cell count'].max())+1))
    Plasma_range = st.slider("Select Normal Range of Normal Plasma (sec):", 0, int(df['Normal Plasma (sec)'].max())+1, (int(df['Normal Plasma (sec)'].min())-1, int(df['Normal Plasma (sec)'].max())+1))
    eGFR_range = st.slider("Select Normal Range of Thai eGFR (mL/min/1.73m2) Blood:", 0, int(df['Thai eGFR (mL/min/1.73m2) Blood '].max())+1, (int(df['Thai eGFR (mL/min/1.73m2) Blood '].min())-1, int(df['Thai eGFR (mL/min/1.73m2) Blood '].max())+1))
    LAD_range = st.slider("Select Normal Range of LAD:", 0, int(df['LAD'].max())+1, (int(df['LAD'].min())-1, int(df['LAD'].max())+1))
    take_pill = st.selectbox('Take Pill:', ("No", "Yes"))

with col2:
    TMAO_range = st.slider("Select Normal Range of TMAO (umol/l):", 0, int(df['ผล plasma TMAO (umol/l)'].max())+1, (0, 6))
    CAC_range = st.slider("Select Normal Range of Coronary Calcium Scan (CAC):", 0, int(df['Coronary Calcium Scan (CAC)'].max())+1, (0, 100))
    HbA1C_range = st.slider("Select Normal Range of HbA1C (%):", 0, int(df['HbA1C %'].max())+1, (int(df['HbA1C %'].min())-1, int(df['HbA1C %'].max())+1))
    LDL_range = st.slider("Select Normal Range of LDL-Cholesterol:", 0, int(df['LDL-Cholesterol (direct)'].max())+1, (int(df['LDL-Cholesterol (direct)'].min())-1, int(df['LDL-Cholesterol (direct)'].max())+1))
    Protein_range = st.slider("Select Normal Range of Total Protein:", 0, int(df['Total protein'].max())+1, (int(df['Total protein'].min())-1, int(df['Total protein'].max())+1))
    Bilirubin_D_range = st.slider("Select Normal Range of Bilirubin (Direct):", 0, int(df['Bilirubin (Direct)'].max())+1, (int(df['Bilirubin (Direct)'].min())-1, int(df['Bilirubin (Direct)'].max())+1))
    ALP_range = st.slider("Select Normal Range of Alkaline Phosphatase (ALP):", 0, int(df['Alkaline Phosphatase (ALP)'].max())+1, (int(df['Alkaline Phosphatase (ALP)'].min())-1, int(df['Alkaline Phosphatase (ALP)'].max())+1))
    HCT_range = st.slider("Select Normal Range of Hematocrit (HCT):", 0, int(df['Hematocrit (HCT)'].max())+1, (int(df['Hematocrit (HCT)'].min())-1, int(df['Hematocrit (HCT)'].max())+1))
    Neutrophils_range = st.slider("Select Normal Range of Neutrophils (%):", 0, int(df['Neutrophils %'].max())+1, (int(df['Neutrophils %'].min())-1, int(df['Neutrophils %'].max())+1))
    INR_range = st.slider("Select Normal Range of INR:", 0, int(df['INR'].max())+1, (int(df['INR'].min())-1, int(df['INR'].max())+1))
    Uric_range = st.slider("Select Normal Range of Uric Acid:", 0, int(df['uric acid'].max())+1, (int(df['uric acid'].min())-1, int(df['uric acid'].max())+1))
    LCX_range = st.slider("Select Normal Range of LCX:", 0, int(df['LCX'].max())+1, (int(df['LCX'].min())-1, int(df['LCX'].max())+1))

with col3:
    CAP_range = st.slider("Select Normal Range of CAP (dB/m):", 0, int(df['CAP (dB/m)'].max())+1, (0, 248))
    AFP_range = st.slider("Select Normal Range of Alpha Fetoprotein (AFP) IU/ml:", 0, int(df['Alpha Fetoprotein (AFP) IU/ml'].max())+1, (int(df['Alpha Fetoprotein (AFP) IU/ml'].min()), int(df['Alpha Fetoprotein (AFP) IU/ml'].max())+1))
    Cholesterol_range = st.slider("Select Normal Range of Cholesterol (total):", 0, int(df['Cholesterol (total)'].max())+1, (int(df['Cholesterol (total)'].min())-1, int(df['Cholesterol (total)'].max())+1))
    Triglyceride_range = st.slider("Select Normal Range of Triglyceride (lipid-TG):", 0, int(df['Triglyceride (lipid-TG)'].max())+1, (int(df['Triglyceride (lipid-TG)'].min())-1, int(df['Triglyceride (lipid-TG)'].max())+1))
    Albumin_range = st.slider("Select Normal Range of Albumin:", 0, int(df['Albumin'].max())+1, (int(df['Albumin'].min())-1, int(df['Albumin'].max())+1))
    AST_range = st.slider("Select Normal Range of SGOT (AST):", 0, int(df['SGOT (AST)'].max())+1, (int(df['SGOT (AST)'].min())-1, int(df['SGOT (AST)'].max())+1))
    Red_range = st.slider("Select Normal Range of Red Cell Count:", 0, int(df['red cell count'].max())+1, (int(df['red cell count'].min())-1, int(df['red cell count'].max())+1))
    Platelets_range = st.slider("Select Normal Range of Platelets counts:", 0, int(df['Platelets counts'].max())+1, (int(df['Platelets counts'].min())-1, int(df['Platelets counts'].max())+1))
    Prothrombin_range = st.slider("Select Normal Range of Prothrombin Time (sec):", 0, int(df['Prothrombin Time (sec)'].max())+1, (int(df['Prothrombin Time (sec)'].min())-1, int(df['Prothrombin Time (sec)'].max())+1))
    Creatinine_range = st.slider("Select Normal Range of Creatinine (mg/dL) Blood:", 0, int(df['Creatinine (mg/dL) Blood'].max())+1, (int(df['Creatinine (mg/dL) Blood'].min())-1, int(df['Creatinine (mg/dL) Blood'].max())+1))
    LMA_range = st.slider("Select Normal Range of LMA:", 0, int(df['LMA'].max())+1, (int(df['LMA'].min())-1, int(df['LMA'].max())+1))
    RCA_range = st.slider("Select Normal Range of RCA:", 0, int(df['RCA'].max())+1, (int(df['RCA'].min())-1, int(df['RCA'].max())+1))

st.subheader('Number of healthy people = ' + str(df[(df['BMI_group'].isin(BMI_list)) & 
                                                    
                                  (((TMAO_range[0] <= df['ผล plasma TMAO (umol/l)']) & (df['ผล plasma TMAO (umol/l)'] <= TMAO_range[1]))
                                  | (df['ผล plasma TMAO (umol/l)'].isnull())) &

                                  (((CAP_range[0] <= df['CAP (dB/m)']) & (df['CAP (dB/m)'] <= CAP_range[1]))
                                  | (df['CAP (dB/m)'].isnull())) &

                                  (((TE_range[0] <= df['TE (kPa)']) & (df['TE (kPa)'] <= TE_range[1]))
                                  | (df['TE (kPa)'].isnull())) &

                                  (((CAC_range[0] <= df['Coronary Calcium Scan (CAC)']) & (df['Coronary Calcium Scan (CAC)'] <= CAC_range[1]))
                                  | (df['Coronary Calcium Scan (CAC)'].isnull())) &

                                  (((AFP_range[0] <= df['Alpha Fetoprotein (AFP) IU/ml']) & (df['Alpha Fetoprotein (AFP) IU/ml'] <= AFP_range[1]))
                                  | (df['Alpha Fetoprotein (AFP) IU/ml'].isnull())) &

                                  (((FBS_range[0] <= df['FBS (mg/dL)']) & (df['FBS (mg/dL)'] <= FBS_range[1]))
                                  | (df['FBS (mg/dL)'].isnull())) &

                                  (((HbA1C_range[0] <= df['HbA1C %']) & (df['HbA1C %'] <= HbA1C_range[1]))
                                  | (df['HbA1C %'].isnull())) &

                                  (((Cholesterol_range[0] <= df['Cholesterol (total)']) & (df['Cholesterol (total)'] <= Cholesterol_range[1]))
                                  | (df['Cholesterol (total)'].isnull())) &

                                  (((HDL_range[0] <= df['HDL-Cholesterol']) & (df['HDL-Cholesterol'] <= HDL_range[1]))
                                  | (df['HDL-Cholesterol'].isnull())) &

                                  (((LDL_range[0] <= df['LDL-Cholesterol (direct)']) & (df['LDL-Cholesterol (direct)'] <= LDL_range[1]))
                                  | (df['LDL-Cholesterol (direct)'].isnull())) &

                                  (((Triglyceride_range[0] <= df['Triglyceride (lipid-TG)']) & (df['Triglyceride (lipid-TG)'] <= Triglyceride_range[1]))
                                  | (df['Triglyceride (lipid-TG)'].isnull())) &

                                  (df['take_pill'] == take_pill)

                                  ].shape[0]))