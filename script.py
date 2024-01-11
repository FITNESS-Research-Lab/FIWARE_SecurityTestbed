#!/usr/bin/env python3
import requests
import json
import random
import time

url = 'http://localhost:1026/ngsi-ld/v1/entities/urn:ngsi-ld:TemperatureSensor:001/attrs'
headers = {
    'Content-Type': 'application/json',
    'Link': '<http://context/ngsi-context.jsonld>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"',
    'Ngsild-Tenant': 'basetopic'
}

while True:
    # Generarte random temperature value
    temperature_value = random.randint(0, 1000)

    # Build payload
    payload = {
        "temperature": {
            "type": "Property",
            "value": temperature_value,
            "unitCode": "CEL"
        }
    }

    # Send PATCH request
    response = requests.patch(url, headers=headers, data=json.dumps(payload))

    # Print server response for debug purposes
    print(f"Temperature value sent: {temperature_value}")
    print(f"Response: {response.status_code} - {response.text}")

    # Wait 10 seconds before next request
    time.sleep(0.5)
