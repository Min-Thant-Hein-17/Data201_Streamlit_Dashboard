import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Academic Improvement Journey Dashboard",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .insight-box {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #ff7f0e;
        margin: 1rem 0;
    }
    .ethics-box {
        background-color: #d1ecf1;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #17a2b8;
        margin: 1rem 0;
    }
    .warning-box {
        background-color: #f8d7da;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #dc3545;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('academic_journey_dataset.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_data()

# Sidebar navigation
st.sidebar.title("📚 Academic Journey Dashboard")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigate to:",
    ["📖 Story Overview", 
     "📊 Data Visualizations", 
     "🎯 Decision-Making",
     "⚖️ Ethics & Responsibility",
     "🔍 Data Explorer"]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "This dashboard analyzes academic performance patterns across two semesters "
    "with 5 courses, an internship, and civic engagement commitments."
)

# ============================================================================
# PAGE 1: STORY OVERVIEW
# ============================================================================
if page == "📖 Story Overview":
    st.title("📖 My Academic Improvement Journey")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ## The Challenge
        
        This semester, I took on significantly more responsibilities than ever before:
        - **5 courses** (compared to 3 last semester)
        - **Internship** at a tech company working on fraud detection analysis dashboard
        - **Civic engagement project** - SDS Bridge Program
        
        This created unprecedented time pressure and stress, but also an opportunity to understand 
        my academic patterns and optimize my performance.
        """)
    
    with col2:
        st.metric("Courses This Semester", "5", "+2 from last semester")
        st.metric("GPA Improvement", "3.57", "+0.26 from 3.31")
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### Why This Matters
        
        Understanding my academic patterns helps me:
        - Identify what actually improves my grades
        - Optimize time management
        - Maintain health while performing well
        - Make data-driven decisions about future commitments
        """)
    
    with col2:
        st.markdown("""
        ### The Data
        
        I tracked:
        - Study hours per day
        - Sleep hours per day
        - Stress levels (1-5 scale)
        - Productivity (1-5 scale)
        - Assignment scores
        - Exam results
        
        **Period:** September 2025 - May 2026  
        **Observations:** 25 data points
        """)
    
    with col3:
        st.markdown("""
        ### Key Questions
        
        1. What habits improve my academic performance?
        2. What is the trade-off between stress and productivity?
        3. How does sleep affect my exam performance?
        4. Can I replicate finals-level focus earlier?
        5. Is this workload sustainable long-term?
        """)
    
    st.markdown("---")
    st.markdown("""
    ## Semester Comparison
    """)
    
    comparison_data = {
        'Metric': ['Number of Courses', 'GPA', 'Average Stress (1-5)', 'Average Sleep (hours)', 'Average Study Hours'],
        'Fall 2025': [3, 3.31, '2-3', '8+', 6],
        'Spring 2026': [5, 3.57, '3-5', 7, 8],
        'Change': ['+2', '+0.26', '+1-2', '-1', '+2']
    }
    
    comparison_df = pd.DataFrame(comparison_data)
    st.dataframe(comparison_df, use_container_width=True, hide_index=True)
    
    st.markdown("""
    ### Initial Observations
    
    Despite taking 5 courses instead of 3, my GPA actually improved. However, this came at a cost:
    - Stress levels increased significantly
    - Sleep hours decreased by about 1 hour per night
    - Study hours increased by 2 hours per day
    
    This raises important questions about sustainability and whether this pattern can continue.
    """)

