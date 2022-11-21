import streamlit as st
import plotly.graph_objects as ob
from PIL import Image
from datetime import datetime
import calendar


#setting variables
page_title = "AVOR CASH TRACKER"
page_icon = ":bar_chart:"
layout = "centered"
incomes = ["salary", "rent income", "business", "other income"]
expenses = ["rent","savings","busiiness expenses", "other expenses"]
currency = "ksh"
logo = Image.open("image/Logopit_1668939612159.png")

#web page configuration
with st.container():
    logo_column, title_column = st.columns((1,2))
    with logo_column:
        st.image(logo)
    with title_column:
        st.title(page_title)
#inputing dates
years = (datetime.today().year, datetime.today().year +1)
months = list(calendar.month_name [1:])

#making forms
st.subheader(f"ENTRY IN {currency}")
with st.form("entry_form", clear_on_submit = True):
    col1, col2 = st.columns(2)
    col1.selectbox("select month", months, key="months")
    col2.selectbox("select year", years, key="years")

    "---"
    with st.expander("incomes"):
        for income in incomes:
            st.number_input(f"{income}", min_value = 0, format = "%i", step = 10, key=income)
    with st.expander("expenses"):
        for expense in expenses:
            st.number_input(f"{expense}", min_value = 0, format = "%i", step = 10, key =expense)
    with st.expander("comments"):
        st.text_area("", placeholder = "enter commnt here")

    "---"
#configuring the submit button
    submitted = st.form_submit_button("save data")
    if submitted:
        period = str(st.session_state["years"]) + "_" + str(st.session_state["months"])
        incomes = {income:st.session_state[income] for income in incomes}
        expenses = {expense:st.session_state[expense] for expense in expenses}
        #to_do insert period incomes and expenses to data base
        st.write(f"incomes are{incomes}")
        st.write(f"expenses are{expenses}")
        st.success("data saved")
