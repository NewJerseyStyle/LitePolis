import streamlit as st
import streamlit_authenticator as stauth

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
    pass
    # if db query st.session_state["email"] role is admin
        # st.switch_page("pages/dashboard.py")
    # else:
        # st.switch_page("pages/portal.py")
