import streamlit as st
from  PIL import Image
import numpy as np
import pandas as pd
import plotly.express as px
import io
import time
import hydralit_components as hc
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
import streamlit_authenticator as stauth
#from  PIL import ImageChops
#import plotly.express as px
import webbrowser

# streamlit_app.py


def check_password():
    """Returns `True` if the user had a correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if (
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"]
            == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store username + password
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 User not known or password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():
    st.write("Here goes your normal Streamlit app...")
    st.button("Click me")

    st.title('Tender Pipeline')
    from PIL import Image
    #logo1 = Image.open("Logos.jpg")
    #logo2 = Image.open("AMBERO_logo.jpg")
    image1 = Image.open("Downloads/FeaturedImageCFP.jpeg")
    #image2 = Image.open("homepage_agriculture__50.png")
    #image3 = Image.open("funnel.png")

    #st.image(logo1,width = 700)

    with st.sidebar:
        choose = option_menu("MENU", ["New Calls", "My Projects","My Analysis", "More"],
                             icons=['megaphone-fill', 'list-ol','stack','inboxes-fill'],
                             menu_icon="app-indicator", default_index=0,
                             styles={
            "container": {"padding": "5!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "25px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#02ab21"},
        }
        )

    if choose == "New Calls":
    #Add the cover image for the cover page. Used a little trick to center the image
        col1, col2 = st.columns( [0.8, 0.2])
        with col1:               # To display the header text using css style
            st.markdown(""" <style> .font {
            font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
            </style> """, unsafe_allow_html=True)
            st.markdown('<p class="font">New Calls</p>', unsafe_allow_html=True)


        #with col2:               # To display brand logo

            st.image(image1, width=700)
        st.subheader('Here the new calls will be displayed in a list form. ')    
        st.write("User can select the call and see all the information, including key data and details")
        df = pd.DataFrame(columns=['Project','Sector','Client','Location','Budget','Issue Date','Deadline'])
        st.table(df)
        #st.image(image1, width=700)
        st.write("xxxxx")
        st.write("xxxxx") 
        st.markdown("""---""")
        #st.image(profile, width=700 )

    elif choose == "My Projects":
        st.write("The user's project will be displayed here")
        df = pd.DataFrame(columns=['Project','Sector','Client','Location','Budget','Issue Date','Deadline'])
        st.table(df)
        #st.image(image2, width=700)
        st.markdown("""---""")
    elif choose == "My Analysis":
        st.markdown(""" <style> .font {font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">My Analysis</p>', unsafe_allow_html=True)
        st.write("Project Summary")
        container = st.container()
        container.markdown('<p class="font">Objective of the Assignment</p>', unsafe_allow_html=True)
        #st.write('outside container')
    # Now insert some more in the container
        container.markdown('<p class="font">Project requirements</p>', unsafe_allow_html=True)
        container.markdown(
    """
    Below is the project key data:
    - Name
    - Sectors
    - Client
    - Budget
    - Issue Date
    - Duration
    - Deadline time
    """
    )
        container.markdown('<p class="font">Company requirements</p>', unsafe_allow_html=True)
        container.markdown(
    """
    As a company, I must show references with/in:
    - Contract Volume
    - Technical fields
    - Location
    """
    )
        container.markdown('<p class="font">Expertise requirements</p>', unsafe_allow_html=True)
        container.markdown(
    """
    I must provide the following experts:
    - Expert 1: Team Leader
    - Expert 2: 
    - Expert 3:
    """
    )
        st.markdown("""---""")

    elif choose == "More":
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font"> 1️⃣ Anaylsis</p>', unsafe_allow_html=True)

        st.markdown('xxxxx')

        st.markdown("""---""")

        st.markdown('<p class="font"> 2️⃣ xxxx </p>', unsafe_allow_html=True)
        st.markdown('xxxxx')
        st.markdown("xxxxx")
        #st.image(image3, width = 750)


        st.markdown("""---""")

        st.markdown('<p class="font"> 3️⃣ xxxxx </p>', unsafe_allow_html=True)
        st.markdown('xxxxx ')

        #st.subheader('🔶 Module 0: Starting the training phase')
        #st.subheader("🔶 Module 1: Online training on VC concepts")
        #st.subheader('🔶 Module 2: Training on innovation process')
        #st.subheader('🔶 Module 3: Training on technical and management aspects')

        st.markdown("""---""")

        st.markdown('<p class="font"> 4️⃣ xxxxx </p>', unsafe_allow_html=True)
        st.markdown("xxxxx")

        st.markdown("""---""")
        st.markdown('<p class="font"> 5️⃣ xxxxx </p>', unsafe_allow_html=True)
        st.markdown("xxxxx")
        st.markdown("""---""")

        st.markdown('<p class="font"> 6️⃣ xxxxx </p>', unsafe_allow_html=True)
        st.markdown("xxxxxx")

    elif choose == "Contact":
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">Contact Form</p>', unsafe_allow_html=True)
        with st.form(key='columns_in_form2',clear_on_submit=True): #set clear_on_submit=True so that the form will be reset/cleared once it's submitted
            #st.write('Please help us improve!')
            Name=st.text_input(label='Please Enter Your Name') #Collect user feedback
            Email=st.text_input(label='Please Enter Your Email') #Collect user feedback
            Mobilephone= st.text_input(label='Please Enter Your Mobile phone') #Collect user feedback
            Message=st.text_input(label='Please Enter Your Message') #Collect user feedback
            submitted = st.form_submit_button('Submit')
            if submitted:
                st.write('Thanks for your contacting us. We will respond to your questions or inquiries as soon as possible!')    

    #url = "https://ee.kobotoolbox.org/x/tYuoOA2m" #url is for the platform that we collect data from participants,Kobo or Googleform
    #st.sidebar.write("[APPLY NOW](%s)" % url)

    #if st.sidebar.button('APPLY'):
        #webbrowser.open_new_tab(url)
    #st.sidebar.write("Deadline 17/05/2022")
    #st.sidebar.write("[APPLY NOW](%s)" % url)
    #if st.button('APPLY NOW'):
        #webbrowser.open_new_tab(url)
    #st.write("Deadline 17/05/2022")
    #st.markdown("[APPLY NOW](%s)" % url)

    #st.sidebar.image(logo2, width = 150)
