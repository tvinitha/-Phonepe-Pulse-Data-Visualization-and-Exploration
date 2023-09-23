# Phonepe-Pulse-Data-Visualization-and-Exploration
PhonePe-Pulse-Data-Visualization

## Problem Statement
The Phonepe pulse Github repository contains a large amount of data related to various metrics and statistics. The goal is to extract this data and process it to obtain insights and information that can be visualized in a user-friendly manner.

##  Technology Stack Used:
1. Python
2. MySQL
3. Streamlit
4. colab
5. Github Cloning
6. Geo Visualisation

## Import Libraries:
 import pandas as pd
import numpy as np
import os
import json
import mysql.connector
import streamlit as st
import plotly.express as px

## Approach:

1. Data Extraction: The data is obtained from the Phonepe pulse Github repository using scripting techniques and cloned for further processing. 
https://github.com/PhonePe/pulse.git
2. Data Transformation: Process the clone data by using Python algorithms and transform the processed data into DataFrame formate andensuring it is clean and ready for analysis.
3. Database Integration: The transformed data is inserted into a MySQL database, offering efficient storage and retrieval capabilities.
4. Live Geo Visualization Dashboard: Python's Streamlit and Plotly libraries are utilized to create an interactive and visually appealing dashboard. This dashboard presents the data in real-time, enabling users to explore the insights effectively.
5. Database Integration with the Dashboard: The relevant data is fetched from the MySQL database and seamlessly integrated into the dashboard, ensuring the displayed information is up-to-date and accurate.
6. Visualization: Finally, create a Dashboard by using Streamlit and applying selection and dropdown options on the Dashboard and show the output are Geo visualization, bar chart, and Dataframe Table
