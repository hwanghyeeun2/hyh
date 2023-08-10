import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(columns=['Statutes_name','Statutes_id','Statutes_legalinterpretation','Statutes_legalproblem','Statutes_link'])

df.loc[0] = ["Employment Act 1968","15.3","The notice to terminate the service of a person who is employed under……","Employment Termination","https://sso.agc.gov.sg/act/ema1968#pr10-"]

df