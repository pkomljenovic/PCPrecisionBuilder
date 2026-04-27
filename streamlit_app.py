import streamlit as st

st.title("Precision PC Builder")

name = st.text_input("Customer Name")
purpose = st.selectbox("Purpose", ["Gaming", "Office", "Streaming"])

cpu = st.selectbox("CPU", ["Ryzen 5 7600", "Ryzen 7 7700X", "Intel i5 13600K"])
gpu = st.selectbox("GPU", ["RTX 4060", "RTX 4070", "RX 7800XT"])
ram = st.selectbox("RAM", ["16GB DDR5", "32GB DDR5"])
storage = st.selectbox("Storage", ["1TB SSD", "2TB SSD"])
case = st.selectbox("Case", ["Mid Tower", "Full Tower"])

if st.button("Build PC"):
    st.success("Build Created!")
    st.write("Customer:", name)
    st.write("Purpose:", purpose)
    st.write("CPU:", cpu)
    st.write("GPU:", gpu)
    st.write("RAM:", ram)
    st.write("Storage:", storage)
    st.write("Case:", case)