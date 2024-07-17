import os
import hashlib
import base64
import json
import streamlit as st
from streamlit_cookies_controller import CookieController

import litepolis_client
from litepolis_client.models.user_profile import UserProfile
from litepolis_client.rest import ApiException

controller = CookieController()
configuration = litepolis_client.Configuration(
    host = "http://localhost:8000"
)

# login
tab1, tab2 = st.tabs(["Join conversation", "Login or register"])
# input conversation id
with tab1:
    with st.form("join_conversation"):
        b64 = st.text_input('The conversation ID#', '')
        if st.form_submit_button('Submit my picks'):
            # use client SDK access API get comments of conversation
            decoded_data = base64.b64decode(b64).decode('utf-8')
            json_data = json.loads(decoded_data)
            conversation_id = json_data.get('id')
            if conversation_id is None:
                st.error('Invalid ID')
            configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]
            configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'
            with litepolis_client.ApiClient(configuration) as api_client:
                api_instance = conversations_api.ConversationsApi(api_client)
                api_response = api_instance.get_conversation_api_v1_secure_conversations_cid_get(conversation_id)
                if api_response.status_code == 200:
                    print(api_response)
            st.session_state['conversation_id'] = conversation_id
            if controller.get('litepolis.ac.apikey'):
                st.session_state['apikey'] = controller.get('litepolis.ac.apikey')
            st.switch_page("pages/portal.py")
with tab2:
    if controller.get('litepolis.ac.apikey'):
        st.session_state['apikey'] = controller.get('litepolis.ac.apikey')
        configuration.api_key['APIKeyHeader'] = controller.get('litepolis.ac.apikey')
        configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'
        # Enter a context with an instance of the API client
        with litepolis_client.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = litepolis_client.UserApi(api_client)
            try:
                api_response = api_instance.get_userrole_api_v1_secure_users_role_get()
                if api_response["detail"]["role"] is "root":
                    st.switch_page("pages/dashboard.py")
                else:
                    st.switch_page("pages/portal.py")
            except Exception as e:
                print("Exception when calling UserApi->create_userprofile_api_v1_secure_users_profile_post: %s\n" % e)

    with st.form("login"):
        # login
        email = st.text_input('email', placeholder='email-address@domain.com')
        passwd = st.text_input('password', placeholder='********', type="password")
        # client SDK login fail
        passwd = hashlib.md5(passwd.encode()).hexdigest()
        configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]
        configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'
        with litepolis_client.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = litepolis_client.UserApi(api_client)
            user_profile = litepolis_client.UserProfile(email=email,
                                                        password=passwd)
            if st.form_submit_button('login or register'):
                try:
                    # Create Userprofile
                    api_response = api_instance.get_userauth_api_v1_secure_users_auth_post(user_profile)
                    if api_response.status_code == 200:
                        key = api_response["detail"]
                        controller.set('litepolis.ac.apikey', key)
                    elif api_response.status_code == 403:
                        # # registration
                        # passwd2 = st.text_input('Re-enter the same password',
                        #                         placeholder='********',
                        #                         type="password")
                        # if not passwd == passwd2:
                        #     st.warning('Entered two passwords not match')
                        api_response = api_instance.create_user(user_profile)
                        key = api_response["detail"]
                        controller.set('litepolis.ac.apikey', key)
                        st.session_state['apikey'] = key
                    else:
                        st.error('Wrong username or password')
                except Exception as e:
                    print("Exception when calling UserApi->create_userprofile_api_v1_secure_users_profile_post: %s\n" % e)
    
