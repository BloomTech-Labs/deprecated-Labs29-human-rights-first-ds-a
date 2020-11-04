from fastapi import APIRouter, HTTPException
import pandas as pd
import numpy as np
import praw
from bs4 import BeautifulSoup
import re
import pickle
from newspaper import Article
# from .update import backlog_path  # Use this when able to get the backlog.csv filled correctly
from ast import literal_eval
import os
import json
import ast
import spacy
from collections import Counter
from datetime import datetime
from dotenv import load_dotenv

router = APIRouter()

@router.get('/getdata')
async def getdata():
    '''
    Get jsonified dataset from all_sources_geoed.csv
    '''

    # Path to dataset used in our endpoint
    locs_path = os.path.join(os.path.dirname(
        __file__), '..', '..', 'all_sources_geoed.csv')

    router = APIRouter()

    df = pd.read_csv(locs_path)
    # Fix issue where "Unnamed: 0" created when reading in the dataframe
    df = df.drop(columns="Unnamed: 0")

    # Removes the string type output from columns src and tags, leaving them as arrays for easier use by backend
    for i in range(len(df)):
        df['src'][i] = ast.literal_eval(df['src'][i])
        df['tags'][i] = ast.literal_eval(df['tags'][i])


    """
    Convert data to useable json format
    ### Response
    dateframe: JSON object
    """
    # Initial conversion to json - use records to jsonify by instances (rows)
    result = df.to_json(orient="records")
    # Parse the jsonified data removing instances of '\"' making it difficult for backend to collect the data
    parsed = json.loads(result.replace('\"', '"'))
    return parsed

@router.get('/getnewdata')
async def newdata():
    ''' 
    Pulling Data from reddit api
    and converting to JSON format
    for web backend
    '''
    pass
    
    

    