import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Student Study Hours Dashboard",
    page_icon="📚",
    layout="wide"
)

# CUSTOM TITLE
st.title("📚 Student Study Hours Analysis Dashboard")
st.write("Analyze student study hours and academic performance.")
st.divider()

# LOAD CSV FILE
@st.cache_data
def load_data():
    return pd.read_csv("student_data.csv")

data = load_data()

# CHECK REQUIRED COLUMNS
required_columns = ["Study_Hours", "Marks", "Subject"]

if not all(col in data.columns for col in required_columns):
    st.error("CSV file is missing required columns.")
    st.stop()

# SIDEBAR FILTER
st.sidebar.title("Dashboard Filters")

subjects = sorted(data["Subject"].dropna().unique())

selected_subject = st.sidebar.multiselect(
    "Select Subject",
    subjects,
    default=subjects
)

# FILTER DATA
filtered_data = data[
    data["Subject"].isin(selected_subject)
].copy()

if filtered_data.empty:
    st.warning("Please select at least one subject.")
    st.stop()

# SUMMARY CARDS
total_students = len(filtered_data)
average_hours = filtered_data["Study_Hours"].mean()
average_marks = filtered_data["Marks"].mean()

st.subheader("📊 Overall Performance")

col1, col2, col3 = st.columns(3)

col1.metric("Total Records", total_students)
col2.metric("Average Study Hours", f"{average_hours:.2f}")
col3.metric("Average Marks", f"{average_marks:.2f}")

st.divider()

# SUBJECT-WISE ANALYSIS
st.subheader("📖 Subject-Wise Performance")

subject_analysis = filtered_data.groupby("Subject").agg({
    "Study_Hours": "mean",
    "Marks": "mean"
})

col1, col2 = st.columns(2)

# BAR CHART
with col1:
    st.write("Average Marks by Subject")

    fig, ax = plt.subplots(figsize=(7, 4))

    ax.bar(
        subject_analysis.index,
        subject_analysis["Marks"]
    )

    ax.set_xlabel("Subject")
    ax.set_ylabel("Average Marks")
    ax.set_title("Subject-Wise Marks")
    ax.grid(axis="y", alpha=0.3)

    st.pyplot(fig)
    plt.close(fig)

# STUDY HOURS CHART
with col2:
    st.write("Average Study Hours by Subject")

    fig, ax = plt.subplots(figsize=(7, 4))

    ax.bar(
        subject_analysis.index,
        subject_analysis["Study_Hours"]
    )

    ax.set_xlabel("Subject")
    ax.set_ylabel("Average Study Hours")
    ax.set_title("Subject-Wise Study Hours")
    ax.grid(axis="y", alpha=0.3)

    st.pyplot(fig)
    plt.close(fig)

st.divider()

# SCATTER PLOT
st.subheader("📈 Study Hours vs Marks")

fig, ax = plt.subplots(figsize=(9, 5))

ax.scatter(
    filtered_data["Study_Hours"],
    filtered_data["Marks"]
)

ax.set_xlabel("Study Hours")
ax.set_ylabel("Marks")
ax.set_title("Study Hours and Academic Performance")
ax.grid(True, alpha=0.3)

st.pyplot(fig)
plt.close(fig)

st.divider()

# STUDENT DATA TABLE
st.subheader("👨‍🎓 Student Records")

search_text = st.text_input(
    "Search Student Records by Subject"
)

if search_text:
    display_data = filtered_data[
        filtered_data["Subject"].astype(str).str.contains(
            search_text,
            case=False,
            na=False
        )
    ]
else:
    display_data = filtered_data

st.dataframe(
    display_data,
    width="stretch",
    hide_index=True
)

