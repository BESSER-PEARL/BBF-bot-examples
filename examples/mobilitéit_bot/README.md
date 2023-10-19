# Mobilitéit Bot
Mobilitéit Bot (similar to what the name implies) is a bot that helps the user find a possible bus or train trip in Luxembourg between two train stations or bus stops. Apart from being able to help you find a fitting public transportation trip, Mobilitéit Bot is also multilingual! 

## Pre-configuration
Before starting, a bit of pre-configuration is necessary. 

First of all, Mobilitéit Bot makes use of an open data set called "[Horaires et arrêts des transport publics (GTFS)](https://data.public.lu/en/datasets/horaires-et-arrets-des-transport-publics-gtfs/#)". You can simply download the latest ZIP file available on the page, which should be named "gtfs-TimePeriod". Note that we don't need all the datasets contained in the ZIP file, but only the one called "stops.txt". You still need to convert the "stops.txt" file to CSV format for the bot to be able to use it. 

Secondly, the Mobilitéit Bot also uses the ["API mobiliteit.lu"](https://data.public.lu/en/datasets/api-mobiliteit-lu/) to fetch the real time data of the relevant buses/trains. To give the bot the necessary rights to make these API calls, an API token is necessary. You can get the token by following the steps on the ["API mobiliteit.lu"](https://data.public.lu/en/datasets/api-mobiliteit-lu/) page. 
Once you have it, you simply need to adjust a line in the Mobilitéit Bot's code: 

```python
    payload["accessId"] = "YOUR MOBILITEIT API TOKEN HERE"
```

## Run Bot
To start, simply execute:
```bash
python ./mobiliteit_bot.py
```
You can then access your bot at http://localhost:5000.

