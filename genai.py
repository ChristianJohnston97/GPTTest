import openai

def extract_brief_summary(brief_input):
    command = """Analyse the brief and pull out the following key information:
                - Target audience demographic
                - Location
                - Key verticals
                - And any other critical information which is needed to build an audience to respond to the RFP """
    messages = [
        {"role": "system", "content": f"The follow is a digital advertising campaign RFP brief: {brief_input}"},
        {"role": "user", "content": command},
    ]

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo-0613", messages=messages)
    return response.choices[0].message.content


def extract_relevant_segments(segments, brief_summary):
    messages = [
        {"role": "system", "content": f"Based on the brief targeting requirement information here: {brief_summary}"},
        {"role": "system", "content": f"The follow is a list of standard segment definitions: {segments}"},
        {"role": "user", "content": """Select the segment IDs in this list which match the Target Audience Demographic 
                                       and age range and key verticals outputted in the previous step.
                                       Make sure to select all of the segment in the specified age range and then 
                                       10 segments which match the verticals closest. Return only the segment IDs 
                                       in a comma-separated list. Do not return any other text."""
         },
    ]

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo-0613", messages=messages)
    return response.choices[0].message.content