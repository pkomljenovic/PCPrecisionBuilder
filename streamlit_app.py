import streamlit as st

# -----------------------------
# Precision PC Builder App
# Sprint 14 UX Refactor
# -----------------------------

st.set_page_config(
    page_title="Precision PC Builder",
    page_icon="🖥️",
    layout="centered"
)

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

st.title("🖥️ Precision PC Builder")
st.write("Build a custom PC by choosing your purpose and parts. The total updates automatically.")

st.divider()

# -----------------------------
# Customer Info
# -----------------------------
st.header("1. Customer Information")

name = st.text_input(
    "Customer Name",
    placeholder="Enter customer name",
    help="This name will appear on the final build summary."
)

purpose = st.selectbox(
    "Build Purpose",
    ["Gaming", "Office", "Streaming"],
    help="Choose what the PC will mainly be used for."
)

st.divider()

# -----------------------------
# Component Selection
# -----------------------------
st.header("2. Choose Your Components")

col1, col2 = st.columns(2)

with col1:
    cpu = st.selectbox(
        "CPU",
        ["Ryzen 5 7600", "Ryzen 7 7700X", "Intel i5 13600K"],
        help="The CPU is the main processor of the computer."
    )

    ram = st.selectbox(
        "RAM",
        ["16GB DDR5", "32GB DDR5"],
        help="RAM helps the computer run multiple programs smoothly."
    )

    case = st.selectbox(
        "Case",
        ["Mid Tower", "Full Tower"],
        help="The case holds all the computer parts."
    )

with col2:
    gpu = st.selectbox(
        "GPU",
        ["RTX 4060", "RTX 4070", "RX 7800XT"],
        help="The GPU affects gaming, streaming, and graphics performance."
    )

    storage = st.selectbox(
        "Storage",
        ["1TB SSD", "2TB SSD"],
        help="Storage is where files, games, and programs are saved."
    )

st.divider()

# -----------------------------
# Price Calculation
# -----------------------------
total = (
    prices[cpu]
    + prices[gpu]
    + prices[ram]
    + prices[storage]
    + prices[case]
)

st.header("3. Live Build Total")

st.metric("Estimated Total Cost", f"${total:.2f}")

budget = st.slider(
    "Optional Budget Check",
    min_value=500,
    max_value=2000,
    value=1000,
    step=50,
    help="Use this to see if the build fits within a target budget."
)

if total <= budget:
    st.success("This build is within your selected budget.")
else:
    st.warning("This build is over your selected budget.")

progress = min(total / budget, 1.0)
st.progress(progress)

st.divider()

# -----------------------------
# Final Summary
# -----------------------------
st.header("4. Final Build Summary")

if st.button("Create Build Summary"):
    if name.strip() == "":
        st.error("Please enter a customer name before creating the build.")
    else:
        st.success("Build Created Successfully!")

        st.subheader("Customer Build Details")
        st.write(f"**Customer:** {name}")
        st.write(f"**Purpose:** {purpose}")
        st.write(f"**CPU:** {cpu} - ${prices[cpu]}")
        st.write(f"**GPU:** {gpu} - ${prices[gpu]}")
        st.write(f"**RAM:** {ram} - ${prices[ram]}")
        st.write(f"**Storage:** {storage} - ${prices[storage]}")
        st.write(f"**Case:** {case} - ${prices[case]}")

        st.subheader(f"Total Build Cost: ${total:.2f}")

        if purpose == "Gaming":
            st.info("Gaming builds benefit most from a strong GPU.")
        elif purpose == "Office":
            st.info("Office builds usually do not need the most expensive GPU.")
        elif purpose == "Streaming":
            st.info("Streaming builds benefit from stronger CPU, GPU, and RAM choices.")