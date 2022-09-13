import streamlit as st
import pandas as pd
import plotly.express as px

# Page Settings
st.set_page_config(layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("Advertisement Dashboard")

# Data
data = pd.read_csv('Impressions5Campaigns6Days.csv')

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

complete_view = round(data['complete_view'].sum()*100/data['complete_view'].count(), 4)
adv_clicked = round(data['clicks'].loc[data['clicks'] == 1].sum()*100/data['impressions'].count(), 4)
adv_impressions = round(data['impressions'].loc[data['impressions'] == 1].sum()*100/data['impressions'].count(), 4)

# KPIs
a1, a2, a3 = st.columns(3)
a1.metric("Viewed Fully", str(complete_view) + '%')
a2.metric("Ad Clicks", str(adv_clicked) + '%')
a3.metric("Ad Impressions", str(adv_impressions) + '%')

# Charts
b1, b2 = st.columns(2)

with b1:
    st.markdown('### Viewed Fully Per Campaign')
    data_chart1 = data.loc[data['complete_view'] == 1].groupby('campaign_name').count().reset_index().sort_values(['complete_view'], ascending=True)
    fig = px.bar(data_chart1, x=data_chart1['complete_view'], y=data_chart1['campaign_name'], orientation='h', text=None)
    st.write(fig)
    
with b2:
    st.markdown('### Viewed Fully Per Device')
    data_chart2 = data.loc[data['complete_view'] == 1].groupby('device_type').count().reset_index().sort_values(['complete_view'], ascending=True)
    fig = px.bar(data_chart2, x=data_chart2['complete_view'], y=data_chart2['device_type'], orientation='h', text=None)
    st.write(fig)

c1, c2 = st.columns(2)

with c1:
    st.markdown('### Viewed Fully Trend Per Date and Campaign')
    data_time_series1 = data.loc[data['complete_view'] == 1].groupby(['campaign_name', 'date_pst']).count().reset_index().sort_values(['complete_view'], ascending=True)
    fig = px.bar(data_time_series1, x='date_pst', y='complete_view', color='campaign_name', barmode='group')
    st.write(fig)

with c2:
    st.markdown('### Viewed Fully Trend Per Date and Device')
    data_time_series2 = data.loc[data['complete_view'] == 1].groupby(['device_type', 'date_pst']).count().reset_index().sort_values(['complete_view'], ascending=True)
    fig = px.bar(data_time_series2, x='date_pst', y='complete_view', color='device_type', barmode='group')
    st.write(fig)