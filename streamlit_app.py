import streamlit as st
import time
import matplotlib.pyplot as plt

st.title("📚 Smart Study Session Timer with Focus Stats")

# Input session length
minutes = st.number_input("Enter study session length (minutes):", min_value=1, max_value=180, value=25)
seconds = minutes * 60

if st.button("Start Session"):
    st.write("Session started... Stay focused!")
    progress_bar = st.progress(0)

    for i in range(seconds):
        time.sleep(0.1)  # reduce speed for testing
        progress_bar.progress(int((i + 1) / seconds * 100))
    st.success("🎉 Session Complete!")

# Simple focus stats chart
st.subheader("📊 Focus Stats Example")
focus_data = [20, 25, 30, 15, 40]
sessions = ["Mon", "Tue", "Wed", "Thu", "Fri"]

fig, ax = plt.subplots()
ax.plot(sessions, focus_data, marker="o")
ax.set_title("Focus Time Across Sessions")
ax.set_ylabel("Minutes")
st.pyplot(fig)
