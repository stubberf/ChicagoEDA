import os
import time

from dotenv import load_dotenv
import pandas as pd
from urllib.parse import quote
import requests
from tqdm import tqdm

from census_column_codes import COLUMN_CODES


load_dotenv()


class Census:
    def __init__(self):
        self.api_key = os.environ["CENSUS_API_KEY"]
        self.max_code_chunk = 49
        self.base_url = "https://api.census.gov/data"


    def download(self, datasets=['acs/acs5/profile', 'acs/acs5'],
                    years=[2022], 
                    zip_codes=['60620', '60652', '60643']):
        """
        Download as a CSV the following datasets from the specified years and
        zip codes.
        """
        results = {}
        for dataset in datasets:
            yearly_dataframes = []
            
            for year in years:
                chunk_results = pd.DataFrame(columns=['NAME'])

                codes = COLUMN_CODES[dataset]
                codes = list(codes.values())

                desc = f"Downloading Dataset {dataset} for {year}..."
                _range = range(0, len(codes), self.max_code_chunk)
                for ii in tqdm(_range, desc=desc):
                    codes_subset = ["NAME"] + codes[ii:ii+self.max_code_chunk]

                    # Construct API request
                    location = "zip code tabulation area:" + ','.join(zip_codes)
                    url_vars = ','.join(codes_subset)
                    url = f"{self.base_url}/{year}/{dataset}?get={url_vars}&for={location}&key={self.api_key}"
                    encoded_url = quote(url, safe=':/?=&')

                    # Send API request and convert response to dataframe
                    response = requests.get(encoded_url)
                    df_response = pd.DataFrame(response.json()[1:], columns=response.json()[0])
                    chunk_results = pd.merge(chunk_results, df_response, how='outer')
                    
                    # Sleep for 1/4 sec to avoid rate limits
                    time.sleep(0.25)

                # Add the results of each year to list
                chunk_results.insert(0, 'Year', year)
                yearly_dataframes.append(chunk_results)

            # Combine all of the data into one Pandas Table
            results[dataset] = pd.concat(yearly_dataframes, axis=0)

        return results