import streamlit as st

from app import logic as lg


st.title("Investigating Home Ownership in Chicago")

gdf = lg.load_zip_codes()
# st.write(gdf.to_json())
lg.interactive_chloropleth(gdf)