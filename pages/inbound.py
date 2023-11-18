import time
from io import StringIO
import matplotlib.pyplot as plt

import streamlit as st

from mockdata import demographicSegments, generateInsightsDf, getUsersForSegments, interestSegments
from sidebar import renderSidebarInfo, renderSidebarFilters


def displaySegmentsMetadataDf(df):
    st.dataframe(
        df,
        column_config={
            "Name": "Segment Name",
            "Description": "Segment Description",
            "FirstParty": st.column_config.CheckboxColumn(
                "Is First Party",
                disabled=True,
            ),
            "Users": st.column_config.LineChartColumn(
                "Users (last 30 days)", y_min=0, y_max=5000, width="large"
            ),
            "Total": "Total users (last 30 days)"
        },
        use_container_width=True,
        hide_index=True,
    )


def get_segment_users_for_campaign(segments_list):
    conn = st.connection("postgresql", type="sql")
    segments_array = ','.join(str(v) for v in segments_list)
    sql_query = "SELECT segment_id, users FROM campaign_performance where segment_id in (%s)" % segments_array
    df = conn.query(sql_query)
    return df


def extract_file_contents(uploaded_file):
    bytes_data = uploaded_file.getvalue()
    stringio = StringIO(bytes_data.decode("utf-8"))
    return stringio.read()


@st.cache_resource
def extractSegmentsFromFile(uploaded_file):
    _ = extract_file_contents(uploaded_file)
    with st.spinner('Generating insights...'):
        # mocking querying of relevant segments and basic high level insights
        time.sleep(3)
        return ['segment1', 'segment2', 'segment3']


# Main Header and config
st.set_page_config(layout="wide")
# Styling
with open('style.css') as f:
    st.markdown(f"""<style>{f.read()}</style>""", unsafe_allow_html=True)

renderSidebarInfo()

st.write("""### Upload your digital advertiser RFP brief here... """)
uploaded_file = st.file_uploader("")
if uploaded_file is not None:
    extractedSegments = extractSegmentsFromFile(uploaded_file)
    st.divider()
    st.subheader("Extracted key information")
    st.markdown(
        """
        - **Gender**: Male
        - **Age**: 18-45
        - **Interests**: Sports enthusiasts, athletes, particularly those interested in ball sports
        - **Location**: United Kingdom (UK)
        - **Ad Formats**: Display, video, native ads
        - **Keywords**: sports, ball sports, sports enthusiasts, lifestyle
        - **Budget**: $2 million
        """
    )

    st.divider()
    st.subheader("Suggested demographic segments")
    displaySegmentsMetadataDf(demographicSegments)

    # set select regions (based off RPF input)- hard-coded for now 
    if 'selectedRegions' not in st.session_state:
        st.session_state['selectedRegions'] = ["ENG"]
    selectedRegions = st.session_state['selectedRegions']

    selectedSegments = renderSidebarFilters(selectedRegions)

    st.subheader("Suggested interest segments")
    displaySegmentsMetadataDf(interestSegments)

    st.subheader("Suggested domains")
    st.markdown(
        """
        - Rugby.com
        - Football.com
        - Cricket.com
        - Golf.com
        - Tennis.com
        """
    )

    st.divider()

    # select segments
    st.subheader("Aggregated Insights")
    segmentData = getUsersForSegments(extractedSegments)
    totalUsers = sum(list(segmentData.values()))

    st.line_chart(generateInsightsDf(selectedSegments))

    total1, total2, total3, total4 = st.columns(4, gap='large')
    with total1:
        st.info('Total Users', icon="📌")
        st.metric(label="", value=totalUsers)

    with total2:
        st.info('Total Impressions', icon="📌")
        st.metric(label="", value=totalUsers)

    with total3:
        st.info('Total Clicks', icon="📌")
        st.metric(label="", value=totalUsers)

    with total4:
        st.info('Total Revenue ($)', icon="📌")
        st.metric(label="", value=totalUsers)

    total1, total2, total3, total4 = st.columns(4, gap='small')
    with total1:
        st.info('Average Session Length', icon="📌")
        labels = '<5s', '5-30s', '30-60s', '60-90s'
        sizes = [15, 30, 45, 10]
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')
        st.pyplot(fig1)

    st.divider()
    st.subheader("Activation ")

    generateRfpResponse = st.button("Generate RFP response", type="primary")
    if generateRfpResponse:
        st.markdown('''
        Our :red[Sports Enthusiasts] constantly seek out the latest scores and updates for their teams and look to the 
        our publication to know which events are coming up and who's on top for the season. As one of our most 
        hyper-engaged audiences, our Sports Enthusiasts average :red[10 pageviews] each per month and avidly engage with the [your publication].
        Regularly reading both at their desks and on the go, this audience engages with a wide range of content, 
        spanning from Premier League football to Grand Prix Racing. As hyper-engaged  Sports Enthusiasts, 
        this audience is actively seeking to buy their favorite team's apparel, the best athletic tech, 
        and equipment that the Sports Enthusiasts market has to offer''')

