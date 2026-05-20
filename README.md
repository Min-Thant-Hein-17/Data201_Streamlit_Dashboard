# 📚 MinThant_DataCom_Final_Project_Personal_Dashboard

An interactive Streamlit dashboard tracking my undergraduate academic journey, built for the **Data Communication and Ethics (DATA 201)** course at **Parami University**.

> This project analyzes the relationship between academic workload, study habits, sleep, stress, and academic performance across two semesters — using self-tracked daily data and interactive visualizations.

---

## 🌐 Live App

👉 **[View the Live Dashboard](https://your-app-url.streamlit.app)** *(replace with your Streamlit Cloud URL)*

---

## 📖 Project Overview

This project maps my personal academic journey from Fall 2025 through Spring 2026 — a semester where I took on significantly more responsibilities than ever before: **5 courses**, an **internship** (fraud detection analysis dashboard), and a **civic engagement project** (SDS Bridge Program).

Instead of guessing what helps me perform better academically, I tracked daily habits and outcomes over 8 months (September 2025 – May 2026) and built this dashboard to find honest, evidence-based answers to five key questions:

1. What habits actually improve my academic performance?
2. What is the real trade-off between stress and productivity?
3. How does sleep affect my exam performance?
4. Can I replicate finals-level focus earlier in the semester?
5. Is this workload sustainable long-term?

The result is a 5-page interactive dashboard that tells the story of the data, visualizes the patterns, makes evidence-based recommendations, and critically reflects on the ethical responsibilities of self-data analysis.

---

## 🗂️ Repository Structure

```
├── app.py                        # Main Streamlit application (5-page dashboard)
├── academic_journey_dataset.csv  # Self-tracked daily academic data (243 rows)
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

---

## 📊 Dataset Description

**File:** `academic_journey_dataset.csv`  
**Period:** September 2025 – May 2026  
**Coverage:** 8 months, 243 daily observations across 2 semesters

| Column | Type | Description |
|---|---|---|
| `Date` | date | Daily observation date |
| `Semester` | string | Fall 2025 or Spring 2026 |
| `Course_Load` | integer | Number of courses enrolled (3 or 5) |
| `Study_Hours` | integer | Hours spent studying that day |
| `Sleep_Hours` | integer | Hours of sleep that night |
| `Stress_Level` | integer | Self-rated stress on a 1–5 scale |
| `Productivity_Level` | integer | Self-rated productivity on a 1–5 scale |
| `Assignment_Score` | float | Score received (if applicable that day) |
| `Exam_Status` | string | Normal / Midterm / Final |
| `Is_Weekend` | boolean | Whether the day was a weekend |
| `Notes` | string | Contextual notes for notable days |

**Semester breakdown:**

| Semester | Months Tracked | Course Load | Additional Commitments |
|---|---|---|---|
| Fall 2025 | Sep, Oct, Dec 2025 | 3 courses | — |
| Spring 2026 | Jan – May 2026 | 5 courses | Internship + SDS Bridge Program |

---

## 🖥️ Dashboard Pages

### 📖 Page 1 — Story Overview
Introduces the academic journey with context, motivation, and a semester-by-semester comparison table. Answers *why* this data was collected and what questions it aims to answer.

### 📊 Page 2 — Data Visualizations
Four interactive Plotly charts with key findings:
- **Study vs Sleep Hours Over Time** — reveals the inverse trade-off pattern during exam periods
- **Stress vs Productivity Scatter** — explores the counterintuitive relationship between stress and output
- **Exam Performance Trajectory** — exposes the consistent midterm dip vs. finals recovery
- **Weekday vs Weekend Study (Box Plot)** — shows how study behaviour shifts with motivation

### 🎯 Page 3 — Decision-Making
Five evidence-based recommendations derived from the data patterns, each with a clear action, rationale, data support, and trade-off. Includes a phased implementation strategy.

### ⚖️ Page 4 — Ethics & Responsibility
Critical self-reflection on the data, covering:
- Privacy and anonymisation practices
- Bias and limitation disclosure (7 identified biases)
- Visualization justification and misinterpretation risks
- Correlation vs. causation discussion
- Responsible decision-making guidelines

### 🔍 Page 5 — Data Explorer
Fully interactive exploration of the raw dataset with sidebar filters (semester, exam status, stress range), summary statistics, a custom scatter plot builder, and a CSV download button.

---

## ⚙️ Sidebar Filters

All pages respond dynamically to three sidebar filters:

- **Semester** — filter by Fall 2025 and/or Spring 2026
- **Exam Status** — filter by Normal, Midterm, or Final periods
- **Stress Level Range** — slide to focus on specific stress levels (1–5)

---

## 🛠️ Technology Stack

| Tool | Purpose |
|---|---|
| [Streamlit](https://streamlit.io/) | Web app framework for the interactive dashboard |
| [Plotly](https://plotly.com/python/) | Interactive charts (line, scatter, box plots) |
| [Pandas](https://pandas.pydata.org/) | Data loading, filtering, and manipulation |
| [NumPy](https://numpy.org/) | Numerical operations and array handling |

**Why Plotly?**
Plotly was chosen over Matplotlib/Seaborn because it provides interactive visualizations natively supported by Streamlit — users can hover for exact values, zoom, and pan directly in the browser. Its ability to encode multiple variables (colour, size, axis) in a single chart call also made it well-suited to the multivariate nature of this dataset.

---

## 🚀 How to Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/your-username/data201_streamlit_dashboard.git
cd data201_streamlit_dashboard
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
streamlit run app.py
```

**4. Open in browser**  
The app will open automatically at `http://localhost:8501`

---

## 📦 Dependencies

```
streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.24.0
plotly>=5.18.0
```

---

## 🔍 Key Findings

| Finding | Pattern | Implication |
|---|---|---|
| Sleep–Study Trade-off | Study hours ↑ → Sleep hours ↓ during exams | Sleep deprivation is a recurring cost of exam preparation |
| Productivity Paradox | Stress 5/5 correlates with Productivity 5/5 | Deadline pressure enhances focus — but may reflect outcome bias |
| Midterm Vulnerability | Scores drop 20–25 points at midterms vs. finals | Preparation strategy is less effective at midterms |
| Discretionary Behaviour | Weekend study hours jump from 2 to 8–10 during finals | The behaviour can change — motivation is the missing variable |

---

## ⚠️ Limitations & Ethics

This dashboard is built on self-reported data and should be interpreted carefully:

- **Small sample:** 243 rows across 2 semesters is insufficient for statistical significance
- **Recall bias:** Stress and productivity ratings were retrospectively assigned
- **Correlation only:** No causal relationships can be established from this data
- **Single subject:** Findings apply to one person and should not be generalised
- **Survivorship bias:** Only successful semesters are tracked

Full bias disclosure is available in the **Ethics & Responsibility** page of the dashboard.

---

## 👤 Author

**Khant** — Undergraduate student, Parami University  
Course: Data Communication and Ethics (DATA 201)  
Academic Year: 2025–2026

---

## 📄 License

This project was created for academic purposes as part of a university course assessment. Data is self-reported and synthetic, created for educational use only.
