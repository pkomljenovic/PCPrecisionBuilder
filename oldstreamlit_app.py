import streamlit as st

prices = {
    "Ryzen 5 7600": 230,
    "Ryzen 7 7700X": 340,
    "Intel i5 13600K": 320,
    "RTX 4060": 299,
    "RTX 4070": 599,
    "RX 7800XT": 499,
    "16GB DDR5": 85,
    "32GB DDR5": 150,
    "1TB SSD": 95,
    "2TB SSD": 160,
    "Mid Tower": 90,
    "Full Tower": 140
}

st.title("Precision PC Builder")

name = st.text_input("Customer Name")
purpose = st.selectbox("Purpose", ["Gaming", "Office", "Streaming"])

cpu = st.selectbox("CPU", ["Ryzen 5 7600", "Ryzen 7 7700X", "Intel i5 13600K"])
gpu = st.selectbox("GPU", ["RTX 4060", "RTX 4070", "RX 7800XT"])
ram = st.selectbox("RAM", ["16GB DDR5", "32GB DDR5"])
storage = st.selectbox("Storage", ["1TB SSD", "2TB SSD"])
case = st.selectbox("Case", ["Mid Tower", "Full Tower"])

total = (
    prices[cpu]
    + prices[gpu]
    + prices[ram]
    + prices[storage]
    + prices[case]
)

if st.button("Build PC"):
    if name.strip() == "":
        st.warning("Please enter a customer name.")
    else:
        st.success("Build Created!")

        st.write("Customer:", name)
        st.write("Purpose:", purpose)
        st.write("CPU:", cpu)
        st.write("GPU:", gpu)
        st.write("RAM:", ram)
        st.write("Storage:", storage)
        st.write("Case:", case)

        st.subheader(f"Total Build Cost: ${total:.2f}")