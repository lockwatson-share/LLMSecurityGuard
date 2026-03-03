import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import streamlit as st
from manual_review.manual_review import get_queue

st.title("LLMSecurityGuard Dashboard")

st.subheader("Pending Manual Review Queue")
queue = get_queue()
if queue:
    for idx, item in enumerate(queue, 1):
        st.write(f"**{idx}. User:** {item['user']}")
        st.write(f"Prompt: {item['prompt']}")
        st.write(f"Risk Score: {item['risk_score']}")
        st.write(f"Provider: {item['provider']}")
        st.write("---")
else:
    st.write("No items pending review.")