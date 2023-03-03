import streamlit as st
import datetime
import numpy as np
import requests

'''
# TaxiFareModel front
'''

# st.markdown('''
# Remember that there are several ways to output content into your web page...

# Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
# ''')

# '''
# ## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

# 1. Let's ask for:
# - date and time
# - pickup longitude
# - pickup latitude
# - dropoff longitude
# - dropoff latitude
# - passenger count
# '''
d = st.date_input('pickup date', datetime.date(2012, 10, 6))
t = st.time_input('pickup time', datetime.time(12, 10))
pickup_datetime=str(d)+" "+str(t)
st.write(pickup_datetime)
pickup_longitude=st.number_input('pickup_longitude',40.7614327)
pickup_latitude=st.number_input('pickup_latitude',-73.9798156)
dropoff_longitude=st.number_input('dropoff_longitude',40.651311)
dropoff_latitude=st.number_input('dropoff_latitude',-73.8803331)
passenger_count = st.selectbox('passenger count', np.arange(1,11),1)


url = 'https://taxifare.lewagon.ai/predict'

# 2. Let's build a dictionary containing the parameters for our API...
params=dict(pickup_datetime=pickup_datetime,
            pickup_longitude=pickup_longitude,
            pickup_latitude=pickup_latitude,
            dropoff_longitude=dropoff_longitude,
            dropoff_latitude=dropoff_latitude,
            passenger_count=passenger_count
            )

# 3. Let's call our API using the `requests` package...
res=requests.get(url, params).json()

# 4. Let's retrieve the prediction from the **JSON** returned by the API...
fare=res['fare']
# 5. we can display the prediction to the user
st.write("FARE:",fare)
