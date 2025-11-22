import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from groq import Groq
from dotenv import load_dotenv
import os
from datetime import datetime
try:
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet
    REPORTLAB_AVAILABLE = True
except:
    REPORTLAB_AVAILABLE = False

# Load environment variables
load_dotenv()

# Initialize GROQ client (use your API key)
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("❌ GROQ_API_KEY not configured. Please set your API key in the .env file.")
    st.info("Steps to fix:\n1. Get your API key from https://console.groq.com\n2. Add it to the .env file:\nGROQ_API_KEY=your_key_here\n3. Restart the app")
    st.stop()

try:
    client = Groq(api_key=api_key)
except Exception as e:
    st.error(f"❌ Error initializing Groq client: {str(e)}")
    st.stop()

# Page config
st.set_page_config(
    page_title="Multi-Agent Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS for clean UI ---
st.markdown("""
<style>
/* White and Green gradient background with animation */
.stApp {
    background: linear-gradient(135deg, #ffffff 0%, #e8f5e9 25%, #c8e6c9 50%, #a5d6a7 75%, #81c784 100%);
    background-size: 400% 400%;
    animation: gradientFlow 15s ease infinite;
    color: #000000;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

@keyframes gradientFlow {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Main container */
.main {
    padding: 2rem;
}

/* Card style with animations */
.agent-card, .metric-card, .custom-insight-box {
    background: linear-gradient(135deg, #ffffff 0%, #f1f8f4 100%);
    border-radius: 16px;
    padding: 25px;
    margin-bottom: 25px;
    box-shadow: 0 8px 24px rgba(76, 175, 80, 0.15);
    border: 2px solid rgba(76, 175, 80, 0.2);
    transition: all 0.4s ease;
    animation: slideUp 0.6s ease;
}

.agent-card:hover, .metric-card:hover, .custom-insight-box:hover {
    transform: translateY(-8px);
    box-shadow: 0 12px 32px rgba(76, 175, 80, 0.25);
    border-color: rgba(76, 175, 80, 0.4);
}

@keyframes slideUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Headings */
h1 {
    color: #1b5e20 !important;
    font-weight: 800;
    text-shadow: 2px 2px 4px rgba(76, 175, 80, 0.2);
    animation: fadeIn 1s ease;
}

h2, h3 {
    color: #2e7d32 !important;
    font-weight: 700;
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

/* All text in black */
p, label, .stMarkdown, .stText, span, div {
    color: #000000 !important;
}

/* Buttons with green gradient */
.stButton>button, .stDownloadButton>button {
    background: linear-gradient(135deg, #4caf50 0%, #66bb6a 50%, #81c784 100%);
    color: white !important;
    border-radius: 12px;
    padding: 12px 30px;
    font-weight: bold;
    font-size: 16px;
    border: none;
    box-shadow: 0 4px 15px rgba(76, 175, 80, 0.3);
    transition: all 0.3s ease;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.stButton>button:hover, .stDownloadButton>button:hover {
    background: linear-gradient(135deg, #81c784 0%, #66bb6a 50%, #4caf50 100%);
    transform: scale(1.05) translateY(-2px);
    box-shadow: 0 6px 20px rgba(76, 175, 80, 0.5);
}

.stButton>button:active, .stDownloadButton>button:active {
    transform: scale(0.98);
}

/* File uploader with animation */
.stFileUploader {
    background: linear-gradient(135deg, #ffffff 0%, #f1f8f4 100%);
    border: 3px dashed #4caf50;
    border-radius: 16px;
    padding: 25px;
    transition: all 0.3s ease;
    animation: pulse 2s ease-in-out infinite;
}

.stFileUploader:hover {
    border-color: #2e7d32;
    background: linear-gradient(135deg, #f1f8f4 0%, #e8f5e9 100%);
    transform: scale(1.02);
}

@keyframes pulse {
    0%, 100% { box-shadow: 0 0 0 0 rgba(76, 175, 80, 0.4); }
    50% { box-shadow: 0 0 0 10px rgba(76, 175, 80, 0); }
}

/* Sidebar styling */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #e8f5e9 0%, #c8e6c9 100%);
    border-right: 3px solid #4caf50;
}

[data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
    color: #1b5e20 !important;
}

/* Metrics with green accents */
.stMetric {
    background: linear-gradient(135deg, #ffffff 0%, #e8f5e9 100%);
    padding: 15px;
    border-radius: 12px;
    border-left: 5px solid #4caf50;
    box-shadow: 0 4px 12px rgba(76, 175, 80, 0.15);
    transition: all 0.3s ease;
}

.stMetric:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 20px rgba(76, 175, 80, 0.25);
}

/* Info boxes */
.stInfo {
    background-color: #e8f5e9 !important;
    border-left: 5px solid #4caf50 !important;
    color: #000000 !important;
    border-radius: 8px;
    animation: slideIn 0.5s ease;
}

.stSuccess {
    background-color: #c8e6c9 !important;
    border-left: 5px solid #2e7d32 !important;
    color: #000000 !important;
    border-radius: 8px;
    animation: slideIn 0.5s ease;
}

@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateX(-20px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

/* Input fields */
.stTextInput input, .stSelectbox select, .stMultiSelect {
    background-color: #ffffff !important;
    color: #000000 !important;
    border: 2px solid #4caf50 !important;
    border-radius: 8px;
    transition: all 0.3s ease;
}

.stTextInput input:focus, .stSelectbox select:focus {
    border-color: #2e7d32 !important;
    box-shadow: 0 0 0 3px rgba(76, 175, 80, 0.2);
}

/* Dataframe styling */
.dataframe {
    background-color: #ffffff !important;
    color: #000000 !important;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 12px rgba(76, 175, 80, 0.15);
}

.dataframe th {
    background: linear-gradient(135deg, #4caf50 0%, #66bb6a 100%) !important;
    color: white !important;
    font-weight: bold;
    padding: 12px;
}

.dataframe td {
    color: #000000 !important;
    padding: 10px;
    border-bottom: 1px solid #e8f5e9;
}

.dataframe tr:hover {
    background-color: #f1f8f4 !important;
}

/* Responsive design */
@media (max-width: 768px) {
    .agent-card, .metric-card, .custom-insight-box {
        padding: 15px;
        margin-bottom: 15px;
    }
    
    .stButton>button, .stDownloadButton>button {
        padding: 10px 20px;
        font-size: 14px;
    }
    
    h1 {
        font-size: 2rem !important;
    }
}

/* Smooth scrolling */
html {
    scroll-behavior: smooth;
}

/* Loading animation */
.stSpinner > div {
    border-color: #4caf50 !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Agents ---------------- #

# Agent 1: Data Analysis
def agent_1_analyze_data(df):
    st.markdown('<div class="agent-card">', unsafe_allow_html=True)
    st.subheader("🤖 Agent 1: Data Analysis")

    analysis = {
        "shape": df.shape,
        "columns": list(df.columns),
        "dtypes": df.dtypes.to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
        "numeric_columns": df.select_dtypes(include=['int64','float64']).columns.tolist(),
        "categorical_columns": df.select_dtypes(include=['object']).columns.tolist(),
        "summary_stats": df.describe().to_dict()
    }

    prompt = f"""Analyze this dataset and provide cleaning recommendations:
    - Shape: {analysis['shape']}
    - Columns: {analysis['columns']}
    - Data types: {analysis['dtypes']}
    - Missing values: {analysis['missing_values']}
    Provide a brief analysis (3-4 sentences) about data quality and cleaning recommendations."""

    try:
        response = client.chat.completions.create(
            messages=[{"role":"user","content":prompt}],
            model="llama3-8b-8192",
            temperature=0.7,
            max_tokens=300
        )
        insights = response.choices[0].message.content
    except Exception as e:
        insights = f"⚠️ Could not generate insights. Error: {str(e)[:100]}. Please check your API key and rate limits."

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Rows", f"{analysis['shape'][0]:,}")
    col2.metric("Total Columns", analysis['shape'][1])
    col3.metric("Missing Values", sum(analysis['missing_values'].values()))
    st.info(insights)
    st.markdown('</div>', unsafe_allow_html=True)

    return analysis, insights

# Agent 2: Dashboard Planning
def agent_2_plan_dashboard(analysis):
    st.markdown('<div class="agent-card">', unsafe_allow_html=True)
    st.subheader("🎨 Agent 2: Dashboard Planning")

    prompt = f"""Based on this dataset analysis, suggest the best visualizations:
    - Numeric columns: {analysis['numeric_columns']}
    - Categorical columns: {analysis['categorical_columns']}
    Suggest 2 bar, 1 line, 2 pie charts."""

    try:
        response = client.chat.completions.create(
            messages=[{"role":"user","content":prompt}],
            model="llama3-8b-8192",
            temperature=0.7,
            max_tokens=400
        )
        plan = response.choices[0].message.content
    except Exception as e:
        plan = f"""⚠️ Could not generate visualization plan: {str(e)[:100]}

Fallback Visualization Plan:
- Bar Chart 1: Distribution of categorical features
- Bar Chart 2: Top values comparison
- Line Chart: Trend analysis
- Pie Chart 1: Category proportions
- Pie Chart 2: Segment distribution"""

    st.success(plan)
    st.markdown('</div>', unsafe_allow_html=True)
    return plan

# Agent 3: Visualization Generator
def agent_3_generate_visualizations(df, analysis, filters):
    st.markdown('<div class="agent-card">', unsafe_allow_html=True)
    st.subheader("📊 Agent 3: Visualization Generator")

    filtered_df = df.copy()
    for col, values in filters.items():
        if values:
            filtered_df = filtered_df[filtered_df[col].isin(values)]

    # Bar Chart
    if analysis['categorical_columns']:
        cat_col = analysis['categorical_columns'][0]
        counts = filtered_df[cat_col].value_counts().reset_index()
        counts.columns = [cat_col, 'count']
        fig = px.bar(counts, x=cat_col, y='count', text='count', title=f'Distribution of {cat_col}')
        st.plotly_chart(fig, use_container_width=True)

    # Pie Chart
    if len(analysis['categorical_columns'])>1:
        cat_col2 = analysis['categorical_columns'][1]
        pie_data = filtered_df[cat_col2].value_counts().head(8)
        fig2 = px.pie(values=pie_data.values, names=pie_data.index, title=f'{cat_col2} Distribution')
        st.plotly_chart(fig2, use_container_width=True)

    # Line Chart
    if analysis['numeric_columns']:
        num_col = analysis['numeric_columns'][0]
        fig3 = px.line(filtered_df.reset_index(), x='index', y=num_col, title=f'{num_col} Trend', markers=True)
        st.plotly_chart(fig3, use_container_width=True)

    # Correlation Heatmap
    if len(analysis['numeric_columns'])>1:
        corr = filtered_df[analysis['numeric_columns']].corr()
        fig4 = px.imshow(corr, text_auto='.2f', aspect='auto', title='Feature Correlation Matrix')
        st.plotly_chart(fig4, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)
    return filtered_df

# Agent 4: Dashboard Code Generator
def agent_4_generate_dashboard_code(df, analysis, custom_insights=""):
    insights_code = f'"""{custom_insights}"""' if custom_insights else '"""No custom insights."""'
    code = f"""
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("your_dataset.csv")
st.title("📊 Analytics Dashboard")
st.header("Custom Insights")
st.info({insights_code})
"""
    return code

# Agent 5: PDF Report Generator
def agent_5_generate_pdf(df, analysis, filtered_df, custom_insights=""):
    if not REPORTLAB_AVAILABLE:
        # Fallback: return a text-based report
        report = f"""Analytics Dashboard Report
Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Custom Insights:
{custom_insights}

Dataset Overview:
- Total Rows: {analysis['shape'][0]}
- Total Columns: {analysis['shape'][1]}
- Filtered Rows: {len(filtered_df)}

Key Statistics:
- Numeric Columns: {len(analysis['numeric_columns'])}
- Categorical Columns: {len(analysis['categorical_columns'])}
"""
        return report.encode('utf-8')
    
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
        from reportlab.lib.styles import getSampleStyleSheet
        from io import BytesIO
        
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        story = []
        styles = getSampleStyleSheet()
        
        story.append(Paragraph("Analytics Dashboard Report", styles['Heading1']))
        story.append(Spacer(1, 12))
        
        if custom_insights:
            story.append(Paragraph("Custom Insights", styles['Heading2']))
            story.append(Paragraph(custom_insights[:500], styles['Normal']))
            story.append(Spacer(1, 12))
        
        story.append(Paragraph("Dataset Overview", styles['Heading2']))
        story.append(Paragraph(f"Total Rows: {analysis['shape'][0]}", styles['Normal']))
        story.append(Paragraph(f"Total Columns: {analysis['shape'][1]}", styles['Normal']))
        story.append(Paragraph(f"Filtered Rows: {len(filtered_df)}", styles['Normal']))
        story.append(Spacer(1, 12))
        
        story.append(Paragraph("Key Insights", styles['Heading2']))
        story.append(Paragraph(f"The dataset contains {len(analysis['numeric_columns'])} numeric and {len(analysis['categorical_columns'])} categorical features.", styles['Normal']))
        story.append(Spacer(1, 12))
        
        story.append(Paragraph(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles['Italic']))
        
        doc.build(story)
        return buffer.getvalue()
    except Exception as e:
        report = f"""Analytics Dashboard Report
Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Error: {str(e)}
"""
        return report.encode('utf-8')

# Agent 6: Custom Insights
def agent_6_customize_insights(df, analysis, user_prompt):
    st.markdown('<div class="agent-card">', unsafe_allow_html=True)
    st.subheader("✨ Agent 6: Insight Customization")
    try:
        response = client.chat.completions.create(
            messages=[{"role":"user","content":user_prompt}],
            model="llama3-8b-8192",
            temperature=0.7,
            max_tokens=500
        )
        custom_insights = response.choices[0].message.content
        st.markdown('<div class="custom-insight-box">', unsafe_allow_html=True)
        st.write(custom_insights)
        st.markdown('</div>', unsafe_allow_html=True)
    except Exception as e:
        custom_insights = f"⚠️ Could not generate custom insights: {str(e)[:100]}. Please check your API key."
        st.error(custom_insights)
    st.markdown('</div>', unsafe_allow_html=True)
    return custom_insights

# ---------------- Main App ---------------- #
def main():
    st.title("🚀 Multi-Agent Analytics Dashboard")
    st.markdown("### Powered by 6 AI Agents for Intelligent Data Analysis")

    uploaded_file = st.file_uploader("📁 Upload your dataset (CSV, XLSX, JSON)", type=['csv','xlsx','json'])
    if uploaded_file is not None:
        ext = uploaded_file.name.split('.')[-1]
        if ext == 'csv':
            df = pd.read_csv(uploaded_file)
        elif ext == 'xlsx':
            df = pd.read_excel(uploaded_file)
        else:
            df = pd.read_json(uploaded_file)

        analysis, agent1_insights = agent_1_analyze_data(df)

        # Filters
        st.sidebar.header("Filters")
        filters = {}
        for i, col in enumerate(analysis['categorical_columns'][:3]):
            selected = st.sidebar.multiselect(f"Filter {col}", options=df[col].unique(), default=[])
            filters[col] = selected
        for i, col in enumerate(analysis['numeric_columns'][:2]):
            min_val, max_val = float(df[col].min()), float(df[col].max())
            selected_range = st.sidebar.slider(f"{col} range", min_val, max_val, (min_val,max_val))
            if selected_range != (min_val,max_val):
                filters[col] = selected_range

        plan = agent_2_plan_dashboard(analysis)

        st.markdown("---")
        st.header("✨ Customize Your Insights with AI")
        user_prompt = st.text_input("Enter your insight request:")
        generate_insights = st.button("🚀 Generate")
        if generate_insights and user_prompt:
            custom_insights = agent_6_customize_insights(df, analysis, user_prompt)
        else:
            custom_insights = ""

        filtered_df = agent_3_generate_visualizations(df, analysis, filters)

        # Downloads
        st.markdown("---")
        st.header("📥 Download Options")
        col1, col2 = st.columns(2)
        with col1:
            dashboard_code = agent_4_generate_dashboard_code(df, analysis, custom_insights)
            st.download_button("📄 Download dashboard.py", dashboard_code, "dashboard.py", "text/plain")
        with col2:
            pdf_bytes = agent_5_generate_pdf(df, analysis, filtered_df, custom_insights)
            st.download_button("📑 Download PDF Report", pdf_bytes, f"analytics_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf", "application/pdf")

        # Data preview
        st.markdown("---")
        st.header("📋 Filtered Data Preview")
        st.dataframe(filtered_df.head(10))
    else:
        st.info("👆 Please upload a CSV, XLSX, or JSON file to begin analysis")

if __name__ == "__main__":
    main()
