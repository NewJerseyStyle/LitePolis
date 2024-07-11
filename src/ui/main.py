import streamlit as st
from streamlit_cookies_controller import CookieController

controller = CookieController()

# login
tab1, tab2 = st.tabs(["Join conversation", "Login or register"])
# input conversation id
with tab1:
    with st.form("join_conversation"):
        st.text_input('The conversation ID#', '')
        if st.form_submit_button('Submit my picks'):
            # use client SDK access API get comments of conversation
            st.switch_page("pages/portal.py")
with tab2:
    if controller.get('litepolis.ac.apikey'):
        pass # use client SDK
        # if db query st.session_state["email"] role is "root":
        #     st.switch_page("pages/dashboard.py")
        # else:
        #     st.switch_page("pages/portal.py")
    with st.form("login"):
        # login
        email = st.text_input('email', 'email-address@domain.com')
        email = st.text_input('password', '********', type="password")
        # client SDK login fail
        # registration
        # if no such email, ask for 2password + 1username
        # except Exception as e:
        #     st.error(e)
        
        controller.set('litepolis.ac.apikey', 'key')
