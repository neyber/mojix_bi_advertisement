import streamlit as st
import pandas as pd
from PIL import Image

# Page Settings
st.set_page_config(layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Data
data = pd.read_csv('Impressions5Campaigns6Days.csv')

# Row A
a1, a2, a3 = st.columns(3)
a1.image(Image.open('streamlit-logo-secondary-colormark-darktext.png'))
a2.metric("Wind", "9 mph", "-8%")
a3.metric("Humidity", "86%", "4%")

# Row B
b1, b2, b3, b4 = st.columns(4)
b1.metric("Temperature", "70 °F", "1.2 °F")
b2.metric("Wind", "9 mph", "-8%")
b3.metric("Humidity", "86%", "4%")
b4.metric("Humidity", "86%", "4%")

# Add campaign name.
campaigns = {
    241093: 'WindowProvider',
    244615: 'LendingService',
    246927: 'BeachHouses',
    247336: 'Soda',
    248782: 'HomeImprovementRetail'
}

def get_campaign_name(campaign_id):
    return campaigns[campaign_id]

data['campaign_name'] = data.apply(lambda row: get_campaign_name(row.campaign_id), axis=1)
data