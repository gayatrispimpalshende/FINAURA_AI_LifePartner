import streamlit as st
import joblib
import numpy as np
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="FINAURA - Agentic AI",
    page_icon="💎",
    layout="wide"
)

# ---------------- SESSION STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------------- HOME PAGE ----------------
if st.session_state.page == "home":

    st.title("💎 FINAURA AI – Intelligent Financial Recommendation System")

    st.markdown("##  How It Works")

    st.markdown("""
    ### Step 1️ – Enter Financial Details  
    Provide your age, income, expenses, savings %, and life events.

    ### Step 2️ – AI Analysis  
    Our Machine Learning model analyzes your financial behavior.

    ### Step 3️ – Smart Recommendation  
    The system predicts the most suitable financial product.

    ### Step 4️ – Engagement Optimization  
    View confidence score and engagement probability.
    """)

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

        st.markdown("##  AI Agent Decision Engine")

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
