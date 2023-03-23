import streamlit as st
from bokeh.plotting import figure, show
from bokeh.sampledata.penguins import data
from bokeh.transform import factor_cmap, factor_mark



SPECIES = sorted(data.species.unique())
MARKERS = ['hex', 'circle_x', 'triangle']

p = figure(title = "Tamaño del Pingüino", background_fill_color="#fafafa")
p.xaxis.axis_label = 'Tamaño de la aleta(mm)'
p.yaxis.axis_label = 'Masa del cuerpo(g)'

p.scatter("flipper_length_mm", "body_mass_g", source=data,
          legend_group="species", fill_alpha=0.4, size=12,
          marker=factor_mark('species', MARKERS, SPECIES),
          color=factor_cmap('species', 'Category10_3', SPECIES))

p.legend.location = "top_left"
p.legend.title = "Species"
dataset_url = "https://allisonhorst.github.io/palmerpenguins/"
st.title('Visualizaciones del dataset [palmerpenguins](%s)' % dataset_url)

st.bokeh_chart(p, use_container_width=True)
