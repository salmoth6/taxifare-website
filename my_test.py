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
url = 'https://taxifare.lewagon.ai/predict'

# 1. Let's ask for:
# - date and time
# - pickup longitude
# - pickup latitude
# - dropoff longitude
# - dropoff latitude
# - passenger count
# '''

pickup_datetime="2012-10-06 12:10:20"
pickup_longitude=40.7614327
pickup_latitude=-73.9798156
dropoff_longitude=40.651311
dropoff_latitude=-73.8803331
passenger_count = 2

url = 'https://taxifare.lewagon.ai/predict'

# 2. Let's build a dictionary containing the parameters for our API...
params=dict(pickup_datetime=pickup_datetime,
            pickup_longitude=pickup_longitude,
            pickup_latitude=pickup_latitude,
            dropoff_longitude=dropoff_longitude,
            dropoff_latitude=dropoff_latitude,
            passenger_count=passenger_count
            )
print (params)
# 3. Let's call our API using the `requests` package...
res=requests.get(url, params)
res=res.json()
print(res)
# 4. Let's retrieve the prediction from the **JSON** returned by the API...
fare=res['fare']
print(fare)
# 5. we can display the prediction to the user
