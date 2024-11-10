# 2024.11.06 - itbetyar.hu - Python | main

import streamlit as st

st.title("Ben Streamlit App")
st.header("I am a Hedör!")
st.subheader("I am a subheader!")

st.text(" Ez egy sima **text**, mint ilyen a csillagok nem \"bold-olnak\" semmit")


st.markdown("---")
st.markdown("# Markdown 1 Header")
st.markdown("### Markdown 3 Header")
st.markdown("[Google link](https://www.google.com)")

st.markdown("> Idézet bigyó")
st.markdown("H~2~O")
st.markdown("x^2^")


my_code="""
x = 5
print(f"Hello IT Betyár! X = {x}")
def my_func():
        return:0; 
"""

st.code(my_code, language="python")


col1, col2 = st.columns([1,1])

col1.write("## Ez st.write Header 2 - Oszlop 1")
my_json={"a":"1,2,3","b":"4,5,6"}
col1.json(my_json)

# A swiss army knife of st:
col2.write("### Ez st.write Header 3 - Oszlop 2")
col2.write("Ez egy st.write **vastagon szed** elem. Vagy *dőlt* ha kell")

col2.metric(label="Metric elem", value="153 °C", delta=32)


