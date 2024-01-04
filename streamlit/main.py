import streamlit as st
import requests
import json

# =========================================================================================

st.write("""

# Speech to Text: Swahili

""")


# =========================================================================================

st.write("""# """)

# =========================================================================================

# =========================================================================================

st.write("""## Upload a Swahili audio of up-to 30 seconds""")

# =========================================================================================

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()

    with open("audio.wav", 'wb') as f:
        f.write(bytes_data)

    st.audio("audio.wav")



# Button
predict_bt = st.button('Text')

st.write("""# """)

# server url
url = 'https://jayem-11-swahili-asr.hf.space/predict'  

if predict_bt:

    summary = ""

    # for file in files:
    data = {'file': open("audio.wav", 'rb')}

    response = requests.post(url, files=data)

    # Decode the byte string to string
    str_response = response.content.decode()

    # Parse the string to JSON
    json_response = json.loads(str_response)

    # Retrieve the summary content
    Text = json_response['Text'][0]

    st.write("""### Text """)
    st.success(Text)

    # Call the function
    st.balloons()