# ============================================================================
# PAGE 2: DATA VISUALIZATIONS & KEY INSIGHTS
# ============================================================================
elif page == "📊 Data Visualizations":
    st.title("📊 Data Visualizations & Key Insights")
    
    st.markdown("## Visualization 1: Study Hours vs Sleep Hours Over Time")
    
    # Chart 1: Study vs Sleep
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(
        x=df['Date'], y=df['Study_Hours'],
        mode='lines+markers',
        name='Study Hours',
        line=dict(color='#1f77b4', width=3),
        marker=dict(size=6)
    ))
    fig1.add_trace(go.Scatter(
        x=df['Date'], y=df['Sleep_Hours'],
        mode='lines+markers',
        name='Sleep Hours',
        line=dict(color='#ff7f0e', width=3),
        marker=dict(size=6)
    ))
    fig1.update_layout(
        title="Study Hours vs Sleep Hours - The Trade-off Pattern",
        xaxis_title="Date",
        yaxis_title="Hours",
        hovermode='x unified',
        height=400,
        template='plotly_white'
    )
    st.plotly_chart(fig1, use_container_width=True)
    
    st.markdown("""
    **Key Finding:** There is a clear inverse relationship between study hours and sleep hours. 
    As study hours increase (especially during midterms and finals), sleep hours decrease. 
    This trade-off is most pronounced during high-stress periods.
    """)
    
    st.markdown("---")
    st.markdown("## Visualization 2: Stress vs Productivity Correlation")
    
    # Chart 2: Stress vs Productivity
    fig2 = px.scatter(
        df, x='Stress_Level', y='Productivity_Level',
        color='Exam_Period',
        size='Study_Hours',
        hover_data=['Date', 'Sleep_Hours'],
        title="Stress Level vs Productivity - The Paradox",
        labels={'Stress_Level': 'Stress Level (1-5)', 'Productivity_Level': 'Productivity (1-5)'},
        color_discrete_map={'Normal': '#2ca02c', 'Midterm': '#ff7f0e', 'Finals': '#d62728'}
    )
    fig2.update_layout(height=400, template='plotly_white')
    st.plotly_chart(fig2, use_container_width=True)
    
    st.markdown("""
    **Key Finding:** Counterintuitively, maximum stress (5/5) correlates with maximum productivity (5/5). 
    This suggests that deadline pressure creates conditions that enhance focus and output, 
    though this may be subject to outcome bias.
    """)
    
    st.markdown("---")
    st.markdown("## Visualization 3: Exam Performance Trajectory")
    
    # Chart 3: Exam Scores Over Semester
    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(
        x=['Week 1-3\n(Beginning)', 'Week 8-10\n(Midterm)', 'Week 14-16\n(Finals)'],
        y=[85, 72.5, 92.5],
        mode='lines+markers',
        name='Average Score',
        line=dict(color='#1f77b4', width=4),
        marker=dict(size=12, color=['#2ca02c', '#d62728', '#2ca02c'])
    ))
    fig3.update_layout(
        title="Exam Performance Trajectory - The Midterm Dip",
        xaxis_title="Semester Phase",
        yaxis_title="Average Score",
        yaxis=dict(range=[60, 100]),
        height=400,
        template='plotly_white',
        showlegend=False
    )
    st.plotly_chart(fig3, use_container_width=True)
    
    st.markdown("""
    **Key Finding:** There is a consistent 20-25 point drop in performance during midterms 
    compared to both the beginning of the semester and finals. This pattern appears in both semesters, 
    suggesting a systematic issue with midterm preparation strategy.
    """)
    
    st.markdown("---")
    st.markdown("## Visualization 4: Weekday vs Weekend Study Patterns")
    
    # Chart 4: Weekday vs Weekend
    weekday_study = [8, 8.5, 9, 8, 7, 2, 2]  # Mon-Sun
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    colors = ['#1f77b4']*5 + ['#ff7f0e']*2
    
    fig4 = go.Figure(data=[
        go.Bar(x=days, y=weekday_study, marker_color=colors)
    ])
    fig4.update_layout(
        title="Average Study Hours by Day of Week (Normal Weeks)",
        xaxis_title="Day of Week",
        yaxis_title="Study Hours",
        height=400,
        template='plotly_white',
        showlegend=False
    )
    st.plotly_chart(fig4, use_container_width=True)
    
    st.markdown("""
    **Key Finding:** Study hours are high on weekdays (7-9 hours) but drop dramatically on weekends (2 hours). 
    This is when social media consumption (YouTube Reels, Instagram) peaks. However, during finals weeks, 
    weekend study hours increase to 8-10 hours, showing that this behavior is discretionary, not compulsive.
    """)
    
    st.markdown("---")
    st.markdown("## 🔍 Key Insights Summary")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Insight 1: Sleep-Study Trade-off
        - Study hours increase from 6 to 10-12 during finals
        - Sleep decreases from 8+ to 5-7 hours
        - **Risk:** Chronic sleep deprivation may harm long-term health
        
        ### Insight 2: Productivity Paradox
        - Maximum stress correlates with maximum productivity
        - Deadline pressure enhances focus
        - **Caveat:** Outcome bias may inflate self-rated productivity
        """)
    
    with col2:
        st.markdown("""
        ### Insight 3: Midterm Vulnerability
        - Consistent 20-25 point gap between midterm and finals
        - Suggests midterm prep strategy is less effective
        - Opportunity to improve through earlier preparation
        
        ### Insight 4: Discretionary Behavior
        - Weekend social media dominates normal weeks (6+ hours)
        - Drops to minimal during finals (redirected to study)
        - Shows behavior can be changed with motivation
        """)

# ============================================================================
# PAGE 3: DECISION-MAKING SECTION
# ============================================================================
elif page == "🎯 Decision-Making":
    st.title("🎯 Decision-Making Section")
    
    st.markdown("""
    ## Based on My Data, What Should I Do Differently in the Future?
    
    The data reveals clear patterns that can inform future academic strategies. 
    However, each recommendation comes with trade-offs and limitations.
    """)
    
    st.markdown("---")
    st.markdown("## 5 Evidence-Based Recommendations")
    
    recommendations = [
        {
            "number": "1",
            "title": "Protect Sleep During Exams",
            "action": "Maintain 7-8 hours minimum, reduce study hours if needed",
            "rationale": "Research shows 7-8 hours optimal for memory retention and exam performance",
            "data_support": "Sleep deprivation during finals (5-7 hours) correlates with increased stress",
            "trade_off": "May reduce study time, but improves retention and cognitive function"
        },
        {
            "number": "2",
            "title": "Start Midterm Prep 2 Weeks Earlier",
            "action": "Begin studying 2 weeks in advance instead of 1 week",
            "rationale": "Consistent 20-25 point gap between midterm (70-75) and finals (90-95) scores",
            "data_support": "Pattern repeats across both semesters, indicating systematic issue",
            "trade_off": "Requires more sustained effort earlier, but improves midterm performance"
        },
        {
            "number": "3",
            "title": "Redirect Weekend Social Media Time",
            "action": "Limit to 1-2 hours, especially weeks 5-7 (pre-midterm)",
            "rationale": "Currently only 2 hours study on weekends; redirecting 2-3 hours could improve preparation",
            "data_support": "Behavior is discretionary—drops to minimal during finals",
            "trade_off": "Reduces leisure time, but provides 10-15 hours extra study per month"
        },
        {
            "number": "4",
            "title": "Front-Load Internship Work",
            "action": "Concentrate internship during weeks 1-7 (low-stress periods)",
            "rationale": "Reduces concurrent demands during midterms and finals",
            "data_support": "Stress levels peak during exam periods; front-loading reduces overlap",
            "trade_off": "More intense early semester, but provides breathing room during exams"
        },
        {
            "number": "5",
            "title": "Replicate Finals Focus Earlier",
            "action": "Create artificial deadlines and structured study environments",
            "rationale": "Peak productivity occurs during finals; replicating these conditions could improve earlier performance",
            "data_support": "Productivity jumps to 5/5 during finals despite similar stress levels",
            "trade_off": "Requires discipline to maintain artificial pressure, but improves consistency"
        }
    ]
    
    for rec in recommendations:
        st.markdown(f"""
        ### Recommendation {rec['number']}: {rec['title']}
        
        **Action:** {rec['action']}
        
        **Rationale:** {rec['rationale']}
        
        **Data Support:** {rec['data_support']}
        
        **Trade-off:** {rec['trade_off']}
        """)
        st.markdown("---")
    
    st.markdown("""
    ## Implementation Strategy
    
    ### Phase 1: Immediate (Next Semester)
    - Protect sleep: Commit to 7-8 hours minimum during exam periods
    - Start midterm prep 2 weeks earlier
    - Monitor effectiveness through tracking
    
    ### Phase 2: Medium-term (Following Year)
    - Redirect weekend social media time gradually
    - Front-load internship work
    - Establish artificial deadlines for consistency
    
    ### Phase 3: Long-term
    - Develop sustainable study habits
    - Balance academic performance with health
    - Adjust based on outcomes and well-being
    """)
    
    st.markdown("---")
    st.markdown("""
    ## Important Caveats
    
    ⚠️ **These recommendations are based on:**
    - Only 25 observations over 2 semesters
    - Self-reported data subject to bias
    - One person's experience (may not generalize)
    - Correlation, not necessarily causation
    
    ✅ **Before implementing:**
    - Test recommendations gradually
    - Monitor outcomes objectively
    - Adjust based on personal results
    - Prioritize health and well-being over grades
    """)

# ============================================================================
# PAGE 4: ETHICS & RESPONSIBILITY
# ============================================================================
elif page == "⚖️ Ethics & Responsibility":
    st.title("⚖️ Ethics & Responsibility")
    
    st.markdown("""
    ## 🔒 Privacy Statement
    """)
    
    st.markdown("""
    ### What Data is Included?
    
    This dashboard contains:
    - **Included:** Study hours, sleep hours, stress levels, productivity ratings, exam scores, course load
    - **Anonymized:** No real names, no specific company names (internship referred to generically)
    - **Aggregated:** Individual assignment scores are averaged, not listed separately
    - **Generalized:** Specific course names and instructors not identified
    
    ### What is Anonymized?
    
    - Internship company name (referred to as "tech company working on fraud detection")
    - Civic engagement project details (referred to as "SDS Bridge Program")
    - Specific course codes and instructors
    - Personal identifiers (email, ID numbers, etc.)
    - Specific dates replaced with semester phases (Week 1-3, Week 8-10, etc.)
    """)
    
    st.markdown("---")
    st.markdown("""
    ## ⚠️ Bias & Limitation Disclosure
    """)
    
    bias_data = {
        'Bias/Limitation': [
            'Memory Bias',
            'Subjective Measurement',
            'Small Sample Size',
            'Confounding Variables',
            'Outcome Bias',
            'Survivorship Bias',
            'Selection Bias'
        ],
        'Description': [
            'All data collected retrospectively based on recollection. Stress and productivity levels particularly subject to recall bias.',
            'Stress and productivity are self-rated 1-5 scales without objective tools (cortisol levels, time-tracking software).',
            'Only 25 observations across 2 semesters. Too small for statistical significance. Patterns may not generalize to future semesters.',
            'Course difficulty, instructor quality, and external life events not controlled for. Unmeasured factors may influence patterns.',
            'Productivity self-rating may be inflated during finals because better results achieved, not because more productive.',
            'Only tracking successful academic outcomes. Failures or dropped courses not included in analysis.',
            'Data only from semesters where I took 3-5 courses. May not represent other course loads.'
        ],
        'Impact': [
            'High',
            'High',
            'Medium',
            'High',
            'Medium',
            'Medium',
            'Low'
        ]
    }
    
    bias_df = pd.DataFrame(bias_data)
    st.dataframe(bias_df, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    st.markdown("""
    ## 📊 Visualization Justification
    """)
    
    viz_justification = {
        'Visualization': [
            'Study Hours vs Sleep Hours',
            'Stress vs Productivity',
            'Exam Performance Trajectory',
            'Weekday vs Weekend Study'
        ],
        'Why Chosen': [
            'Line chart shows time-series trend clearly, reveals inverse relationship',
            'Scatter plot with color/size encoding shows multivariate relationships',
            'Line chart emphasizes the midterm dip pattern across semester',
            'Bar chart compares discrete categories (days of week)'
        ],
        'Risk of Misinterpretation': [
            'May appear to show causation (sleep causes study hours) when actually both respond to exam pressure',
            'Correlation between stress and productivity might suggest stress improves performance, but causation unclear',
            'Midterm dip might be attributed to lack of preparation, but could be due to course difficulty variation',
            'Weekend pattern might be seen as laziness, but is actually discretionary behavior (changes during finals)'
        ],
        'Mitigation': [
            'Include explanation of confounding variable (exam period)',
            'Include caveat about outcome bias and alternative explanations',
            'Discuss multiple possible causes (preparation strategy, course difficulty, motivation)',
            'Show that behavior changes during finals, proving it is discretionary'
        ]
    }
    
    viz_df = pd.DataFrame(viz_justification)
    st.dataframe(viz_df, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    st.markdown("""
    ## 🎯 Responsible Decision-Making
    """)
    
    st.markdown("""
    ### Limitations of My Recommendations
    
    1. **Generalizability:** These recommendations are based on my data and may not apply to others with different:
       - Learning styles
       - Course types
       - Personal circumstances
       - Stress responses
    
    2. **Causation vs Correlation:** I cannot definitively say that:
       - Protecting sleep will improve grades (correlation observed, but causation not proven)
       - Starting midterm prep earlier will close the performance gap
       - Redirecting social media time will improve outcomes
    
    3. **Trade-offs Not Fully Explored:**
       - Protecting sleep might reduce study time and hurt grades
       - Front-loading internship might create early-semester stress
       - Artificial deadlines might create unnecessary pressure
    
    4. **Individual Variation:**
       - What works for me may not work for others
       - My stress response may differ from peers
       - My learning patterns are unique to me
    
    ### How to Use This Dashboard Responsibly
    
    ✅ **DO:**
    - Use patterns to inform decisions, not dictate them
    - Test recommendations gradually and monitor outcomes
    - Adjust based on personal results and well-being
    - Combine with other sources of information
    - Prioritize health and well-being over grades
    
    ❌ **DON'T:**
    - Assume these patterns apply to everyone
    - Implement all recommendations simultaneously
    - Ignore warning signs of burnout or health issues
    - Treat correlations as definitive proof of causation
    - Sacrifice mental or physical health for academic performance
    """)
    
    st.markdown("---")
    st.markdown("""
    ## 🔗 Correlation ≠ Causation
    
    This dashboard shows correlations observed in my data. Important reminders:
    
    - **Correlation:** Two variables move together (e.g., stress and productivity both increase during finals)
    - **Causation:** One variable causes changes in another (e.g., stress causes increased productivity)
    
    In this data:
    - High stress and high productivity are correlated during finals
    - But both may be caused by a third factor: **exam deadlines**
    - Stress doesn't cause productivity; deadlines cause both
    
    This is why recommendations should be tested carefully before full implementation.
    """)

# ============================================================================
# PAGE 5: INTERACTIVE DATA EXPLORER
# ============================================================================
elif page == "🔍 Data Explorer":
    st.title("🔍 Interactive Data Explorer")
    
    st.markdown("""
    Explore the raw data and create custom visualizations. Use the filters below to focus on specific time periods or exam phases.
    """)
    
    st.markdown("---")
    st.markdown("## Data Filters")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        exam_period_filter = st.multiselect(
            "Exam Period:",
            options=df['Exam_Period'].unique(),
            default=df['Exam_Period'].unique()
        )
    
    with col2:
        date_range = st.slider(
            "Date Range:",
            min_value=df['Date'].min(),
            max_value=df['Date'].max(),
            value=(df['Date'].min(), df['Date'].max()),
            format="YYYY-MM-DD"
        )
    
    with col3:
        stress_range = st.slider(
            "Stress Level Range:",
            min_value=int(df['Stress_Level'].min()),
            max_value=int(df['Stress_Level'].max()),
            value=(int(df['Stress_Level'].min()), int(df['Stress_Level'].max()))
        )
    
    # Filter data
    filtered_df = df[
        (df['Exam_Period'].isin(exam_period_filter)) &
        (df['Date'] >= date_range[0]) &
        (df['Date'] <= date_range[1]) &
        (df['Stress_Level'] >= stress_range[0]) &
        (df['Stress_Level'] <= stress_range[1])
    ]
    
    st.markdown("---")
    st.markdown(f"## Filtered Data ({len(filtered_df)} records)")
    
    st.dataframe(filtered_df, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    st.markdown("## Summary Statistics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Avg Study Hours", f"{filtered_df['Study_Hours'].mean():.1f}")
    with col2:
        st.metric("Avg Sleep Hours", f"{filtered_df['Sleep_Hours'].mean():.1f}")
    with col3:
        st.metric("Avg Stress Level", f"{filtered_df['Stress_Level'].mean():.1f}")
    with col4:
        st.metric("Avg Productivity", f"{filtered_df['Productivity_Level'].mean():.1f}")
    
    st.markdown("---")
    st.markdown("## Custom Visualization")
    
    col1, col2 = st.columns(2)
    
    with col1:
        x_axis = st.selectbox("X-Axis:", options=df.columns[1:])
    with col2:
        y_axis = st.selectbox("Y-Axis:", options=df.columns[1:], index=2)
    
    if x_axis and y_axis and x_axis != y_axis:
        fig = px.scatter(
            filtered_df, x=x_axis, y=y_axis,
            color='Exam_Period',
            size='Study_Hours' if 'Study_Hours' in df.columns else None,
            hover_data=['Date'],
            title=f"{y_axis} vs {x_axis}",
            color_discrete_map={'Normal': '#2ca02c', 'Midterm': '#ff7f0e', 'Finals': '#d62728'}
        )
        fig.update_layout(height=500, template='plotly_white')
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    st.markdown("## Download Filtered Data")
    
    csv = filtered_df.to_csv(index=False)
    st.download_button(
        label="Download as CSV",
        data=csv,
        file_name="academic_journey_filtered.csv",
        mime="text/csv"
    )

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p><strong>Academic Improvement Journey Dashboard</strong></p>
    <p>Data Collection Period: September 2025 - May 2026</p>
    <p>25 observations | Self-reported and transcript data</p>
    <p style='font-size: 12px; color: #999;'>
        This dashboard is for educational purposes as part of Data201: Data Communication and Ethics
    </p>
</div>
""", unsafe_allow_html=True)
