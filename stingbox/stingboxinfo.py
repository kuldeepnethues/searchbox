import pandas as pd
import streamlit as st
from stingboxapi.api import data

def stingboxinfo(data, i):
    st.write(pd.DataFrame({
        'Code': data[i]['code'],
        'Key': data[i]['key'],
        'Local IP' : data[i]['last_local_ip'],
        'Public IP' : data[i]['last_public_ip'],
        'MAC Address' : data[i]['mac'],
        'Version' : data[i]['software_version'],
        'Last Activity' : data[i]['last_heartbeat'],
        'SMB Share' : 'Disable' if data[i]['LANSCANSMBSHARES'] == 1 else 'Enable',
        'LAN Discovery': 'Disable' if data[i]['LANSCAN'] == 1 else 'Enable',
        'Custom IP Range': data[i]['CUSTOMRANGE']
    }, index=['value']).transpose())