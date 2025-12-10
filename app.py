import streamlit as st
import pandas as pd
import pickle


## load pipeline
with open('pipe.pkl', 'rb') as f:
    pipe = pickle.load(f)


st.title("German Credit Risk: Customer Segmentation Engine")

df = pd.read_csv("data/german_credit_data.csv")
df_data_profile= pd.read_csv("data/data_profile.csv")



def classify_new_user(record):
    df_test = pd.DataFrame([record])
    cluster= pipe.predict(df_test)[0]
    return display_interpretation(cluster)
# --- INTERPRETATION MODULE CODE ---

CLUSTER_PROFILES = {
    0: {
        "name": "The VIP Investor",
        "tagline": "High Credit • Long Duration • Older",
        "verdict": "High Risk / High Reward",
        "action": "MONITOR: Assign Relationship Manager to prevent default.",
        "color": "red" 
    },
    1: {
        "name": "The Young Starter",
        "tagline": "Low Credit • Young • Female-Leaning",
        "verdict": "Medium Risk / Future Growth",
        "action": "NURTURE: Cross-sell starter products to build loyalty.",
        "color": "blue"
    },
    2: {
        "name": "The Middle-Class Core",
        "tagline": "Medium Credit • Established • Stable",
        "verdict": "Low Risk / Steady Reward",
        "action": "RETAIN: This is your standard stable customer.",
        "color": "green"
    },
    3: {
        "name": "The Cautious Senior",
        "tagline": "Low Credit • Older • Short Duration",
        "verdict": "Lowest Risk / Low Reward",
        "action": "AUTOMATE: Low profit margin; serve via App/ATM.",
        "color": "gray"
    }
}

# 2. The Display Function
def display_interpretation(cluster_id):

    profile = CLUSTER_PROFILES.get(cluster_id, {})
    
    with st.container():
        st.markdown("---")
        st.subheader(f"🎯 Prediction: Cluster {cluster_id}")
        
        st.markdown(f"### **{profile['name']}**")
        st.caption(profile['tagline'])
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.info(f"**Financial Verdict:**\n\n{profile['verdict']}")
            
        with col2:
            if profile['color'] == 'red':
                st.error(f"**Strategic Action:**\n\n{profile['action']}")
            elif profile['color'] == 'green':
                st.success(f"**Strategic Action:**\n\n{profile['action']}")
            else:
                st.warning(f"**Strategic Action:**\n\n{profile['action']}")




# Input fields
age = st.number_input("Age", min_value=18, max_value=100, value=30)
sex = st.selectbox("Sex", options=df['Sex'].unique())
job = st.selectbox("Job", options=df['Job'].unique())   
housing = st.selectbox("Housing", options=df['Housing'].unique())
saving_accounts = st.selectbox("Saving Accounts", options=df['Saving accounts'].dropna().unique())
checking_account = st.selectbox("Checking Account", options=df['Checking account'].dropna().unique())
credit_amount = st.number_input("Credit Amount", min_value=100, max_value=100000, value=1000)
duration = st.number_input("Duration (in months)", min_value=1, max_value=72, value=12)
purpose = st.selectbox("Purpose", options=df['Purpose'].unique())


new_user = {
    'Age': age,
    'Sex': sex,
    'Job': job,
    'Housing': housing,
    'Saving accounts': saving_accounts,
    'Checking account': checking_account,
    'Credit amount': credit_amount,
    'Duration': duration,
    'Purpose': purpose
}

if st.button("Predict Cluster"):
    classify_new_user(new_user)
 