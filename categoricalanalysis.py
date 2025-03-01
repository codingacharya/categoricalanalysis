import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Streamlit App Title
st.title("Categorical Data Analysis")
st.write("Upload a CSV file and select a categorical column for analysis.")

# File Upload
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    # Read CSV file
    df = pd.read_csv(uploaded_file)
    st.write("## Dataset Preview")
    st.dataframe(df.head())
    
    # Select Categorical Column
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns.tolist()
    if categorical_columns:
        selected_column = st.selectbox("Select a Categorical Column", categorical_columns)
        
        if selected_column:
            st.write(f"## Analysis of {selected_column}")
            
            # Value Counts
            value_counts = df[selected_column].value_counts()
            st.write("### Value Counts")
            st.dataframe(value_counts)
            
            # Unique Values
            unique_values = df[selected_column].unique()
            st.write(f"### Unique Values ({len(unique_values)})")
            st.write(unique_values)
            
            # Bar Plot
            st.write("### Distribution Plot")
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.countplot(data=df, x=selected_column, order=value_counts.index, palette="viridis")
            plt.xticks(rotation=45)
            st.pyplot(fig)
    else:
        st.warning("No categorical columns found in the uploaded dataset.")
