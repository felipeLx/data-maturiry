import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from google.oauth2 import service_account
import gspread
from utils import delete_pdfs, merge_pdfs, send_email_with_attachment
from xhtml2pdf import pisa
import os
from jinja2 import Environment, select_autoescape, FileSystemLoader

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

st.image('./logo.png', width=200)


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

# Utility function
def convert_html_to_pdf(source_html, output_filename):
    # open output file for writing (truncated binary)
    result_file = open(output_filename, "w+b")

    # convert HTML to PDF
    pisa_status = pisa.CreatePDF(
            source_html,                # the HTML to convert
            dest=result_file,           # file handle to recieve result
            options={"--print-background": True}
    )
    # close output file
    result_file.close()                 # close output file

    # return False on success and True on errors
    return pisa_status.err

for i in range(0, num_entries):
    value = "{:.0f}".format(filtered_df['Porcentagem'].iloc[i])
    text = "{:.0f}%".format(filtered_df["Porcentagem"].iloc[i])
    today = "{}".format(filtered_df["Hoje"].iloc[i])
    future = "{}".format(filtered_df["Futuro"].iloc[i])
    
    values.append(value)
    texts.append(text)
    todays.append(today)
    futures.append(future)
    
# html template
env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
template_0 = env.get_template("page01.html")
html_0 = template_0.render(
        business=business_name,
        formatted_median=formatted_median,
        value_0 = values[0],
        text_0 = texts[0],
        value_1 = values[1],
        text_1 = texts[1],
        value_2 = values[2],
        text_2 = texts[2],
        value_3 = values[3],
        text_3 = texts[3],
        value_4 = values[4],
        text_4 = texts[4],
        value_5 = values[5],
        text_5 = texts[5],
        grade=f"{filtered_df['Porcentagem'].iloc[5]}/100"
    )
pdf_0 = convert_html_to_pdf(html_0, 'pdf_0.pdf')

template_1 = env.get_template("page02.html")
html_1 = template_1.render(
        value_0 = values[0],
        text_0 = texts[0],
        today_0 = todays[0],
        future_0 = futures[0]
    )
pdf_1 = convert_html_to_pdf(html_1, 'pdf_1.pdf')

template_2 = env.get_template("page03.html")
html_2 = template_2.render(
        value_1 = values[1],
        text_1 = texts[1],
        today_1 = todays[1],
        future_1 = futures[1]
    )
pdf_2 = convert_html_to_pdf(html_2, 'pdf_2.pdf')

template_3 = env.get_template("page04.html")
html_3 = template_3.render(
        value_2 = values[2],
        text_2 = texts[2],
        today_2 = todays[2],
        future_2 = futures[2]
    )
pdf_3 = convert_html_to_pdf(html_3, 'pdf_3.pdf')

template_4 = env.get_template("page05.html")
html_4 = template_4.render(
        value_3 = values[3],
        text_3 = texts[3],
        today_3 = todays[3],
        future_3 = futures[3]
    )
pdf_4 = convert_html_to_pdf(html_4, 'pdf_4.pdf')

template_5 = env.get_template("page06.html")
html_5 = template_5.render(
        value_4 = values[4],
        text_4 = texts[4],
        today_4 = todays[4],
        future_4 = futures[4]
    )
pdf_5 = convert_html_to_pdf(html_5, 'pdf_5.pdf')

template_6 = env.get_template("page07.html")
html_6 = template_6.render(
        value_5 = values[5],
        text_5 = texts[5],
        today_5 = todays[5],
        future_5 = futures[5]
    )
pdf_6 = convert_html_to_pdf(html_6, 'pdf_6.pdf')

# Get the full path to the PDF files
list_of_pdf_templates = ['pdf_0.pdf', 'pdf_1.pdf', 'pdf_2.pdf', 'pdf_3.pdf', 'pdf_4.pdf', 'pdf_5.pdf', 'pdf_6.pdf']

# Merge PDF files
mergeHaveData = merge_pdfs(list_of_pdf_templates)

send_email_with_attachment(user_email)

st.subheader('Ao clicar para baixar o PDF iremos apagar o mesmo do servidor.')

with open('page01.html', 'r') as f:
    components.html(f.read())

with open('analise.pdf', 'r') as f:
    button_click = st.download_button('Baixar Relatório', f, file_name='analise.pdf', mime='application/pdf')  
    if button_click:
        st.balloons()
        # Delete PDF files in the current directory
        delete_pdfs(".")