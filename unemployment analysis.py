import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

unemp_data = pd.read_csv('/content/drive/MyDrive/Unemployment in India.csv')

unemp_data.head()

unemp_data.isnull().sum()

unemp_data.info()

sns.heatmap(unemp_data.corr(), annot = True)
plt.show()

b = px.bar(unemp_data, x='Area', y = ' Estimated Unemployment Rate (%)')
b.show()

bp = px.box(unemp_data, x = 'Region', y = ' Estimated Unemployment Rate (%)', color = 'Area', template = 'plotly')
bp.update_layout(xaxis = {'categoryorder': 'total descending'})
bp.show()

bp1 = px.box(unemp_data, x = 'Region', y = ' Estimated Unemployment Rate (%)', color = 'Region', template = 'plotly')
bp1.update_layout(xaxis = {'categoryorder': 'total descending'})
bp1.show()

h = px.histogram(unemp_data, x = 'Region', y = ' Estimated Unemployment Rate (%)', color = 'Area', template = 'plotly')
h.update_layout(xaxis = {'categoryorder': 'total descending'})
h.show()

h = px.histogram(unemp_data, x = 'Region', y = ' Estimated Unemployment Rate (%)', color = 'Region', template = 'plotly')
h.update_layout(xaxis = {'categoryorder': 'total descending'})
h.show()
