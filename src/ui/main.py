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
        st.text_input('The conversation ID#', '')
        if st.form_submit_button('Submit my picks'):
            # use client SDK access API get comments of conversation
            litepolis_client.ConversationApi.
            st.switch_page("pages/portal.py")
with tab2:
    if controller.get('litepolis.ac.apikey'):
        pass # use client SDK
        configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]
        configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

########## need to re-gen the SDK
# Enter a context with an instance of the API client
with litepolis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = litepolis_client.UserApi(api_client)
    user_profile = litepolis_client.UserProfile() # UserProfile | 

    try:
        # Create Userprofile
        api_response = api_instance.create_userprofile_api_v1_secure_users_profile_post(user_profile)
        print("The response of UserApi->create_userprofile_api_v1_secure_users_profile_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->create_userprofile_api_v1_secure_users_profile_post: %s\n" % e)
########## need to re-gen the SDK before procceed

        # if db query st.session_state["email"] role is "root":
        #     st.switch_page("pages/dashboard.py")
        # else:
        #     st.switch_page("pages/portal.py")
    with st.form("login"):
        # login
        email = st.text_input('email', 'email-address@domain.com')
        passwd = st.text_input('password', '********', type="password")
        # client SDK login fail
        key = "" #litepolis_client.UserApi.verify return detail
        if key is None:
            # registration
            # ask for type again password + 1username
        else:
            controller.set('litepolis.ac.apikey', key)
