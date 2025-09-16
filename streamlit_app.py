import streamlit as st
import time
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import base64

# ---- Helper function for beep ----
def beep_sound():
    # Simple beep in .wav format (encoded)
    beep_wav = (
        b"UklGRiQAAABXQVZFZm10IBAAAAABAAEAESsAACJWAAACABAAZGF0YQgAAAAA"
        b"//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA"
    )
    b64 = base64.b64encode(beep_wav).decode("utf-8")
    st.audio(f"data:audio/wav;base64,{b64}", format="audio/wav")

# ---- SESSION STATE ----
if "logs" not in st.session_state:
    st.session_state.logs = []

# ---- APP TITLE ----
st.title("📚 Smart Study Session Timer with Focus Stats")

# ---- SIDEBAR SETTINGS ----
st.sidebar.header("⏲️ Session Settings")
session_length = st.sidebar.number_input("Session Length (minutes)", min_value=1, value=25)
break_length = st.sidebar.number_input("Break Length (minutes)", min_value=1, value=5)

# ---- START SESSION ----
if st.button("▶️ Start Study Session"):
    st.success(f"Study session started for {session_length} minutes!")
    start_time = datetime.now()

    countdown_placeholder = st.empty()

    # ---- Study Countdown ----
    total_seconds = session_length * 60
    for remaining in range(total_seconds, 0, -1):
        mins, secs = divmod(remaining, 60)
        countdown_placeholder.metric("📖 Study Time Remaining", f"{mins:02}:{secs:02}")
        time.sleep(1)

    st.success("✅ Study Session Completed! Time for a break.")
    beep_sound()
    end_time = datetime.now()

    # ---- Break Countdown ----
    break_placeholder = st.empty()
    break_seconds = break_length * 60
    for remaining in range(break_seconds, 0, -1):
        mins, secs = divmod(remaining, 60)
        break_placeholder.metric("☕ Break Time Remaining", f"{mins:02}:{secs:02}")
        time.sleep(1)

    st.success("🎉 Break Over! Ready for your next session?")
    beep_sound()

    # Log session
    st.session_state.logs.append({
        "date": start_time.date(),
        "start": start_time,
        "end": end_time,
        "duration": session_length,
        "break": break_length
    })

# ---- SHOW LOGS ----
if st.session_state.logs:
    df = pd.DataFrame(st.session_state.logs)

    st.subheader("📊 Session History")
    st.dataframe(df[["date", "duration", "break"]])

    # ---- LINE CHART ----
    st.subheader("📈 Study Progress Over Time")
    fig, ax = plt.subplots()
    ax.plot(df["date"], df["duration"], marker="o", linestyle="-", color="blue", label="Study Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Minutes")
    ax.legend()
    st.pyplot(fig)

    # ---- PIE CHART ----
    st.subheader("🥧 Focus vs Break Ratio")
    total_study = df["duration"].sum()
    total_break = df["break"].sum()
    fig2, ax2 = plt.subplots()
    ax2.pie([total_study, total_break], labels=["Study", "Break"], autopct="%1.1f%%", colors=["#4CAF50", "#FF6347"])
    st.pyplot(fig2)

    # ---- DAILY TOTAL ----
    today = datetime.now().date()
    today_total = df[df["date"] == today]["duration"].sum()
    st.subheader("📅 Today's Study Time")
    st.info(f"⏳ You studied **{today_total} minutes** today!")

    # ---- MOTIVATION ----
    if today_total >= 60:
        st.success("🔥 Amazing! You studied more than 1 hour today. Keep it up!")
    elif today_total > 0:
        st.warning("👏 Good start! Try to reach 1 hour for today.")
    else:
        st.error("😴 No study logged yet today. Let's get started!")
else:
    st.info("No sessions logged yet. Start your first study session!")
