# 🎯 How to Use Custom Insights Feature

## Overview
The Multi-Agent Dashboard now includes **Agent 6: Insight Customization** - a powerful AI agent that generates custom insights based on your specific questions about the data.

---

## 🚀 Quick Start Guide

### Step 1: Upload Your Dataset
1. Click "📁 Upload your CSV dataset"
2. Select any CSV file
3. Wait for Agents 1-2 to analyze the data

### Step 2: Generate Custom Insights
1. Scroll to the **"✨ Customize Your Insights with AI"** section
2. Enter your question in the text input field
3. Click the **"🚀 Generate"** button
4. Wait for Agent 6 to create your custom insights

### Step 3: View Your Insights
- Custom insights appear in a highlighted box
- Insights are saved and persist while you explore the dashboard
- They automatically update when you generate new insights

### Step 4: Download with Custom Insights
- Click **"📄 Download dashboard.py"** - includes your insights in the code
- Click **"📑 Download PDF Report"** - includes your insights in the report
- Both downloads reflect your latest custom insights

---

## 💡 Example Prompts

### For Employee Data:
- "What are the key salary trends by department?"
- "Identify any performance rating outliers"
- "Which cities have the highest average salaries?"
- "Analyze the relationship between experience and salary"
- "Find patterns in project count distribution"

### For Sales Data:
- "What are the top-performing products?"
- "Identify seasonal trends in sales"
- "Which regions show declining performance?"
- "Analyze customer segmentation patterns"

### For General Data:
- "Summarize the most important findings"
- "What anomalies exist in the data?"
- "Identify correlations between key features"
- "What recommendations would you make?"

---

## 🎨 Features

### ✅ Real-Time Generation
- Insights generated in seconds using GROQ AI
- No page refresh needed
- Smooth loading animation

### ✅ Persistent Storage
- Insights saved in session
- Remain visible as you explore
- Update only when you generate new ones

### ✅ Integrated Exports
- **PDF Reports**: Custom insights appear in dedicated section
- **Python Code**: Insights embedded as comments/info boxes
- Both downloads always include latest insights

### ✅ Smart Context
Agent 6 has access to:
- Dataset dimensions and structure
- Column names and types
- Summary statistics
- Missing value information
- Your specific question

---

## 📊 How It Works

```
User enters prompt
        ↓
Agent 6 analyzes dataset context
        ↓
GROQ AI generates insights
        ↓
Insights displayed on dashboard
        ↓
Insights included in downloads
```

---

## 🔧 Technical Details

### AI Model
- **Model**: Llama 3 8B (via GROQ)
- **Temperature**: 0.7 (balanced creativity)
- **Max Tokens**: 500 (detailed responses)

### Context Provided
```python
- Total Rows
- Total Columns  
- Numeric Columns (names)
- Categorical Columns (names)
- Missing Values count
- Summary Statistics
- User's specific question
```

### Fallback Behavior
- If API fails, uses fallback insights
- Dashboard continues to work normally
- Warning message displayed

---

## 📥 Download Integration

### dashboard.py File
Custom insights appear at the top:
```python
# Custom Insights
st.header("🎯 Custom Insights")
st.info("""Your custom insights here...""")
```

### PDF Report
Custom insights in dedicated section:
- **Section**: "Custom Insights"
- **Position**: After title, before dataset overview
- **Formatting**: Multi-line text with proper wrapping

---

## 🎯 Best Practices

### ✅ DO:
- Be specific in your prompts
- Ask about relationships between features
- Request actionable recommendations
- Use domain-specific terminology

### ❌ DON'T:
- Ask overly broad questions
- Request insights about columns that don't exist
- Expect insights without uploading data first

---

## 🔄 Workflow Example

1. **Upload** `sample_data.csv`
2. **Review** Agent 1 & 2 automatic insights
3. **Enter prompt**: "What factors influence high salaries?"
4. **Click** "🚀 Generate"
5. **Read** custom insights from Agent 6
6. **Apply filters** to explore specific segments
7. **Download** PDF with insights included
8. **Download** dashboard.py with insights embedded

---

## 💾 Session Management

### Insights Persistence
- Stored in `st.session_state`
- Survives filter changes
- Survives visualization interactions
- Cleared on page refresh or new file upload

### Updating Insights
- Enter new prompt
- Click "🚀 Generate" again
- Old insights replaced with new ones
- Downloads always use latest insights

---

## 🎨 UI Elements

### Input Field
- **Placeholder**: Example prompts
- **Width**: 80% of screen
- **Position**: Before visualizations

### Generate Button
- **Style**: Purple gradient
- **Icon**: 🚀 rocket
- **Hover**: Scale + shadow effect

### Insights Display
- **Background**: Gradient (aqua to pink)
- **Border**: Left purple accent
- **Animation**: Slide-in effect
- **Typography**: Clear, readable

---

## 🚀 Advanced Usage

### Multiple Insights
Generate insights for different aspects:
1. "Overall data quality assessment"
2. "Key trends in numeric features"
3. "Categorical distribution patterns"
4. "Recommendations for action"

### Combining with Filters
1. Apply filters (e.g., Engineering department)
2. Generate insights about filtered data
3. Insights reflect filtered subset
4. Download filtered insights

---

## 🔒 Privacy & Security

- All processing uses GROQ API
- No data stored on servers
- API key secured in .env file
- Insights generated on-demand
- No persistent storage of insights

---

## 📞 Troubleshooting

### Issue: "Using fallback insights"
**Cause**: API connection failed
**Solution**: Check internet connection, verify API key

### Issue: Insights not updating
**Cause**: Button not clicked after entering prompt
**Solution**: Click "🚀 Generate" button

### Issue: Insights missing from downloads
**Cause**: No insights generated yet
**Solution**: Generate insights before downloading

---

## ✨ Summary

**Agent 6** transforms your dashboard from static analysis to **interactive intelligence**:
- Ask specific questions
- Get AI-powered answers
- Export insights automatically
- Make data-driven decisions faster

**Try it now with the sample dataset!**

Example: "What are the salary trends across different departments and cities?"
