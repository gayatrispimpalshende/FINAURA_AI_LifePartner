import streamlit as st
import joblib
import numpy as np
import time

# Load model
model = joblib.load("finaura_model.pkl")

st.set_page_config(
    page_title="FINAURA - Agentic AI",
    page_icon="💎",
    layout="wide"
)

st.markdown("""
<h1 style='text-align: center; color: #2E86C1;'>
💎 FINAURA – Agentic AI Financial Life Partner
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h4 style='text-align: center; color: grey;'>
Predictive Behavioral Intelligence for Proactive Banking
</h4>
""", unsafe_allow_html=True)

st.markdown("---")


st.markdown("Reimagining Banking Through Predictive Behavioral Intelligence")

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

st.markdown("""
<style>
div.stButton > button {
    background-color: #2E86C1;
    color: white;
    height: 3em;
    width: 100%;
    border-radius:10px;
}
</style>
""", unsafe_allow_html=True)


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
 
    intelligence_score = round((income / (monthly_expense + 1)) * 10, 2)
    intelligence_score = min(intelligence_score, 100)

    st.markdown("## 🤖 AI Agent Decision Engine")

    col1, col2 = st.columns(2)

    with col1:
        st.success(f"🎯 Recommended Product: **{recommended_product}**")
        st.info(f"🔍 Confidence Score: {round(probability,2)}%")

    with col2:
        st.metric("📊 360° Profile Score", f"{intelligence_score}/100")
        st.progress(int(probability))

    st.markdown("---")

    # ----------------------------
    # Omnichannel Orchestration
    # ----------------------------
    st.subheader("📡 Smart Channel Selection")

    channel = st.selectbox(
        "Choose Engagement Channel",
        ["SMS", "Email", "In-App Notification"]
    )

    if channel == "SMS":
        st.success(f"📱 SMS Sent: Hi! Based on your profile, we recommend {recommended_product}.")
    elif channel == "Email":
        st.success(f"📧 Email Delivered: Exclusive {recommended_product} curated for you!")
    else:
        st.success(f"🔔 In-App Alert: {recommended_product} now available for you.")

    st.markdown("---")

     # ----------------------------
    # Real-Time Optimization
    # ----------------------------
    st.subheader("⚡ Real-Time Optimization Engine")

    engagement_score = int(probability * 0.9)
    st.progress(engagement_score)

    st.write(f"📈 Expected Engagement Rate: {engagement_score}%")

    st.markdown("### 🔐 Privacy & Compliance Layer Active")

    # Reason Generator
    if prediction == 0:
        reason = "High medical spending pattern detected."
    elif prediction == 1:
        reason = "Strong savings behavior identified."
    elif prediction == 2:
        reason = "Spending exceeds income trend."
    else:
        reason = "Balanced financial behavior observed."

    # Message Generator
    message = f"""
    Hi {name} 👋,

    Based on your financial activity, we recommend our {recommended_product}.
    {reason}

    This solution is tailored specifically for your current financial journey.
    """

    # Channel Selector
    if medical_percent > 35:
        channel = "📱 SMS (Urgent Financial Advisory)"
    elif app_active_time == "Night":
        channel = "💬 WhatsApp Message"
    else:
        channel = "📲 In-App Notification"

    st.success(f"🎯 Recommended Product: {recommended_product}")
    st.metric("Confidence Score", f"{probability:.2f}%")

    st.info(f"💡 Reason: {reason}")

    st.markdown("### 💬 Personalized Message")
    st.write(message)

    st.markdown("### 📡 Suggested Communication Channel")
    st.write(channel)
    if "SMS" in channel:
        import time

        st.markdown("### 📲 Live Notification Simulation")

        with st.spinner("Sending SMS Alert..."):
            time.sleep(2)

        st.toast("📩 New SMS Received!")

        st.markdown("""
        <div style='
            background-color:#E8F6F3;
            padding:20px;
            border-radius:15px;
            border-left:6px solid #1ABC9C;
            font-size:16px;
        '>
        📩 <b>New SMS from FINAURA</b><br><br>
        Urgent Advisory: Based on your recent financial activity,
        immediate financial protection is recommended.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 📊 Income vs Expense")
    st.bar_chart({"Income": income, "Expense": monthly_expense})
    
    st.markdown("---")
    st.markdown("""
     <center>
     AI-driven • Context-aware • Proactive Engagement  
     <br>
     © 2026 FINAURA Intelligent Systems
     </center>
     """, unsafe_allow_html=True)
    st.markdown("---")
    st.caption("Developed by Gayatri, chaitani | AI Engineering | 2026")
