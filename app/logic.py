import streamlit as st
import geopandas as gpd
import plotly.express as px

from directories import DATA_DIR


@st.cache_data
def load_zip_codes():
    gdf = gpd.read_file(DATA_DIR / "Boundaries - ZIP Codes.geojson")
    gdf.set_index("objectid", inplace=True)
    gdf = gdf.to_crs(epsg=4326)
    st.markdown("#### Zip Code Data")
    st.dataframe(gdf)
    return gdf


# @st.cache_resource
def interactive_chloropleth(_gdf):
    """
    The critical part of this plotting function turned out to be the 
    `_gdf.to_geo_dict()` call. 
    """
    fig = px.choropleth(_gdf, 
                        geojson=_gdf.to_geo_dict(), locations=_gdf.index, 
                        color="shape_area", scope="usa")
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(showlegend=False)

    st.markdown("#### Test Map")
    st.plotly_chart(fig, use_container_width=True)