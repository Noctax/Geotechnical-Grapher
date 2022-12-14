import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import os

# Import Tools
from streamlit_Home import streamlit_Home
from streamlit_PDL import streamlit_PDL
from streamlit_PMT import streamlit_PMT
from streamlit_About import streamlit_About


# Load favicon.
images_path = os.path.join(os.path.dirname(__file__), 'images')
favicon = Image.open("%s/favicon.ico" % images_path)

# Page setup
st.set_page_config(
    page_title="Geotechnical Grapher",
    page_icon=favicon,
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---- NavBar ----
selected = option_menu(None, ["Home", "PDL Grapher", "PMT Grapher", "CPT Grapher", 'About'],
                       icons=['house', 'bi bi-graph-down-arrow', "bi bi-graph-down-arrow", "bi bi-graph-down-arrow",
                              'bi bi-info-circle'],
                       menu_icon="cast", default_index=0, orientation="horizontal")
if selected == "Home":
    streamlit_Home()
elif selected == 'PDL Grapher':
    streamlit_PDL()
elif selected == 'PMT Grapher':
    streamlit_PMT()
elif selected == 'About':
    streamlit_About()


# ---- SIDEBAR ----
SIDEBAR = st.sidebar
LOGO = Image.open("%s/logo.png" % images_path)
SIDEBAR.image(
    LOGO,
    use_column_width=True,
)
with st.sidebar:
    st.info('Created by Yettou Fares, aka [Noctax](https://twitter.com/farescrack)')
with st.sidebar:
    st.subheader("""Would you like to buy me a coffee?""")
    st.markdown("""To spend more time and to afford the expenses on this project, I could use a coffee break :)
    """)
    st.markdown("""
    <script data-name="BMC-Widget" data-cfasync="false" src="https://cdnjs.buymeacoffee.com/1.0.0/widget.prod.min.js" 
    data-id="YettouFares" data-description="Support me on Buy me a coffee!" 
    data-message="Thank you for visiting. If you want to support you can buy me a coffee." 
    data-color="#FF813F" data-position="Right" data-x_margin="18" data-y_margin="18"></script>
       """, unsafe_allow_html=True)

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)