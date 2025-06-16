import streamlit as st
from src.load_user_data import load_user_objects, get_person_object_from_list_by_name
from src.ekg_data import Ekg_tests
from PIL import Image
import pandas as pd
import plotly.express as px
from src.analyze_hr_data2 import analyze_hr_data

#sicherstellen, dass die Session-Variable existiert
if "current_user_name" not in st.session_state:
    st.session_state["current_user_name"] = None
if "currernt_user" not in st.session_state:
    st.session_state["current_user"] = None
if "Ekg_data" not in st.session_state:
    st.session_state["Ekg_data"] = None

FILE_PATH = "data/person_db.json"
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


#gibt Bild, ID, Alter und Maximale Herzfrequenz der Versuchsperson aus

st.image(st.session_state["current_user"].picture_path, caption=st.session_state["current_user"].get_fullname())
st.write("ID: ", st.session_state["current_user"].id)
st.write("Alter der Versuchsperson:", st.session_state["current_user"].calc_age(), "Jahre")
st.write("Maximale Herzfrequenz laut Berechnung wäre:", st.session_state["current_user"].calc_max_heart_rate(), "bpm")

#Auswahl der maximalen Herzfrequenz
max_hr = st.number_input(
    "Bitte gib deine maximale Herzfrequenz ein (bpm):",
    min_value=40,
    max_value=300,
    value=200,
    step=1
)

#Asugabe der Analyse der Herzfrequenzdaten
 
fig, data = analyze_hr_data(max_hr)
st.plotly_chart(fig, use_container_width=True)
st.table(data)

person = st.session_state["current_user"]
ekg_info = person.ekg_tests[0]  # z. B. das erste EKG auswählen

st.session_state["Ekg_data"] = Ekg_tests(
    id = person.id,
    date = ekg_info["date"],
    result_link = ekg_info["result_link"]
)

st.session_state["Ekg_data"].find_peaks()
st.session_state["Ekg_data"].estimate_hr()
st.session_state["Ekg_data"].plot_time_series()

fig1 = st.session_state["Ekg_data"].plot_time_series()
st.plotly_chart(fig1, use_container_width=True)


ekg_test = st.session_state["Ekg_data"]


## Ausgabe der berechneten Herzfrequenz-Werte
st.write("## Berechnete Herzfrequenz-Werte (bpm)")

hr_df = pd.DataFrame({
    "Peak-Nr": list(range(1, len(ekg_test.hr) + 1)),
    "Herzfrequenz (bpm)": ekg_test.hr
})

avg_hr = sum(ekg_test.hr) / len(ekg_test.hr)
st.write(f"Durchschnittliche Herzfrequenz: **{round(avg_hr, 2)} bpm**")