import streamlit as st
import time
import pandas as pd

# Store session data in Streamlit session_state
if "stats" not in st.session_state:
    st.session_state.stats = []

st.title("📚 Smart Study Session Timer")

# --- Session Settings ---
st.sidebar.header("⏲️ Session Settings")
session_minutes = st.sidebar.number_input("Session Length (minutes)", min_value=1, max_value=180, value=25)
break_minutes = st.sidebar.number_input("Break Length (minutes)", min_value=1, max_value=60, value=5)

# --- Timer Logic ---
if st.button("Start Study Session"):
    st.write(f"⏳ Studying for {session_minutes} minutes...")
    progress_bar = st.progress(0)

    for i in range(session_minutes * 60):
        time.sleep(1)  # simulate 1 sec
        progress_bar.progress((i + 1) / (session_minutes * 60))
    
    st.success("✅ Study Session Completed!")

    # Log session
    st.session_state.stats.append({
        "Session Length": session_minutes,
        "Break Length": break_minutes
    })

    st.write(f"☕ Take a {break_minutes}-minute break!")

# --- Stats Section ---
st.header("📊 Session Stats")

if st.session_state.stats:
    df = pd.DataFrame(st.session_state.stats)
    st.bar_chart(df["Session Length"])
    st.dataframe(df)
else:
    st.info("No sessions completed yet. Start your first session!")
