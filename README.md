
## Digital Advertising AI-powered Sales Assistant 

### Disclaimed
THIS IS JUST A DEMO APPLICATION FOR MY OWN LEARNING AND IS INTENDED IN NO WAY TO BE COMERCIALISED.

### Video
[streamlit-about-2023-11-18-11-11-14.webm](https://github.com/ChristianJohnston97/GPTTest/assets/25692533/e0b78ac8-ed46-4545-8a26-e9c0a30b58fc)


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

### Project Goals
The goal of this project was to develop a system which would take in an RFP as input and the AI-powered tool would do 
everything else:
1. Extract key targeting requirements, demographic info, location info and keywords 
2. Use GPT-functions to make database calls to retrieve insights and key stats 
3. Generate RFP response

This shortens the time taken to create a brief response from hours to seconds.

### Technologies Used
- Python & Streamlit
- GPT4
- Postgres (via Docker)


