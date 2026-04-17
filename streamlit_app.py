import streamlit as st
import pandas as pd
import chardet # Add this import

st.title('st.file_uploader')
st.subheader('Input CSV')

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    # 1. Read the raw bytes from the uploaded file
    raw_data = uploaded_file.getvalue()
    
    # 2. Detect the encoding
    result = chardet.detect(raw_data)
    encoding_detected = result['encoding']
    
    # 3. Read the CSV using the detected encoding
    try:
        # We wrap the bytes in io.BytesIO so pandas can read it like a file
        import io
        df = pd.read_csv(io.BytesIO(raw_data), encoding=encoding_detected)
        
        st.success(f"Successfully loaded using {encoding_detected} encoding!")
        st.subheader('DataFrame')
        st.write(df)
        st.subheader('Descriptive Statistics')
        st.write(df.describe())
        
    except Exception as e:
        st.error(f"Even with {encoding_detected}, there was an error: {e}")
else:
    st.info('☝️ Upload a CSV file')