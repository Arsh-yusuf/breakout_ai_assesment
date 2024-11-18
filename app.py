import streamlit as st
import pandas as pd
from script import perform_search, parse_results  # Updated parse_results for OpenAI

st.title("AI Search Dashboard")

# File upload section
uploaded_file = st.file_uploader("Upload your dataset", type=["csv", "xlsx"])

if uploaded_file:
    df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)
    st.write("Preview of Dataset:")
    st.dataframe(df.head())

    selected_column = st.selectbox("Select the column for queries", df.columns)

    prompt = st.text_area("Enter your extraction prompt (e.g., 'Extract the key points about AI benefits'):")

    openai_api_key = st.text_input("Enter your OpenAI API Key", type="password")

    if st.button("Start Search"):
        if not prompt or not openai_api_key:
            st.warning("Please provide both a prompt and OpenAI API key!")
        else:
            query_results = []
            print("selected column: ", selected_column)
            for query in df[selected_column]:
                raw_results = perform_search(query)
                # print("raw results: ", raw_results)
                parsed_data = parse_results(raw_results, query, openai_api_key)
                # print("parsed data: ", parsed_data)
                query_results.append({"Query": query, "Parsed Results": parsed_data})

            results_df = pd.DataFrame(query_results)
            st.write("Results:")
            st.dataframe(results_df)

            st.download_button(
                label="Download Results as CSV",
                data=results_df.to_csv(index=False),
                file_name='search_results.csv',
                mime='text/csv'
            )
