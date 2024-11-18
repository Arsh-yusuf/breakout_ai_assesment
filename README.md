# AI Search Dashboard

## Project Description
The AI Search Dashboard is a Streamlit application that enables users to perform targeted web searches and extract key information from search results using AI-powered parsing. Key features include:
- Dataset upload and search query processing
- AI-enhanced information extraction
- Downloadable search results

## Prerequisites
- Python 3.8+
- Streamlit
- Pandas
- Requests
- BeautifulSoup
- OpenAI Python Library

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ai-search-dashboard.git
cd ai-search-dashboard
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Create requirements.txt
```
streamlit
pandas
requests
beautifulsoup4
openai
openpyxl
```

## Usage Guide

### Preparing Your Dataset
- Prepare a CSV or Excel file with search query column
- Supported file types: .csv, .xlsx

### Running the Dashboard
```bash
streamlit run app.py
```

### Dashboard Workflow
1. Upload dataset
2. Select query column
3. Enter extraction prompt
4. Provide OpenAI API Key
5. Click "Start Search"
6. View and download results

## API Keys

### OpenAI API Key
- Required for processing search results
- Enter key in dashboard interface
- Keep key confidential

### ScraperAPI Key
- Used for web scraping
- Currently hardcoded in script.py

## Troubleshooting
- Ensure stable internet connection
- Verify API key permissions
- Check dataset format

## Limitations
- Search results depend on ScraperAPI and Google
- Subject to OpenAI API rate limits
- Processing time varies with dataset size

## Contributing
Contributions welcome! Submit pull requests or open issues.
