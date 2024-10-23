import streamlit as st
import pandas as pd
from stingbox import stingboxinfo
from stingboxapi.api import data, all_boxes, alerts, hosts

st.set_page_config(
    page_title="StingBox",
    page_icon="👋",
)


# st.sidebar.success("What would you like to check.")

st.title('Hello')

code = st.text_input("Enter a code to search:")

st.button(label='Search')

if code in all_boxes:
    i = all_boxes.index(code)
    st.subheader('StingBox Info')
    stingboxinfo.stingboxinfo(data, i)

    st.subheader('Alerts')
    results = []
    for j in range(len(data)):
        for alert in alerts:
            if alert['name'] == data[i]['name']:
                results.append({
                    'DateTime': alert['ts'],
                    'Alert': alert['alert_text']                                 
                })
    if results:  # Check if results list is not empty
        df = pd.DataFrame(results)
        st.write(df)
    else: st.write('No recent alerts found')
                
    st.subheader('Discovered Hosts')
    results = []
    for j in range(len(data)):
        for host in hosts:
            if host['name'] == data[i]['name']:
                results.append({
                    'IP Address': host['ip'],
                    'MAC Address': host['mac'],
                    'Description': host['description'],
                    'Custom Name': host['custom_description'],
                    'Last Seen': host['ts']
                    })
    if results:  # Check if results list is not empty
        df = pd.DataFrame(results)
        st.write(df)
    else: st.write('No Active Hosts Found')

else:
    st.write('Not found')
    