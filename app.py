import streamlit as st
import joblib
import numpy as np
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Finaura AI",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown("""
<div style="background-color:#0E1117; padding:40px; border-radius:12px; text-align:center;">
    <h1 style="color:white; font-size:48px; margin-bottom:10px;">Take Control of Your Financial Future with Finaura AI</h1>
    <p style="color:#00C2A8; font-size:20px;">AI-powered insights · Personalized recommendations · Smart engagement strategies</p>
</div>
""", unsafe_allow_html=True)

# Hero image
st.image("/mnt/data/A_homepage_for_Finaura_AI,_an_AI-powered_financial.png", use_column_width=True)

st.markdown("""
<style>
/* ---------- Global ---------- */

/* Main background */
body, .stApp {
    background-color: #0E1117;
    color: #E0E0E0;
    font-family: 'Arial', sans-serif;
}

/* Headings */
h1, h2, h3, h4 {
    color: #00C2A8;
    font-weight: 700;
}

/* ---------- Inputs ---------- */

/* Change input label colors */
div[data-testid="stTextInput"] label, 
div[data-testid="stNumberInput"] label,
div[data-testid="stSlider"] label,
div[data-testid="stSelectbox"] label {
    color: #00C2A8;
    font-weight: 600;
    font-size: 16px;
}

/* Style input boxes / sliders */
div[data-testid="stTextInput"] input,
div[data-testid="stNumberInput"] input,
div[data-testid="stSlider"] input {
    background-color: #1F2937;
    color: #E0E0E0;
    border-radius: 8px;
    padding: 5px;
}

/* Selectbox dropdown text */
div[data-testid="stSelectbox"] div[role="combobox"] {
    color: #E0E0E0;
    background-color: #1F2937;
}

/* ---------- Buttons ---------- */
.stButton>button {
    background-color: #00C2A8;
    color: white;
    border-radius: 12px;
    height: 3em;
    font-weight: 600;
    font-size: 16px;
    transition: transform 0.2s, box-shadow 0.2s;
}
.stButton>button:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(0, 194, 168, 0.5);
}

/* ---------- Metric Cards ---------- */
[data-testid="metric-container"] {
    background-color: #1F2937;
    padding: 15px;
    border-radius: 12px;
}

/* ---------- Feature / Info Cards ---------- */
.card, .feature-card {
    background-color: #1F2937;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 20px;
    border: 1px solid #333;
    text-align: center;
    transition: transform 0.3s, box-shadow 0.3s;
}
.card:hover, .feature-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 20px rgba(0, 194, 168, 0.5);
}
.card h3, .feature-card h3 {
    color: #00C2A8;
    margin-top: 10px;
}
.card p, .feature-card p {
    color: #E0E0E0;
    font-size: 16px;
}
.card img, .feature-card img {
    width: 80px;
    height: 80px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)
st.subheader("What Finaura AI Can Do")

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown(f"""
    <div class="feature-card">
        <img src="https://img.icons8.com/ios-filled/100/00C2A8/brain.png"/>
        <h3>Smart Analysis</h3>
        <p>Analyze your financial behavior instantly and get insights tailored to you.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="feature-card">
        <img src="https://img.icons8.com/ios-filled/100/00C2A8/pie-chart.png"/>
        <h3>Personalized Recommendation</h3>
        <p>Receive the most suitable financial products based on your unique profile.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="feature-card">
        <img src="https://img.icons8.com/ios-filled/100/00C2A8/analytics.png"/>
        <h3>Engagement Optimization</h3>
        <p>Understand the best channels and timing to maximize your financial engagement.</p>
    </div>
    """, unsafe_allow_html=True)
st.subheader("How It Works")
col1, col2, col3, col4 = st.columns(4, gap="medium")

col1.markdown("""
<div style="text-align:center;">
<img src="https://img.icons8.com/ios-filled/80/00C2A8/user.png"/>
<br><b>Enter Details</b>
<br>Provide age, income, expenses, and life events
</div>
""", unsafe_allow_html=True)

col2.markdown("""
<div style="text-align:center;">
<img src="https://img.icons8.com/ios-filled/80/00C2A8/artificial-intelligence.png"/>
<br><b>AI Analysis</b>
<br>Predict financial behavior using ML model
</div>
""", unsafe_allow_html=True)

col3.markdown("""
<div style="text-align:center;">
<img src="https://img.icons8.com/ios-filled/80/00C2A8/money.png"/>
<br><b>Get Recommendation</b>
<br>Receive the perfect financial product
</div>
""", unsafe_allow_html=True)

