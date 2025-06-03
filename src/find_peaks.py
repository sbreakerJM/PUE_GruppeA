#%% CSV einlesen und in DataFrame speichern
import pandas as pd
df_ekg = pd.read_csv("../data/ekg_data/01_Ruhe.txt", sep = "\t", names=["Voltage in [mV]", "Time in [ms]"])
df_ekg = df_ekg.iloc[0:5000]

threshold = 0.95 * df_ekg["Voltage in [mV]"].max()
min_peak_distance = 10
# %%
list_of_index_of_peaks = []
last_peaks_index = 0
for index, row in df_ekg.iterrows():
    if index < df_ekg.index.max() -1:
    #wenn row größer als das vorhegehende und das nachfolgende Element
    #dann füge den aktuellen Index der Liste hinzu
        if row["Voltage in [mV]"] >= df_ekg.iloc[index-1]["Voltage in [mV]"] and row["Voltage in [mV]"] > df_ekg.iloc[index+1]["Voltage in [mV]"]:
            
            if row["Voltage in [mV]"] > threshold and index - last_peaks_index > min_peak_distance:
                list_of_index_of_peaks.append(index)
                last_peaks_index = index
print(list_of_index_of_peaks)
# %%
#plot der row ["Voltage in [mV]"] and mark peaks with red dots

import plotly.express as plx

#make plot wider
plx.defaults.width = 1000

fig = plx.line(df_ekg, x="Time in [ms]", y="Voltage in [mV]", title="EKG Data with Peaks")
for peak in list_of_index_of_peaks:
    fig.add_scatter(x=[df_ekg.iloc[peak]["Time in [ms]"]],
                    y=[df_ekg.iloc[peak]["Voltage in [mV]"]],
                    mode='markers',
                    marker=dict(color='red', size=10),
                    name='Peak')
fig.show()
# %%
import pandas as pd

def find_peaks(df_ekg, threshold, min_peak_distance):
    list_of_index_of_peaks = []
    last_peaks_index = 0
    for index, row in df_ekg.iterrows():
        if index < df_ekg.index.max() -1:
        #wenn row größer als das vorhegehende und das nachfolgende Element
        #dann füge den aktuellen Index der Liste hinzu
            if row["Voltage in [mV]"] >= df_ekg.iloc[index-1]["Voltage in [mV]"] and row["Voltage in [mV]"] > df_ekg.iloc[index+1]["Voltage in [mV]"]:
                
                if row["Voltage in [mV]"] > threshold and index - last_peaks_index > min_peak_distance:
                    list_of_index_of_peaks.append(index)
                    last_peaks_index = index
    return list_of_index_of_peaks

#test

df_ekg = pd.read_csv("../data/ekg_data/01_Ruhe.txt", sep = "\t", names=["Voltage in [mV]", "Time in [ms]"])
df_ekg = df_ekg.iloc[0:5000]
threshold = 0.95 * df_ekg["Voltage in [mV]"].max()
min_peak_distance = 10

list_of_index_of_peaks = find_peaks(df_ekg, threshold, min_peak_distance)
# %%
import plotly.express as plx

#make plot wider
plx.defaults.width = 1000

fig = plx.line(df_ekg, x="Time in [ms]", y="Voltage in [mV]", title="EKG Data with Peaks")
for peak in list_of_index_of_peaks:
    fig.add_scatter(x=[df_ekg.iloc[peak]["Time in [ms]"]],
                    y=[df_ekg.iloc[peak]["Voltage in [mV]"]],
                    mode='markers',
                    marker=dict(color='red', size=10),
                    name='Peak')
fig.show()
