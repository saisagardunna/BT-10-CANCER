import streamlit as st
from PIL import Image

from apps.home import home_page
from apps.heart import heart_page
from apps.tb import tb_page
from apps.skin import skin_page
from apps.chatbot import chat_page

from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="SkcinScan",
    page_icon="🧬",
    layout="centered",
    initial_sidebar_state="auto",
  )

pages = {
    "Home": home_page,
    "Heart Disease Prediction": heart_page,
    "Tubercolosis Detection": tb_page,
    "Skin Cancer Classification": skin_page,
    "Health Assistant": chat_page,
}

# For Horizontal Menu Layout
# selected_page = option_menu(
#         menu_title = None,
#         options = list(pages.keys()),
#         icons=['house', 'heart', 'lungs', 'person', 'robot'],
#         orientation="horizontal",
#     )

# with st.sidebar:
#     col1, col2, col3 = st.columns((1, 4, 1))
#     with col2:
#         st.image(Image.open("healthy.png"), caption="Your Health, Our Priority")
#     st.sidebar.markdown("---")

#     st.sidebar.markdown("made by [thebugged](https://github.com/thebugged)")

# For Vertical Menu Layout
with st.sidebar:
    col1, col2, col3 = st.columns((1, 4, 1))
    with col2:
        st.image(Image.open("Health.png"), caption="Your Health, Our Priority")
    st.sidebar.markdown("---")

    selected_page = option_menu(
        None,
        list(pages.keys()),
        icons=['house', 'heart', 'lungs', 'person', 'robot'],
        orientation='vertical',
    )


if selected_page in pages:
    pages[selected_page]()
else:
    st.markdown("### Invalid Page Selected")
