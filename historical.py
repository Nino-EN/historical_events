import requests
import streamlit as st
import wikipedia

st.title('Historical events')
st.write('enter a date')

month = st.number_input('Enter the month', min_value = 1, max_value = 12, step=1)
day = st.number_input('Enter a day', min_value=1, max_value=31, step=1)


if st.button('Show events'):
    url = f'https://history.muffinlabs.com/date/{month}/{day}'
    response = requests.get(url)
    data = response.json()
    events = data['data']['Events']

    if events:
        st.subheader(f'Historical events on {month}/{day}')

        for event in events:
            st.write(f'Year: {event['year']}')
            st.write(f'Description: {event['text']}')

            if event['links']:
                st.write(f'Link: {event['links'][0]['link']}')

            results = wikipedia.search(event['text'], results = 1)
            if results:
                page = wikipedia.page(results[0])
                if page.images:
                    st.image(page.images[0], width=400)

            st.divider()

