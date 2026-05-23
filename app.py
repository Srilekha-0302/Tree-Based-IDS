import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Tree-Based IDS",
    page_icon="🛡️",
    layout="wide"
)

# ---------------------------------------------------
# MODERN LIGHT BLUE THEME
# ---------------------------------------------------

st.markdown("""
<style>

/* MAIN BACKGROUND */

.stApp {
    background: linear-gradient(
        to bottom,
        #ffffff,
        #90D5FF
    );
}

/* REMOVE DARK HEADER */

header {
    background: rgba(0,0,0,0) !important;
}

/* HEADINGS */

h1 {
    color: #0b3c5d;
    font-weight: 800;
}

h2, h3 {
    color: #0b3c5d;
    font-weight: 700;
}

/* NORMAL TEXT */

p, div, label, span {
    color: black;
}

/* INFO BOX */

[data-testid="stAlert"] {
    background-color: rgba(255,255,255,0.65);
    border: none;
    border-radius: 16px;
    color: black;
}

/* METRIC CARDS */

[data-testid="metric-container"] {
    background-color: rgba(255,255,255,0.75);
    border: none;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
}

/* DATAFRAME */

div[data-testid="stDataFrame"] {
    background-color: rgba(255,255,255,0.15);
    border-radius: 18px;
    padding: 12px;
    border: 2px solid rgba(0,0,0,0.15);
    box-shadow: 0px 4px 12px rgba(0,0,0,0.04);
    backdrop-filter: blur(6px);
}

/* TABLE TEXT */

div[data-testid="stDataFrame"] table {
    color: black !important;
}

/* HEADER */

div[data-testid="stDataFrame"] th {
    background-color: rgba(255,255,255,0.35) !important;
    color: black !important;
    font-weight: 700 !important;
}

/* CELLS */

div[data-testid="stDataFrame"] td {
    background-color: rgba(255,255,255,0.05) !important;
    color: black !important;
}


/* FILE UPLOADER */

[data-testid="stFileUploader"] {
    background-color: rgba(255,255,255,0.75);
    border-radius: 18px;
    padding: 14px;
    border: 2px dashed #90D5FF;
}

/* BROWSE FILES BUTTON */

[data-testid="stFileUploader"] button {
    background-color: white !important;
    color: #0b3c5d !important;
    border-radius: 10px !important;
    border: 1px solid #90D5FF !important;
    font-weight: 600 !important;
}

/* BUTTON HOVER */

[data-testid="stFileUploader"] button:hover {
    background-color: #eaf6ff !important;
    color: #0b3c5d !important;
}

/* DOWNLOAD BUTTON */

.stDownloadButton button {
    background-color: #4da6ff;
    color: white;
    border-radius: 12px;
    border: none;
    padding: 10px 20px;
    font-weight: 600;
}

.stDownloadButton button:hover {
    background-color: #3399ff;
    color: white;
}

/* HORIZONTAL LINE */

hr {
    border-color: rgba(255,255,255,0.4);
}

/* DATAFRAME TOOLBAR ICONS */

[data-testid="stElementToolbar"] svg {
    fill: white !important;
    color: white !important;
}

/* TOOLBAR BUTTONS */

[data-testid="stElementToolbar"] button {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# LOAD MODEL + FILES
# ---------------------------------------------------

model = joblib.load(
    "models\\phase2\\phase2_xgboost_model.pkl"
)

selected_features = joblib.load(
    "models\\selected_features.pkl"
)

label_mapping = joblib.load(
    "models\\label_mapping.pkl"
)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title("🛡️ Tree-Based Intrusion Detection System")

st.markdown("""
## Real-Time Cyber Attack Detection Dashboard

This application analyzes network traffic and predicts malicious activity using a trained XGBoost-based Intrusion Detection System built on the CICIDS2017 dataset.
""")

st.info(
    "Upload a CSV file to analyze network traffic and detect malicious activity."
)

# ---------------------------------------------------
# FILE UPLOAD
# ---------------------------------------------------

uploaded_file = st.file_uploader(
    "📂 Upload Your Network Traffic CSV",
    type=["csv"]
)

# ---------------------------------------------------
# IF FILE UPLOADED
# ---------------------------------------------------

if uploaded_file is not None:

    # Read CSV
    df = pd.read_csv(uploaded_file)

    # Drop Label column if present
    if "Label" in df.columns:
        df = df.drop("Label", axis=1)

    # ---------------------------------------------------
    # SHOW DATASET
    # ---------------------------------------------------

    st.subheader("📄 Uploaded Dataset")

    st.dataframe(df.head())

    # ---------------------------------------------------
    # FEATURE SELECTION
    # ---------------------------------------------------

    try:
        X = df[selected_features]

    except Exception as e:
        st.error(f"Feature mismatch: {e}")
        st.stop()

    # ---------------------------------------------------
    # PREDICTIONS
    # ---------------------------------------------------

    predictions = model.predict(X)

    prediction_probabilities = model.predict_proba(X)

    confidence_scores = np.max(
        prediction_probabilities,
        axis=1
    )

    # Convert labels
    predicted_labels = [
        label_mapping[p]
        for p in predictions
    ]

    # ---------------------------------------------------
    # ADD RESULTS
    # ---------------------------------------------------

    df["Prediction"] = predicted_labels

    df["Confidence (%)"] = (
        confidence_scores * 100
    ).round(2)

    # ---------------------------------------------------
    # DASHBOARD METRICS
    # ---------------------------------------------------

    total_traffic = len(df)

    benign_count = (
        df["Prediction"] == "BENIGN"
    ).sum()

    malicious_count = (
        total_traffic - benign_count
    )

    most_common_attack = (
        df["Prediction"]
        .value_counts()
        .idxmax()
    )

    # ---------------------------------------------------
    # DASHBOARD
    # ---------------------------------------------------

    st.subheader("📊 Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Traffic",
        total_traffic
    )

    col2.metric(
        "Benign",
        benign_count
    )

    col3.metric(
        "Malicious",
        malicious_count
    )

    col4.metric(
        "Most Common Attack",
        most_common_attack
    )

    st.markdown("---")

    # ---------------------------------------------------
    # ATTACK COUNTS
    # ---------------------------------------------------

    prediction_counts = (
        df["Prediction"]
        .value_counts()
        .reset_index()
    )

    prediction_counts.columns = [
        "Attack Type",
        "Count"
    ]

    # ---------------------------------------------------
    # PIE CHART
    # ---------------------------------------------------

    pie_chart = px.pie(
        prediction_counts,
        names="Attack Type",
        values="Count",
        title="Attack Distribution",
        hole=0.45,
        color_discrete_sequence=px.colors.qualitative.Pastel
    )

    pie_chart.update_layout(
        paper_bgcolor="rgba(255,255,255,0.75)",
        plot_bgcolor="rgba(255,255,255,0.75)",
        font=dict(
            color="black",
            size=14
        ),
        legend=dict(
            font=dict(
                color="black",
                size=12
            )
        ),
        title_font=dict(
            color="black",
            size=20
        )
    )

    # ---------------------------------------------------
    # BAR GRAPH
    # ---------------------------------------------------

    bar_chart = px.bar(
        prediction_counts,
        x="Attack Type",
        y="Count",
        title="Attack Counts",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )

    bar_chart.update_layout(
        paper_bgcolor="rgba(255,255,255,0.75)",
        plot_bgcolor="rgba(255,255,255,0.75)",
        font=dict(
            color="black",
            size=14
        ),
        legend=dict(
            font=dict(
                color="black",
                size=12
            )
        ),
        title_font=dict(
            color="black",
            size=20
        ),
        xaxis=dict(
            tickfont=dict(color="black")
        ),
        yaxis=dict(
            tickfont=dict(color="black")
        )
    )

    # ---------------------------------------------------
    # SHOW CHARTS
    # ---------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(
            pie_chart,
            use_container_width=True
        )

    with col2:
        st.plotly_chart(
            bar_chart,
            use_container_width=True
        )

    st.markdown("---")

    # ---------------------------------------------------
    # RESULTS TABLE
    # ---------------------------------------------------

    st.subheader("🔍 Prediction Results")

    st.dataframe(df.head(50))

    # ---------------------------------------------------
    # DOWNLOAD RESULTS
    # ---------------------------------------------------

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Results CSV",
        data=csv,
        file_name="prediction_results.csv",
        mime="text/csv"
    )

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("---")

st.markdown("""
<center>
Built using Streamlit, XGBoost, and Ensemble Learning
</center>
""", unsafe_allow_html=True)