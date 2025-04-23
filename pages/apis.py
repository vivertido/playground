import streamlit as st
import requests
import pandas as pd

st.title("API Page")

url = st.text_input("Paste URL with campus and API key")

if st.button("Fetch Campus Data"):
    try:
        data = requests.get(url).json()
        
       # st.json(data, expanded=True)   

        tab1, tab2, tab3 = st.tabs(["Overview", "Demobraphics", "Feeder Schools"])
 

        admissions = data["admissions"]
        demographics = data["demographic_totals"]
        top_feeder_schools = data["top_feeder_schools"]

        with tab1:
            # Admissions overview
            st.header(f"UC {data['university'].capitalize()} Admissions Data")
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Applied", admissions["total_applied"])
            col2.metric("Total Accepted", admissions["total_accepted"])
            col3.metric("Total Enrolled", admissions["total_enrolled"])

        with tab2:

            # Demographics
            demo_df = pd.DataFrame(demographics).T
            st.subheader("Demographics Breakdown")
            st.dataframe(demo_df)
            st.divider()
            st.bar_chart(demo_df[["applied", "admitted", "enrolled"]])

        with tab3:
            # Feeder schools
            schools_df = pd.DataFrame(top_feeder_schools)
            st.subheader("Top Feeder Schools")
            st.dataframe(schools_df)
            st.divider()
            st.bar_chart(schools_df.set_index("school")["total_enrolled"])

       

    except Exception as e:
        st.write(f"❌ Error: {e}")


