import streamlit as st
import requests
from models.nickname import NicknameRequest

# Page configuration
st.set_page_config(
    page_title="Nickname Maker",
    page_icon="✨",
    layout="wide"
)

# Title
st.title("✨ Nickname Maker")
st.markdown("Create your own unique nickname!")

# Input form
with st.form("nickname_form"):
    st.subheader("Enter your information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Name", placeholder="John Doe")
        age = st.number_input("Age", min_value=1, max_value=120, value=25)
    
    with col2:
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        vibe = st.text_input("Desired Vibe", placeholder="e.g., cute, cool, funny")
    
    submitted = st.form_submit_button("Generate Nickname", use_container_width=True)

# Form submission handling
if submitted:
    if not name or not vibe:
        st.error("Please enter both name and desired vibe!")
    else:
        with st.spinner("AI is generating nicknames..."):
            try:
                response = requests.post(
                    "http://localhost:8000/nickname",
                    json={
                        "name": name,
                        "age": age,
                        "gender": gender,
                        "vibe": vibe
                    }
                )
                
                if response.status_code == 200:
                    result = response.json()
                    
                    st.success("✅ Nicknames generated successfully!")
                    
                    # Display input information
                    st.subheader("📝 Input Information")
                    info_cols = st.columns(4)
                    with info_cols[0]:
                        st.metric("Name", result["input"]["name"])
                    with info_cols[1]:
                        st.metric("Age", result["input"]["age"])
                    with info_cols[2]:
                        st.metric("Gender", result["input"]["gender"])
                    with info_cols[3]:
                        st.metric("Vibe", result["input"]["vibe"])
                    
                    st.divider()
                    
                    # Display nicknames by category
                    st.subheader("🎯 Recommended Nicknames")
                    
                    for category in result["categories"]:
                        with st.expander(f"🏷️ {category['theme']}", expanded=True):
                            cols = st.columns(min(len(category["nicknames"]), 3))
                            for idx, nickname in enumerate(category["nicknames"]):
                                with cols[idx % 3]:
                                    st.markdown(f"**{nickname['name']}**")
                                    st.caption(nickname["description"])
                else:
                    st.error(f"An error occurred. (Status code: {response.status_code})")
                    
            except requests.exceptions.ConnectionError:
                st.error("⚠️ Cannot connect to FastAPI server. Please check if the server is running!")
                st.info("Start the server with `uvicorn main:app --reload` in terminal.")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

# Sidebar with usage instructions
with st.sidebar:
    st.header("📖 How to Use")
    st.markdown("""
    1. **Run FastAPI Server**
       ```bash
       uvicorn main:app --reload
       ```
    
    2. **Run Streamlit App**
       ```bash
       streamlit run app.py
       ```
    
    3. Enter your information and click **Generate Nickname**!
    """)
    
    st.divider()
    
    st.header("💡 Tips")
    st.markdown("""
    - The more specific your vibe, the better!
    - Try multiple times to find your favorite nickname
    """)
