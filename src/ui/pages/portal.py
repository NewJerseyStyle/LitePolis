import os
import streamlit as st
import litepolis_client
from litepolis_client.api import comments_api
from litepolis_client.rest import ApiException

if 'votes' not in st.session_state:
    st.session_state.votes = {}
if 'apikey' not in st.session_state:
    apikey = os.environ["API_KEY"]
else:
    apikey = st.session_state['apikey']
configuration = litepolis_client.Configuration(
    host = "http://localhost"
)
configuration.api_key['APIKeyHeader'] = apikey
configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# RU comments
with litepolis_client.ApiClient(configuration) as api_client:
    api_instance = comments_api.CommentsApi(api_client)
    cid = st.session_state['conversation_id']
    random = True
    moderated = False
    api_response = api_instance.get_comments_api_v1_secure_comments_cid_get(
        cid, random=random, moderated=moderated)
    texts = api_response['detail']

for text in texts:
    st.write(text)
    
    # Display voting options
    agree = st.radio(f"Vote on {text}", ('Agree', 'Disagree', 'Abstain'), key=text)
    st.session_state.votes[text][st.session_state.user_id] = agree
    # on vote update to API

# C comment
# create comment
