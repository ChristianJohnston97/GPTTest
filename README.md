
## Digital Advertising AI-powered Sales Assistant 

### Disclaimer
THIS IS JUST A DEMO APPLICATION FOR MY OWN LEARNING AND IS INTENDED IN NO WAY TO BE COMERCIALISED.

### Project Goals
The goal of this project was to develop a proof-of-concept ad-sales system which would take in an RFP (see background info below) as input and the AI-powered tool would automate a number of manual tasks currently undertaken by a sales-person:
1. Extract advertiser targeting requirements, demographic info, location info and keywords from RFP
2. Dertemine relevant targeting segments (from database/file)
3. Retrieve key insights which can be used in brief response
4. Generate RFP/brief response

The goal was to develop an E2E solution in a single weekend. 

### Video
[streamlit-about-2023-11-18-11-11-14.webm](https://github.com/ChristianJohnston97/GPTTest/assets/25692533/e0b78ac8-ed46-4545-8a26-e9c0a30b58fc)

**This shortens the time taken to create a brief response from hours to seconds**

### Background
In the digital advertising industry, advertisers want to target particular users based 
on targeting requirements. For example Nike would like to target users of a certain demographic
(e.g. 18-30 males) but also users who have particular interests (e.g. `Interest | Sports | Basketball`).

The IAB (an advertising standards body) publishes these content and audience taxonomies (e.g. https://iabtechlab.com/standards/audience-taxonomy/) 
which are known as segments. Publishers are free to use these, or they can also define their own 'custom' segments, 
typically through an ad-server (e.g. GAM) or a DMP (data management platform). Then, when a user visits their site, they 
fall into one of these segments and then the publisher can monetise their ad-space in a privacy-safe way as an advertiser
can bid on one of these segments (e.g. sports lovers) without knowing the specific users personal data.

This can be done either programmatically (e.g. via an SSP/DSP) by passing this info into a bid-stream but generally the use
of custom segments requires a direct sale with an advertiser. An advertiser/agency will typically send an RFP (see an example in `resources/files/brief.txt`) 
to a number of publisher and the publisher sales team will respond with an RFP-response which will provide evidence as to why their
site is the best for the advertisers campaign. Evidence will typically incorporate how many users/impressions/clicks they have
had on their site over the past 30 days or evidence or success of previous campaigns. Publishers are trying to tell a 
data-led story about their audience, which differentiates them in-market.

This process of building evidence is typically a very labour-intensive process of pulling evidence from multiple platforms 
or BI tools and copying it into a brief response. 

### AI/GPT/LLM
Advances in AI/LLM capabilities are well suited to a task like this due their capabilities in:
- Natural language processing and data extractions
- Semantic analysis 
- Text generation capabilities 

### Technologies Used
- Python & Streamlit
- GPT4
- Postgres (via Docker)


