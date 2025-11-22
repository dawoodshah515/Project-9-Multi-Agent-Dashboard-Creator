# 🚀 Multi-Agent Analytics Dashboard

An intelligent Streamlit dashboard powered by 6 AI agents that automatically analyze datasets, generate insights, and create interactive visualizations.

## 📋 Features

### 🤖 6 AI Agents Working Together

1. **Agent 1: Data Analysis Agent**
   - Reads CSV files
   - Checks for missing data and data types
   - Recommends data cleaning strategies
   - Provides quality assessment

2. **Agent 2: Dashboard Planning Agent**
   - Designs visualization strategy
   - Recommends optimal chart types
   - Plans dashboard layout

3. **Agent 3: Visualization Generator**
   - Creates 2 interactive bar charts
   - Generates 1 line chart for trends
   - Produces 2 pie charts for distributions
   - Builds correlation heatmap

4. **Agent 4: Code Generator Agent**
   - Generates dataset-specific `dashboard.py`
   - Creates standalone dashboard code
   - Includes all visualizations
   - Embeds custom insights

5. **Agent 5: PDF Report Generator**
   - Creates comprehensive PDF reports
   - Includes filtered insights
   - Shows top 4 rows of data
   - Adds timestamp and metadata
   - Includes custom insights

6. **✨ Agent 6: Insight Customization Agent (NEW!)**
   - Generates custom insights based on your prompts
   - Answers specific questions about your data
   - Uses AI to provide actionable recommendations
   - Insights included in PDF and dashboard.py downloads

### 📊 Visualizations

- **2 Bar Charts**: Categorical distributions and top values
- **1 Line Chart**: Trend analysis over time/index
- **2 Pie Charts**: Category proportions and segments
- **Correlation Heatmap**: Feature relationships

### 🎯 Smart Features

- **Auto-detected Filters**: Sidebar automatically shows 3-4 most important filters
- **Dynamic Filtering**: All visualizations update in real-time
- **Export Options**: Download PDF reports and Python code
- **Beautiful UI**: Modern design with animations and gradients

## 🛠️ Installation

1. **Install Python** (if not already installed)
   - Download from [python.org](https://www.python.org/downloads/)
   - Make sure to check "Add Python to PATH" during installation

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   Or if `pip` doesn't work:
   ```bash
   python -m pip install -r requirements.txt
   ```

## 🚀 Usage

1. **Start the Dashboard**
   ```bash
   streamlit run app.py
   ```

2. **Upload Your Dataset**
   - Click "Browse files" button
   - Select any CSV file
   - The agents will automatically analyze it

3. **Explore Insights**
   - View AI-generated insights from Agent 1 & 2
   - Interact with visualizations
   - Use sidebar filters to drill down

4. **Export Results**
   - Download PDF report with insights
   - Download `dashboard.py` for standalone use

## 📁 Project Structure

```
Project 10/
├── .env                  # Environment variables (GROQ API key)
├── .gitignore           # Git ignore rules
├── app.py               # Main dashboard application
├── requirements.txt     # Python dependencies
├── sample_data.csv      # Sample dataset for testing
└── README.md           # This file
```

## 🔑 Environment Setup

The `.env` file contains your GROQ API key for AI agent functionality:

```
GROQ_API_KEY=your_api_key_here
```

**Note**: Keep this file secure and never commit it to public repositories.

## 📊 Sample Dataset

A sample employee dataset (`sample_data.csv`) is included with:
- 30 employee records
- 8 features (Name, Age, Department, Salary, etc.)
- Mix of numeric and categorical data
- Perfect for testing all dashboard features

## 🎨 Dashboard Features

### Automatic Filter Detection
The sidebar automatically detects and displays:
- Top 3 categorical features (as multiselect)
- Top 2 numeric features (as sliders)
- Only shows reasonable options (< 50 unique values)

### Real-time Updates
- All visualizations update when filters change
- Filtered data preview at the bottom
- Download buttons reflect current filters

### AI-Powered Insights
- GROQ API analyzes your data
- Provides cleaning recommendations
- Suggests optimal visualizations
- Generates contextual insights

## 🔧 Troubleshooting

### Python Not Found
If you get "Python was not found" error:
1. Install Python from [python.org](https://www.python.org/downloads/)
2. Restart your terminal/command prompt
3. Verify installation: `python --version`

### Module Not Found
If you get import errors:
```bash
pip install streamlit pandas plotly groq python-dotenv fpdf seaborn matplotlib
```

### GROQ API Errors
- Check your API key in `.env` file
- Ensure you have internet connection
- The dashboard will still work with fallback messages

## 📝 Generated Files

### dashboard.py
- Standalone Python script
- Contains all visualizations
- Customized for your dataset
- Can run independently

### PDF Report
- Dataset overview and statistics
- Missing values analysis
- Top 4 rows of filtered data
- Key insights and recommendations
- Timestamp of generation

## 🎯 Use Cases

- **Business Analytics**: Analyze sales, customer, or employee data
- **Data Exploration**: Quick insights into any CSV dataset
- **Report Generation**: Create professional PDF reports
- **Code Generation**: Get starter code for custom dashboards
- **Learning**: Understand data visualization best practices

## 🌟 Tips

1. **Upload Clean Data**: While agents can handle missing values, cleaner data = better insights
2. **Use Filters**: Combine multiple filters for deeper analysis
3. **Export Early**: Download reports before changing filters
4. **Try Different Datasets**: The agents adapt to any CSV structure

## 📞 Support

For issues or questions:
- Check the troubleshooting section
- Review the sample dataset for format reference
- Ensure all dependencies are installed

---

**Built with ❤️ using Streamlit, Plotly, and GROQ AI**
