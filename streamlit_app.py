
import streamlit as st

 
pages ={
    "Pages":
 [ 
    st.Page("pages/apis.py", title="API explorer"),
    st.Page("pages/movies.py", title="TMDB page"),
    st.Page("pages/playground.py", title="My Playground")

 ]
}

pg = st.navigation(pages)
pg.run()