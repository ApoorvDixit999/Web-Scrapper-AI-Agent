# AI Agent for Web Search and Data Extraction

This project is an **AI-driven web dashboard** built using Streamlit that combines **web search**, **data extraction**, and **natural language processing** to extract relevant information from online sources based on user-uploaded data. It allows users to upload a CSV file, input a custom search prompt, and extract meaningful insights, which can be downloaded as a CSV file.

---

## Features

1. **CSV File Upload**
   - Upload a CSV file containing entities (e.g., company names, product details, etc.).
   - Preview the uploaded data.

2. **Customizable Search Prompts**
   - Create custom prompts such as *"Find the email for {company}"* or *"Get the latest news about {entity}."*

3. **Web Search Integration**
   - Uses the SerpAPI to perform web searches for each entity in the selected column.

4. **Information Extraction**  
   - Summarizes the retrieved web search snippets using a pre-trained NLP model (`t5-small`) from Hugging Face.

5. **Data Download**  
   - Displays extracted information in a clean, interactive table.
   - Allows users to download results as a CSV file.

---

## Tech Stack

### Frontend
- **[Streamlit](https://streamlit.io/)**: A Python framework for building beautiful, interactive dashboards.

### Backend
- **Google API Client**: For integrating with Google Sheets (optional extension).  
- **SerpAPI**: For performing Google searches and retrieving organic results.  
- **Hugging Face Transformers**: For NLP summarization using the T5 model.  

### Libraries
- **pandas**: For data manipulation and handling CSV files.  
- **transformers**: For machine learning-based text summarization.  
- **torch/tensorflow**: Backend frameworks for supporting the summarization model.

---

## Installation

Follow these steps to set up and run the project:

### Prerequisites

Ensure you have Python 3.8+ installed. Install the required Python libraries:

```bash
pip install streamlit pandas google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client serpapi transformers torch torchvision torchaudio tensorflow
```

### Clone the Repository

```bash
git clone https://github.com/ApoorvDixit999/Web-Scrapper-AI-agent.git
cd ai-web-search-extraction
```

### Add API Keys

- SerpAPI Key
	•	Obtain an API key from SerpAPI.
	•	Add your key in the utils/web_search.py file:
```Python
 SERPAPI_KEY = "your_serpapi_key_here"
```
- Google API Credentials (Optional)
	•	Follow Google API instructions to set up credentials.
	•	Save the credentials file as path/to/credentials.json and update the authenticate_sheets() function in utils/google_sheets.py:
```python
flow = InstalledAppFlow.from_client_secrets_file("path/to/credentials.json", scopes=scopes)
```

### Usage

```bash
streamlit run app.py
```