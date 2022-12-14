import streamlit as st
from copy import deepcopy


def streamlit_About():
    st.title(f"About")
    # TOP KPI's
    first_column, second_column, third_column = st.columns(3)
    with first_column:
        st.subheader("Objective :")
        st.markdown("""The mission is simple: Sharing knowledge with the world, 
        providing trusthworthy solutions and to enjoy""")
    with second_column:
        st.subheader("Motivation :")
        st.markdown("""Get in touch with as many geotechnical engineers, domain expertise, 
        stakeholders as possible and creating a shared network by increasing the usage of calculations presented here.""")
    with third_column:
        st.subheader("Promise :")
        st.markdown("""Saving time and decreasing errors...
        Last but not least, providing solutions for communities' needs.""")

    st.subheader("Who am i !")
    st.markdown("""I'm a geotechnical engineer passionate about Data Science and Web development. 
                When I first started working on my master degree thesis, preparing my site investigation charts was too 
                time consuming due to the absence of automated calculation & grapher tools. wich lmakes me wonder if it was possible to automate 
                all those annoying and time consuming tasks with python, So I prepared some Python scripts to overcome the time issue but 
                it has its own limits. So, I started developing simple grapher scripts and calculators to lessen the time I spend preparing 
                geotechnical reports. Later, my friends started using them too. And they liked the idea of online Grapher/calculator 
                because of its simplicity and accessibility. After that, I thought not only my Friends and I, but also any geotechnical 
                engineer or engineering student could benefit from these tools developed. So, here we are...""")
