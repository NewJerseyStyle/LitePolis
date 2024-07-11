import streamlit as st
import streamlit_authenticator as stauth

st.write(
    st.session_state["teset"])
st.write(
    st.session_state["wow"])

if "teset" not in st.session_state:
    st.session_state["teset"] = 1
st.session_state["teset"] += 1

# login
tab1, tab2 = st.tabs(["Join conversation", "Login"])
# input conversation id
with tab1:
    with st.form("join_conversation"):
        st.text_input('The conversation ID#', '')
        if st.form_submit_button('Submit my picks'):
            # use client SDK access API get comments of conversation
            st.switch_page("pages/portal.py")
with tab2:
    # config from yaml loads (db query
    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['pre-authorized']
    )
    # login
    authenticator.login()
    # registration
    try:
        email, _, _ = authenticator.register_user(
          pre_authorization=False,
          fields={
            'Form name':'Register or Reset password',
            'Email':'Email',
            # 'Username':'Username',
            'Password':'Password',
            'Repeat password':'Repeat password',
            'Register':'Register'})
        if email:
            st.success('User registered successfully')
    except Exception as e:
        st.error(e)
    
    if st.session_state["authentication_status"]:
        if db query st.session_state["email"] role is "root":
            st.switch_page("pages/dashboard.py")
        else:
            st.switch_page("pages/portal.py")
