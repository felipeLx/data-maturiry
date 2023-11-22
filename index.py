import streamlit as st
import pandas as pd
from google.oauth2 import service_account
import gspread
from utils import send_email_with_attachment
from page_all import page_all
import re

# App config
st.set_page_config(page_title="Data maturity report", page_icon="./favicon.ico", layout="centered", initial_sidebar_state="collapsed", menu_items=None)

# Global variables
data = ''

credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
        scopes=[
            "https://www.googleapis.com/auth/spreadsheets",
        ],
)
client = gspread.authorize(credentials)

# Open the Google Sheet by its URL
sheet = client.open_by_url(st.secrets["private_gsheets_url"])
pontuation_sheet = client.open_by_url(st.secrets["gsheets_url_mat"])

# Access a specific worksheet
worksheet = sheet.get_worksheet(0)
pt_worksheet = pontuation_sheet.get_worksheet(0)

# Fetch data
data = worksheet.get_all_values()
df = pd.DataFrame(data[1:], columns=data[0])

pt_data = pt_worksheet.get_all_values()
df_pt = pd.DataFrame(pt_data[1:], columns=pt_data[0])

# Create params
paramsToMatch = st.experimental_get_query_params()
selected_names = paramsToMatch.get('phone', [])

# Reshape the dataframe
reshaped_df = pd.melt(
    df,
    id_vars=["Nome", "Cargo", "Departamento", "Email", "Empresa", "Telefone"],
    value_vars=[
        "1. Infraestrutura de dados",
        "2. Gestão da qualidade",
        "3. Ferramentas de análise de dados",
        "4. Análise de dados",
        "5. Gestão da informação",
        "6. Governança de dados"
    ],
    var_name="Pilar tecnológico",
    value_name="Resposta"
)

reshaped_df['Resposta'] = reshaped_df['Resposta'].str.replace(' ', '')
df_pt["Resposta"] = df_pt["Resposta"].str.replace(' ', '')
reshaped_df['Merged'] = reshaped_df["Pilar tecnológico"] + " - " + reshaped_df["Resposta"]
df_pt['Merged'] = df_pt["Pilar tecnológico"] + " - " + df_pt["Resposta"]
reshaped_df['Phone'] = reshaped_df['Telefone'].str.replace('-', '')

# new_df = pd.concat([reshaped_df, df_pt], axis=1, sort=False)
# new_df = reshaped_df.merge(df_pt, how="left", on="Merged")
new_df = reshaped_df.merge(df_pt, on="Resposta", how="left")
print('new_df', new_df.info())
paramsPhone = [re.sub(r'[^0-9]', '', phone) for phone in selected_names] 

if len(selected_names) > 0:
    print('more than 0 len')
    new_df = new_df[new_df['Phone'].isin(paramsPhone)]
    print('new_df', new_df.info())
else:
    st.text('O número não foi encontrado.')

# variables
new_df['Porcentagem'] = new_df['Porcentagem'].str.rstrip('%').astype(float)
pontuation_median = new_df['Porcentagem'].median()
business_name = new_df["Empresa"].values[0]
name = new_df["Nome"].values[0]
user_email = new_df["Email"].values[0]
formatted_median = "{:.0f}%".format(pontuation_median)

num_entries = 6  # The number of questions that the user will answer

values = []
texts = []
todays = []
futures = []


for i in range(0, num_entries):
    value = "{:.0f}".format(new_df['Porcentagem'].iloc[i])
    text = "{:.0f}%".format(new_df["Porcentagem"].iloc[i])
    today = "{}".format(new_df["Hoje"].iloc[i])
    future = "{}".format(new_df["Futuro"].iloc[i])
    
    values.append(value)
    texts.append(text)
    todays.append(today)
    futures.append(future)

# Create variables that will be used in the template
business=business_name
formatted_median=formatted_median
value_0 = values[0]
text_0 = texts[0]
today_0 = todays[0]
future_0 = futures[0]
value_1 = values[1]
text_1 = texts[1]
today_1 = todays[1]
future_1 = futures[1]
value_2 = values[2]
text_2 = texts[2]
today_2 = todays[2]
future_2 = futures[2]
value_3 = values[3]
text_3 = texts[3]
today_3 = todays[3]
future_3 = futures[3]
value_4 = values[4]
text_4 = texts[4]
today_4 = todays[4]
future_4 = futures[4]
value_5 = values[5]
text_5 = texts[5]
today_5 = todays[5]
future_5 = futures[5]
logos = 'fundo_v2.png'

# Replacing values of the pages
page_all = page_all.replace("{{business}}", business)
page_all = page_all.replace("{{formatted_median}}", formatted_median)
page_all = page_all.replace("{{value_0}}", value_0)
page_all = page_all.replace("{{text_0}}", text_0)
page_all = page_all.replace("{{value_1}}", value_1)
page_all = page_all.replace("{{text_1}}", text_1)
page_all = page_all.replace("{{value_2}}", value_2)
page_all = page_all.replace("{{text_2}}", text_2)
page_all = page_all.replace("{{value_3}}", value_3)
page_all = page_all.replace("{{text_3}}", text_3)
page_all = page_all.replace("{{value_4}}", value_4)
page_all = page_all.replace("{{text_4}}", text_4)
page_all = page_all.replace("{{value_5}}", value_5)
page_all = page_all.replace("{{text_5}}", text_5)
page_all = page_all.replace("{{logos}}", logos)
page_all = page_all.replace("{{today_0}}", today_0)
page_all = page_all.replace("{{future_0}}", future_0)
page_all = page_all.replace("{{today_1}}", today_1)
page_all = page_all.replace("{{future_1}}", future_1)
page_all = page_all.replace("{{today_2}}", today_2)
page_all = page_all.replace("{{future_2}}", future_2)
page_all = page_all.replace("{{today_3}}", today_3)
page_all = page_all.replace("{{future_3}}", future_3)
page_all = page_all.replace("{{today_4}}", today_4)
page_all = page_all.replace("{{future_4}}", future_4)
page_all = page_all.replace("{{today_5}}", today_5)
page_all = page_all.replace("{{future_5}}", future_5)

# send_email_with_attachment(user_email, page_all)
st.download_button(label='Baixar', data=page_all, file_name='page_all.html')
st.components.v1.html(page_all, height=8000)

