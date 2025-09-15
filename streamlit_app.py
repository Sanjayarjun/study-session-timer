import streamlit as st
import time
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("📚 Smart Study Session Timer")

# Sidebar inputs
st.sidebar.header("⏲️ Session Settings")
session_minutes = st.sidebar.number_input("Session Length (minutes)", min_value=1, max_value=180, value=25)
break_minutes = st.sidebar.number_input("Break Length (minutes)", min_value=1, max_value=60, value=5)

# Start button
if st.button("Start Study Session"):
    st.success(f"Started a {session_minutes}-minute study session! Focus now 👨‍💻👩‍💻")

    progress_bar = st.progress(0)
    status_text = st.empty()

    for i in range(session_minutes * 60):
        time.sleep(1)  # waits 1 second
        progress = int((i + 1) / (session_minutes * 60) * 100)
        progress_bar.progress(progress)
        status_text.text(f"Time left: {session_minutes*60 - (i+1)} seconds")

    st.warning(f"⏳ Session complete! Take a {break_minutes}-minute break.")

# Stats placeholder (for future improvements)
st.header("📊 Session Stats (Demo)")
data = {"Session": ["1", "2", "3"], "Minutes Focused": [25, 30, 20]}
df = pd.DataFrame(data)

st.dataframe(df)

fig, ax = plt.subplots()
ax.plot(df["Session"], df["Minutes Focused"], marker="o")
ax.set_title("Focus Over Sessions")
ax.set_xlabel("Session")
ax.set_ylabel("Minutes")
st.pyplot(fig)
