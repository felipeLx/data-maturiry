import streamlit as st
import pandas as pd
from google.oauth2 import service_account
import os
import gspread
from utils import delete_pdfs, merge_pdfs, send_email_with_attachment
from xhtml2pdf import pisa
from page01 import page01    
from page02 import page02
from page03 import page03
from page04 import page04
from page05 import page05
from page06 import page06
from page07 import page07
from page_all import page_all

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
selected_names = paramsToMatch.get('name', [])

# Reshape the dataframe
reshaped_df = pd.melt(
    df,
    id_vars=["Nome", "Cargo", "Departamento", "Email", "Empresa"],
    value_vars=[
        "1. Infraestrutura de dados",
        "2. Gestão da qualidade",
        "3. Ferramentas de análise de dados",
        "4. Análise de dados",
        "5. Gestão da informação",
        "6. Governança de dados"
    ],
    var_name="Pilar tecnologico",
    value_name="Resposta"
)

new_df = pd.merge(reshaped_df, df_pt, on="Resposta")

if len(selected_names) > 0:
    filtered_df = new_df[new_df['Nome'].isin(selected_names)]
else:
    filtered_df = new_df

# variables
filtered_df['Porcentagem'] = filtered_df['Porcentagem'].str.rstrip('%').astype(float)
pontuation_median = filtered_df['Porcentagem'].median()
business_name = filtered_df["Empresa"].values[0]
name = filtered_df["Nome"].values[0]
user_email = filtered_df["Email"].values[0]
formatted_median = "{:.0f}%".format(pontuation_median)

num_entries = 6  # You can adjust this to the number of entries you need

values = []
texts = []
todays = []
futures = []


for i in range(0, num_entries):
    value = "{:.0f}".format(filtered_df['Porcentagem'].iloc[i])
    text = "{:.0f}%".format(filtered_df["Porcentagem"].iloc[i])
    today = "{}".format(filtered_df["Hoje"].iloc[i])
    future = "{}".format(filtered_df["Futuro"].iloc[i])
    
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
logos = 'https://thumbs2.imgbox.com/0d/c8/rKvLJFpn_t.png'

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

print(page_all)
page02 = page02.replace("{{value_0}}", value_0)
page02 = page02.replace("{{text_0}}", text_0)
page02 = page02.replace("{{today_0}}", today_0)
page02 = page02.replace("{{future_0}}", future_0)
page02 = page02.replace("{{logos}}", logos)

page03 = page03.replace("{{value_1}}", value_1)
page03 = page03.replace("{{text_1}}", text_1)
page03 = page03.replace("{{today_1}}", today_1)
page03 = page03.replace("{{future_1}}", future_1)
page03 = page03.replace("{{logos}}", logos)

page04 = page04.replace("{{value_2}}", value_2)
page04 = page04.replace("{{text_2}}", text_2)
page04 = page04.replace("{{today_2}}", today_2)
page04 = page04.replace("{{future_2}}", future_2)
page04 = page04.replace("{{logos}}", logos)

page05 = page05.replace("{{value_3}}", value_3)
page05 = page05.replace("{{text_3}}", text_3)
page05 = page05.replace("{{today_3}}", today_3)
page05 = page05.replace("{{future_3}}", future_3)
page05 = page05.replace("{{logos}}", logos)

page06 = page06.replace("{{value_4}}", value_4)
page06 = page06.replace("{{text_4}}", text_4)
page06 = page06.replace("{{today_4}}", today_4)
page06 = page06.replace("{{future_4}}", future_4)
page06 = page06.replace("{{logos}}", logos)

page07 = page07.replace("{{value_5}}", value_5)
page07 = page07.replace("{{text_5}}", text_5)
page07 = page07.replace("{{today_5}}", today_5)
page07 = page07.replace("{{future_5}}", future_5)
page07 = page07.replace("{{logos}}", logos)

# Force Streamlit to re-render the HTML code
# st.experimental_rerun()

@st.cache_data
def convert_html_to_pdf(source_html, output_filename):
    if os.path.exists(output_filename):
        # Delete the output PDF file if it exists.
       os.remove(output_filename)
    # open output file for writing (truncated binary)
    result_file = open(output_filename, "w+b")

    # convert HTML to PDF
    pisa_status = pisa.CreatePDF(
            source_html,                # the HTML to convert
            dest=result_file,           # file handle to recieve result
    )
    print(pisa_status.err)
    return pisa_status.err
    

pdf_1 = convert_html_to_pdf(page01, 'page01.pdf')
pdf_2 = convert_html_to_pdf(page02, 'page02.pdf')
pdf_3 = convert_html_to_pdf(page03, 'page03.pdf')
pdf_4 = convert_html_to_pdf(page04, 'page04.pdf')
pdf_5 = convert_html_to_pdf(page05, 'page05.pdf')
pdf_6 = convert_html_to_pdf(page06, 'page06.pdf')
pdf_7 = convert_html_to_pdf(page07, 'page07.pdf')


# Get the full path to the PDF files
list_of_pdf_templates = ['page01.pdf', 'page02.pdf', 'page03.pdf', 'page04.pdf', 'page05.pdf', 'page06.pdf', 'page07.pdf']

# Merge PDF files
mergeHaveData = merge_pdfs(list_of_pdf_templates)

send_email_with_attachment(user_email)

# start streamlit page
# st.image('./logo.png', width=200)

# Display a download button
with open('analise.pdf', 'rb') as f:
  # download the PDF file
  button_click = st.download_button('Baixar Relatório', f, file_name='analise.pdf', mime='application/pdf')  
  if button_click:
    f.close()  
    st.balloons()
    # Delete PDF files in the current directory
    delete_pdfs(".")

# Display pages
st.components.v1.html(page01, height=900)
st.components.v1.html(page02, height=800)
st.components.v1.html(page03, height=800)
st.components.v1.html(page04, height=800)
st.components.v1.html(page05, height=800)
st.components.v1.html(page06, height=800)
st.components.v1.html(page07, height=800)