col4.markdown("""
<div style="text-align:center;">
<img src="https://img.icons8.com/ios-filled/80/00C2A8/graph.png"/>
<br><b>Optimize Engagement</b>
<br>Maximize returns and engagement
</div>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------------- HOME PAGE ----------------
if st.session_state.page == "home":
    st.title("💎 FINAURA AI – Your Smart Financial Companion")
    st.markdown("**Get AI-powered personalized financial recommendations instantly!**")

    st.image("https://images.unsplash.com/photo-1605902711622-cfb43c443f1c?auto=format&fit=crop&w=1000&q=80", use_column_width=True)

if st.button("🔍 Start Your Analysis Now"):
    st.session_state.page = "main"
    st.rerun()

    if st.button("🔍 Start Analysis"):
        st.session_state.page = "main"
        st.rerun()

# ---------------- MAIN APP ----------------
elif st.session_state.page == "main":

    # Load model
    try:
        model = joblib.load("finaura_model.pkl")
    except:
        st.error("Error: Model file not found or failed to load.")
        st.stop()

    st.markdown("""
    <h1 style='text-align: center; color: #2E86C1;'>
    💎 FINAURA – Agentic AI Financial Life Partner
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Reimagining Banking Through Predictive Behavioral Intelligence")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Customer Name")
        age = st.slider("Age", 22, 60)
        income = st.number_input("Monthly Income", 20000, 200000)
        monthly_expense = st.number_input("Monthly Expense", 10000, 200000)
        medical_percent = st.slider("Medical Expense %", 0, 60)
        savings_percent = st.slider("Savings %", 0, 60)

    with col2:
        life_event = st.selectbox("Life Event",
                                  ["None", "Marriage", "Baby", "Job Change"])
        app_active_time = st.selectbox("App Active Time",
                                       ["Morning", "Night"])

    life_event_map = {"None": 0, "Marriage": 1, "Baby": 2, "Job Change": 3}
    app_time_map = {"Morning": 0, "Night": 1}

    if st.button("🔍 Analyze Financial Profile"):

        input_data = np.array([[age, income, monthly_expense,
                                medical_percent, savings_percent,
                                life_event_map[life_event],
                                app_time_map[app_active_time]]])

        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data).max() * 100

        product_map = {
            0: "Insurance Plan",
            1: "Investment Plan",
            2: "Personal Loan",
            3: "Smart Savings Plan"
        }

        recommended_product = product_map.get(prediction, "Smart Financial Plan")

        intelligence_score = min(round((income / (monthly_expense + 1)) * 10, 2), 100)
        st.markdown("<div class='card'><h3>AI Agent Decision Engine</h3></div>", unsafe_allow_html=True)

        colA, colB = st.columns(2)

        with colA:
            st.success(f"🎯 Recommended Product: **{recommended_product}**")
            st.info(f"🔍 Confidence Score: {round(probability, 2)}%")

        with colB:
            st.metric("📊 360° Profile Score", f"{intelligence_score}/100")
            st.progress(int(probability))

        st.markdown("---")

        # ---------------- Channel Selection ----------------
        st.subheader("📡 Smart Channel Selection")

        channel_choice = st.selectbox(
            "Choose Engagement Channel",
            ["SMS", "Email", "In-App Notification"]
        )

        if channel_choice == "SMS":
            st.success(f"📱 SMS Sent: Hi! Based on your profile, we recommend {recommended_product}.")
        elif channel_choice == "Email":
            st.success(f"📧 Email Delivered: Exclusive {recommended_product} curated for you!")
        else:
            st.success(f"🔔 In-App Alert: {recommended_product} now available for you.")

        st.markdown("---")

        # ---------------- Real-Time Optimization ----------------
        st.subheader(" Real-Time Optimization Engine")

        engagement_score = int(probability * 0.9)
        st.progress(engagement_score)
        st.write(f"📈 Expected Engagement Rate: {engagement_score}%")

        st.markdown("###  Privacy & Compliance Layer Active")

        # ---------------- Reason Generator ----------------
        if prediction == 0:
            reason = "High medical spending pattern detected."
        elif prediction == 1:
            reason = "Strong savings behavior identified."
        elif prediction == 2:
            reason = "Spending exceeds income trend."
        else:
            reason = "Balanced financial behavior observed."

        message = f"""
        Hi {name} ,

        Based on your financial activity, we recommend our {recommended_product}.  
        {reason}

        This solution is tailored specifically for your current financial journey.
        """

        st.markdown("### 💬 Personalized Message")
        st.write(message)

        st.markdown("### Income vs Expense")
        st.bar_chart({"Income": income, "Expense": monthly_expense})

        st.markdown("---")
        st.caption("Developed by Gayatri & Chaitani | AI Engineering | 2026")
