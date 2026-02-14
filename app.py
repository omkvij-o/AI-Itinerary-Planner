import warnings

warnings.filterwarnings("ignore") 

from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from src.core.planner import TravelPlanner
from src.utils.logger import get_logger

logger = get_logger(__name__)

st.set_page_config(page_title="AI Itinerary Planner", page_icon=":earth_asia:", layout="wide")
st.title("AI Itinerary Planner")
with st.form("planner_form"):
    city = st.text_input("Enter the city you want to visit", placeholder="e.g. Paris")
    days = st.slider("Number of days for the trip", min_value=1, max_value=30, value=5)
    interests = st.multiselect(
        "Select your interests",
        options=["Culture", "History", "Nature", "Food", "Adventure", "Relaxation"],
        default=["Culture", "Food"]
    )
    style = st.selectbox(
        "Select your travel style",
        options=["Budget", "Mid-range", "Luxury"],
        index=1
    )
    pace = st.selectbox(
        "Select your preferred pace",
        options=["Relaxed", "Moderate", "Fast-paced"],
        index=1
    )
    month = st.selectbox(
        "Select the month of travel (optional)",
        options=["Not specified"] + ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        index=0
    )
    submit_button = st.form_submit_button(label="Create Itinerary")

    if submit_button:
        planner = TravelPlanner()
        try:
            with st.spinner("Creating your itinerary..."):
                iternary = planner.create_iternary(
                    city=city,
                    days=days,
                    interests=interests,
                    style=style,
                    pace=pace,
                    month=month if month != "Not specified" else None
                )
            st.success("Itinerary created successfully!")
            st.markdown(iternary)
        except Exception as e:
            logger.error(f"Error creating itinerary: {e}")
            st.error("Failed to create itinerary. Please try again.")

