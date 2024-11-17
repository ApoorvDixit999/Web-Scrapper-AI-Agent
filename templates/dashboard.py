import streamlit as st
import pandas as pd
from utils.web_search import search_web
from utils.hf_integration import extract_information

def run_dashboard():
    st.title("AI Agent for Web Search and Data Extraction")

    # File upload
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    
    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        st.write("Data Preview:", data.head())

        # Select the column to process
        column_name = st.selectbox("Select column with entities", data.columns)
        custom_prompt = st.text_input("Enter search prompt (e.g., 'Find the email for {company}')")

        if st.button("Run Extraction"):
            results = []
            for entity in data[column_name]:
                try:
                    # Generate search query
                    search_query = custom_prompt.format(company=entity)

                    # Perform web search
                    search_results = search_web(search_query)

                    # Combine snippets
                    combined_text = "\n".join(
                        [result["snippet"] for result in search_results if "snippet" in result]
                    )
                    if not combined_text:
                        combined_text = "No relevant text found."

                    # Extract information
                    extracted_info = extract_information(f"Extract relevant info: {combined_text}")

                    # Append results
                    results.append({"Entity": entity, "Info": extracted_info})
                
                except Exception as e:
                    results.append({"Entity": entity, "Info": "Error during extraction"})

            # Create DataFrame from results
            results_df = pd.DataFrame(results)

            # Display results as a table
            st.write("Extracted Information:")
            st.dataframe(results_df)

            # Provide download button for the CSV
            st.download_button(
                "Download Results", 
                data=results_df.to_csv(index=False), 
                mime="text/csv",
                file_name="extracted_results.csv"
            )