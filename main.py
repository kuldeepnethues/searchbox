import streamlit as st
from stingbox import stingboxinfo
from stingboxapi.api import data, all_boxes, alerts

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
    for alert in alerts:
        if alert['name'] == data[i]['name']:
            st.write(f"{alert['ts']} : {alert['alert_text']}")


    st.subheader('Discovered Hosts')

else:
    st.write('Not found')
    