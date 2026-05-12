import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Academic Improvement Journey Dashboard",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('academic_journey_dataset.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_data()

# Custom CSS for better styling
st.markdown("""
    <style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .section-header {
        font-size: 24px;
        font-weight: bold;
        margin-top: 30px;
        margin-bottom: 15px;
        border-bottom: 3px solid #1f77b4;
        padding-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar filters
st.sidebar.title("🔍 Filters")
selected_semester = st.sidebar.multiselect(
    "Select Semester(s)",
    options=df['Semester'].unique(),
    default=df['Semester'].unique()
)

selected_status = st.sidebar.multiselect(
    "Exam Status",
    options=['Midterm', 'Final', 'None'],
    default=['Midterm', 'Final', 'None']
)

# Filter data
filtered_df = df[
    (df['Semester'].isin(selected_semester)) &
    (df['Exam_Status'].fillna('None').isin(selected_status))
]

# ============================================================================
# 1. STORY OVERVIEW
# ============================================================================
st.markdown("# 📚 Academic Improvement Journey Dashboard")
st.markdown("## Story Overview")

story_text = """
This dashboard chronicles my academic journey as a student at Parami University, 
tracking how I've balanced coursework, internship responsibilities, and civic engagement 
while managing stress and optimizing my academic performance.

**The Challenge:** This semester, I'm taking **5 courses** (compared to 3 last semester) 
while working on a **fraud detection analysis internship** and contributing to the **SDS Bridge Program** 
for civic engagement. This increased workload has significantly impacted my sleep patterns and stress levels, 
especially during midterm and final exam periods.

**The Goal:** Understand what habits and strategies improve my academic performance and 
how to better manage my time and stress across multiple commitments.
"""

st.markdown(story_text)

# ============================================================================
# 2. KEY METRICS
# ============================================================================
st.markdown('<div class="section-header">📊 Key Metrics</div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    avg_study = filtered_df['Study_Hours'].mean()
    st.metric("Avg Study Hours", f"{avg_study:.1f} hrs", "per day")

with col2:
    avg_sleep = filtered_df['Sleep_Hours'].mean()
    st.metric("Avg Sleep Hours", f"{avg_sleep:.1f} hrs", "per day")

with col3:
    avg_stress = filtered_df['Stress_Level'].mean()
    st.metric("Avg Stress Level", f"{avg_stress:.1f}/5", "self-rated")

with col4:
    avg_productivity = filtered_df['Productivity_Level'].mean()
    st.metric("Avg Productivity", f"{avg_productivity:.1f}/5", "self-rated")

# ============================================================================
# 3. DATA VISUALIZATIONS
# ============================================================================
st.markdown('<div class="section-header">📈 Data Visualizations</div>', unsafe_allow_html=True)

# Visualization 1: Study Hours vs Sleep Hours Over Time
st.subheader("1️⃣ Study Hours vs Sleep Hours Over Time")
fig1 = go.Figure()
fig1.add_trace(go.Scatter(
    x=filtered_df['Date'], y=filtered_df['Study_Hours'],
    mode='lines+markers', name='Study Hours',
    line=dict(color='#1f77b4', width=3),
    marker=dict(size=8)
))
fig1.add_trace(go.Scatter(
    x=filtered_df['Date'], y=filtered_df['Sleep_Hours'],
    mode='lines+markers', name='Sleep Hours',
    line=dict(color='#ff7f0e', width=3),
    marker=dict(size=8)
))
fig1.update_layout(
    title="Study vs Sleep Hours Over Time",
    xaxis_title="Date",
    yaxis_title="Hours",
    hovermode='x unified',
    height=400,
    template='plotly_white'
)
st.plotly_chart(fig1, use_container_width=True)

# Visualization 2: Stress Level vs Productivity Level
st.subheader("2️⃣ Stress Level vs Productivity Level")
fig2 = px.scatter(
    filtered_df,
    x='Stress_Level', y='Productivity_Level',
    color='Semester',
    size='Course_Load',
    hover_data=['Date', 'Study_Hours', 'Sleep_Hours'],
    title="Stress vs Productivity (bubble size = course load)",
    labels={'Stress_Level': 'Stress Level (1-5)', 'Productivity_Level': 'Productivity Level (1-5)'},
    height=400
)
fig2.update_layout(template='plotly_white')
st.plotly_chart(fig2, use_container_width=True)

# Visualization 3: Assignment Scores Trend
st.subheader("3️⃣ Assignment Scores Trend")
scores_df = filtered_df.dropna(subset=['Assignment_Score'])
fig3 = go.Figure()
fig3.add_trace(go.Scatter(
    x=scores_df['Date'], y=scores_df['Assignment_Score'],
    mode='lines+markers', name='Assignment Score',
    line=dict(color='#2ca02c', width=3),
    marker=dict(size=10),
    fill='tozeroy'
))
fig3.update_layout(
    title="Assignment Scores Trend",
    xaxis_title="Date",
    yaxis_title="Score",
    hovermode='x unified',
    height=400,
    template='plotly_white'
)
st.plotly_chart(fig3, use_container_width=True)

# Visualization 4: Weekday vs Weekend Study Patterns
st.subheader("4️⃣ Study Hours: Weekday vs Weekend")
weekend_data = filtered_df.groupby('Is_Weekend')['Study_Hours'].apply(list).to_dict()
fig4 = go.Figure()
fig4.add_trace(go.Box(y=weekend_data[False], name='Weekday', marker_color='#1f77b4'))
fig4.add_trace(go.Box(y=weekend_data[True], name='Weekend', marker_color='#ff7f0e'))
fig4.update_layout(
    title="Study Hours Distribution: Weekday vs Weekend",
    yaxis_title="Study Hours",
    height=400,
    template='plotly_white'
)
st.plotly_chart(fig4, use_container_width=True)

# ============================================================================
# 4. KEY INSIGHTS
# ============================================================================
st.markdown('<div class="section-header">🔍 Key Insights</div>', unsafe_allow_html=True)

insights = [
    {
        "title": "📉 Inverse Sleep-Study Relationship",
        "description": "During midterm and final exam periods, my study hours increase dramatically (8-12 hours) while sleep hours decrease (5-7 hours). This inverse relationship shows the trade-off I make during high-pressure periods."
    },
    {
        "title": "🚀 Productivity Peaks During Finals",
        "description": "My productivity level reaches its maximum (5/5) during final exam periods, despite the highest stress levels (5/5). This suggests that deadline pressure actually enhances my focus and output."
    },
    {
        "title": "📱 Weekend Social Media Impact",
        "description": "On weekends, my study hours drop to 2 hours due to social media scrolling (YouTube Reels, Instagram Reels). However, during finals, weekend study hours increase to 8-10 hours, showing I can override this habit when motivated."
    },
    {
        "title": "📚 5-Course Load Effect",
        "description": "Taking 5 courses this semester (vs. 3 last semester) has increased my average stress level and reduced sleep hours. However, my assignment scores remain high (88-95), indicating effective time management despite increased workload."
    },
    {
        "title": "📈 Exam Performance Pattern",
        "description": "Assignment scores are highest at the beginning of the semester (85) and during finals (90-95), but dip during midterms (70-75). This suggests I need better preparation strategies for midterm exams."
    }
]

for i, insight in enumerate(insights, 1):
    with st.container():
        st.markdown(f"### {insight['title']}")
        st.markdown(insight['description'])
        st.divider()

# ============================================================================
# 5. DECISION-MAKING SECTION
# ============================================================================
st.markdown('<div class="section-header">🎯 Decision-Making: What Should I Do Differently?</div>', unsafe_allow_html=True)

decisions = [
    {
        "title": "1. Prioritize Sleep During Exam Periods",
        "action": "Maintain at least 7-8 hours of sleep even during finals",
        "rationale": "Data shows that while I can work 10+ hours with 5-6 hours sleep, my cognitive performance likely suffers. Research suggests 7-8 hours is optimal for memory retention and exam performance.",
        "limitation": "This may require reducing study hours or delegating some tasks, which could impact short-term grades but improve long-term retention."
    },
    {
        "title": "2. Implement Midterm Preparation Strategy",
        "action": "Start studying for midterms 2 weeks in advance instead of 1 week",
        "rationale": "My midterm scores (70-75) are lower than finals (90-95). Earlier preparation could improve these scores.",
        "limitation": "This requires better time management across all courses and may not be feasible with 5 concurrent courses."
    },
    {
        "title": "3. Reduce Weekend Social Media Time",
        "action": "Limit social media to 1-2 hours on weekends, especially before midterms",
        "rationale": "I currently spend most weekends scrolling (2 hours study vs. 6+ hours free time). Redirecting even 2-3 hours to studying could improve preparation.",
        "limitation": "This is a habit-breaking challenge and requires strong self-discipline."
    },
    {
        "title": "4. Optimize Internship-Study Balance",
        "action": "Schedule internship work during low-stress periods (weeks 1-7 of semester)",
        "rationale": "The internship adds to my workload. Concentrating it early allows more focus on academics during midterms and finals.",
        "limitation": "Internship schedule may not be flexible, and this could impact the quality of my internship work."
    },
    {
        "title": "5. Leverage Peak Productivity Hours",
        "action": "Schedule most challenging coursework during my peak productivity times (finals period strategies)",
        "rationale": "My productivity is highest during finals (5/5). Understanding what drives this (deadline pressure, focused environment) could help me replicate it earlier.",
        "limitation": "Artificially creating pressure might not be sustainable or healthy long-term."
    }
]

for decision in decisions:
    with st.expander(f"**{decision['title']}**"):
        st.markdown(f"**Action:** {decision['action']}")
        st.markdown(f"**Rationale:** {decision['rationale']}")
        st.markdown(f"**Limitation:** {decision['limitation']}")

# ============================================================================
# 6. ETHICS & RESPONSIBILITY SECTION
# ============================================================================
st.markdown('<div class="section-header">⚖️ Ethics & Responsibility</div>', unsafe_allow_html=True)

# Privacy Statement
with st.expander("🔒 Privacy Statement"):
    st.markdown("""
    **Data Included:**
    - Study hours per day
    - Sleep hours per day
    - Assignment scores
    - Self-rated stress levels (1-5)
    - Self-rated productivity levels (1-5)
    - Exam results (Midterm/Final)
    - Course load per semester
    
    **Data Anonymized:**
    - No real names are used (only "Student" or generic references)
    - Internship name is not disclosed (only described as "fraud detection analysis")
    - Specific course names are anonymized (only course codes are referenced)
    - No personal contact information or identifiers are included
    - Civic engagement project is referenced generically as "SDS Bridge Program"
    
    **Data Source:**
    - All data is self-reported and synthetic, created for educational purposes
    - No third-party data is included
    """)

# Bias & Limitation Disclosure
with st.expander("⚠️ Bias & Limitation Disclosure"):
    st.markdown("""
    **Memory Bias:**
    - Self-reported data (stress, productivity) is subject to recall bias
    - Stress levels are subjective and may not reflect actual physiological stress
    - I may unconsciously report higher productivity during finals due to outcome bias
    
    **Small Dataset:**
    - Only ~25 data points across 2 semesters
    - Limited sample size reduces statistical significance of correlations
    - Patterns observed may not generalize to future semesters
    
    **Subjective Scoring:**
    - Stress levels (1-5) and productivity levels (1-5) are self-rated
    - No objective measurement tools (e.g., cortisol levels, time-tracking software)
    - Scoring criteria may have shifted over time
    
    **Confounding Variables:**
    - Course difficulty varies across semesters (not controlled for)
    - Internship workload changes are not quantified
    - External factors (health, personal events) are not tracked
    
    **Causation vs. Correlation:**
    - Observed patterns (e.g., high stress → high productivity) may be correlational, not causal
    - Reverse causation is possible (high productivity might reduce stress, not vice versa)
    """)

# Visualization Justification
with st.expander("📊 Visualization Justification"):
    st.markdown("""
    **1. Study vs Sleep Hours (Line Chart)**
    - **Why:** Line charts are ideal for showing trends over time
    - **Risk:** The inverse relationship might suggest causation when it's just correlation
    - **Mitigation:** Labeled as "Over Time" to emphasize temporal relationship, not causation
    
    **2. Stress vs Productivity (Scatter Plot)**
    - **Why:** Scatter plots reveal relationships between two variables
    - **Risk:** Bubble size (course load) adds a third dimension, which can be confusing
    - **Mitigation:** Hover tooltips provide additional context; color distinguishes semesters
    
    **3. Assignment Scores (Line Chart with Fill)**
    - **Why:** Shows trend and magnitude of scores over time
    - **Risk:** Fill area might exaggerate the importance of score changes
    - **Mitigation:** Y-axis starts at 0 to show true proportions
    
    **4. Weekday vs Weekend (Box Plot)**
    - **Why:** Box plots show distribution and outliers clearly
    - **Risk:** Small sample size (only 3 weekend days per semester) limits reliability
    - **Mitigation:** Hover data shows actual values; interpretation acknowledges small sample
    """)

# Responsible Decision
with st.expander("🎯 Responsible Decision"):
    st.markdown("""
    **Limitations of My Decisions:**
    
    1. **Sleep Reduction Trade-off:**
       - While I can function on 5-6 hours during finals, this may harm long-term health
       - Chronic sleep deprivation could impact future semesters
       - Decision should be temporary (finals only), not permanent
    
    2. **Midterm Strategy:**
       - Assumes earlier preparation = better scores (not always true)
       - May increase overall stress if implemented poorly
       - Requires testing and validation before full commitment
    
    3. **Social Media Reduction:**
       - Assumes social media time is "wasted" (ignores mental health benefits)
       - May not be feasible if social media is part of my social connections
       - Should be balanced with mental health needs
    
    4. **Internship Scheduling:**
       - May not be within my control (employer may set schedule)
       - Concentrating internship work early might reduce learning opportunities
       - Could impact internship performance if rushed
    
    5. **Artificial Pressure:**
       - Creating artificial deadlines might not replicate finals-period focus
       - Could increase anxiety without improving performance
       - Needs careful implementation to avoid burnout
    
    **Ethical Commitment:**
    - These decisions are recommendations, not prescriptions
    - Implementation should be gradual and monitored
    - Health and well-being take priority over grades
    - Regular reassessment is needed to ensure strategies are working
    """)

# Footer
st.divider()
st.markdown("""
---
**Dashboard Created:** May 2026 | **Data Period:** September 2025 - May 2026
**For:** Data201 - Data Communication and Ethics Final Project
**Student:** Hein, Min Thant | **Institution:** Parami University
""")
