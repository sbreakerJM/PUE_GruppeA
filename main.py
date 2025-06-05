import streamlit as st
from src.load_user_data import load_user_objects, get_person_object_from_list_by_name
from PIL import Image
import pandas as pd
import plotly.express as px



#sicherstellen, dass die Session-Variable existiert
if "current_user_name" not in st.session_state:
    st.session_state["current_user_name"] = "NONE"
if "currernt_user" not in st.session_state:
    st.session_state["current_user"] = "NONE"

FILE_PATH = "data/person_db.json"  # Replace with your actual file path
user_data = load_user_objects(FILE_PATH)
name_list = [user.get_fullname() for user in user_data]

#Eine Überschrift der ersten Ebene
st.title("EKG-APP")

#Eine Überschrift der zweiten Ebene
st.write("# Versuchsperson auswählen")

#Auswahlbox
st.session_state["current_user_name"] = st.selectbox(
    "Wählen Sie eine Versuchsperson aus",
    options = name_list, key = "sbVersuchsperson")

st.write("aktuelle Versuchsperson: ", st.session_state["current_user_name"])

st.session_state["current_user"] = get_person_object_from_list_by_name(st.session_state["current_user_name"], user_data)


#Bild mit Caption anzeigen
st.image(st.session_state["current_user"].picture_path, caption=st.session_state["current_user"].get_fullname())
st.write(st.session_state["current_user"].id)

max_hr = st.number_input(
    "Bitte gib deine maximale Herzfrequenz ein (bpm):",
    min_value=40,
    max_value=300,
    value=200,
    step=1
)

#Plotly-Graphen anzeigen mit Maximlaler Herzfrequenz aus 1_analyze_hr_data.py
from src.analyze_hr_data2 import analyze_hr_data
fig, data = analyze_hr_data(max_hr)
st.plotly_chart(fig, use_container_width=True)
st.table(data)
