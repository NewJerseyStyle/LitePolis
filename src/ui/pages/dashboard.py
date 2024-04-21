import streamlit as st
import streamlit_authenticator as stauth

if st.session_state["authentication_status"]:
    # C conversation
    if st.button('New conversation'):
        with st.form("my_form"):
            st.write("Inside the form")
            checkbox_val = st.checkbox("Form checkbox")
            if st.form_submit_button("Submit"):
                # API create conversation

    tab1, tab2 = st.tabs(["Conversation & comments", "Users"])
    with tab1:
        # list of conversations from API
        for conversation in conversations:
            with st.container():
                st.subheader(conversation.title)
                st.write(conversation.desc)
                # no of user involved
                if st.button('Show deatils'):
                    # RUD conversation
                    pass
    # U (moderate) comments

    with tab2:
    # CRUD users
