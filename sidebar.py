import streamlit as st


def renderSidebarInfo():
    st.sidebar.write("""
    # Process
    #### 1. Upload an advertiser/agency RFP brief
    #### 2. Select the segments you would like to generate insights for
    #### 3. Apply filters
    #### 4. Generate brief response
    #### 5. Send to advertiser
    """)


def renderSidebarFilters(selectedRegions):
    st.sidebar.markdown("""---""")
    st.sidebar.header("Apply filters")

    region = st.sidebar.multiselect(
        "Select Region",
        ["USA", "ENG", "FRA", "IRE"],
        selectedRegions
    )
    location = st.sidebar.multiselect(
        "Select Browser",
        ["Chrome", "Safari", "Internet Explorer"],
        []
    )

    platform = st.sidebar.multiselect(
        "Select Platform",
        ["Web", "Android", "IOS"],
        []
    )

    segments = st.sidebar.multiselect("Select segments",
                                      ["age_21-24", "age_25-29", "age_30-34", "age_35-39", "age_40-44",
                                       "interest_sports_baseball", "interest_sports_basketball",
                                       "interest_sports_cricket", "segment1", "segment2", "segment3"],
                                      ["age_21-24", "age_25-29", "age_30-34", "age_35-39", "age_40-44",
                                       "interest_sports_baseball", "interest_sports_basketball",
                                       "interest_sports_cricket"])
    return segments
