import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/giswqs/map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.gifer.com/embedded/download/4j.gif"
st.sidebar.image(logo)

st.title("Split-panel Map")

with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map()
        before = "https://github.com/opengeos/datasets/releases/download/raster/Libya-2023-07-01.tif"
        after = "https://github.com/opengeos/datasets/releases/download/raster/Libya-2023-09-13.tif"
        m.split_map(left_layer=before, right_layer=after)

m.to_streamlit(height=700)
