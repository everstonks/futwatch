import requests, os, subprocess
import pandas as pd
from bs4 import BeautifulSoup

page = 0

url = ('https://www.goal.com/br/not%C3%ADcias/programacao-partidas-futebol-tv-aberta-fechada-onde-assistir/1jf3cuk3yh5uz18j0s89y5od6w/')
j = requests.get(url)

soup = BeautifulSoup(j.content, 'html.parser')

data = []

jogos = soup.find("div", class_="body")
tables = jogos.find_all("table")
table = tables[page]
head = table.find_all('tr', class_="tableizer-firstrow")
rows = table.find_all('tr', attrs={'class': None})

dia = soup.find("h2").a.get("name").upper()
if page == 1:
  dia = subprocess.check_output(['date','+%A']).decode('utf-8').replace('\n','').upper()
elif page == 2:
  dia = subprocess.check_output(['date','-d','+1 days','+%A']).decode('utf-8').replace('\n','').upper()

for row in rows:
  data.append(row)

body = (str(data).replace('[','').replace(']',''))
tabela = ("<table><thead><th colspan=5>&zwnj;</th></thead><thead>"+str(head).replace('[','').replace(']','')+"</thead>"+"<tbody>"+body+"</tbody>"+"</table>")

df_lista = pd.read_html(tabela)
df = df_lista[0]
df.drop(columns = [('\u200c', 'INTERNET')], inplace = True)
xyz = df.loc[(df['\u200c', 'CAMPEONATO'] == 'Paulistão A2') | (df['\u200c', 'CAMPEONATO'] == 'Paulistão A3')]
df = df.drop(xyz.index)
df = df.style.set_table_styles(
    [{'selector':'td', 'props':[('color','#0f0d03'), ('font-weight','normal'), ('font-size','15px'), ('text-align','justify'), ('padding','10px')]}, 
     {'selector':'tr', 'props':[('border-bottom','1px solid black')]},
     {'selector':'tr:nth-of-type(odd)', 'props':[('color','white'),('font-size','22px')]}, 
     {'selector':'tr:nth-of-type(even)', 'props':[('background','#0f0d03'),('color','white')]},
     {'selector':'tbody tr:nth-of-type(even)', 'props':[('background','#f3f3f3')]},
     ]).hide_index()
df_html = df.render()
x = df_html.replace('colspan="4">','colspan=4 id="thdia"><center>'+dia+'</center><small><i class="fa fa-twitter"></i> <i class="fa fa-instagram"></i> <i class="fa fa-youtube-play"></i> <i class="fa fa-facebook"> @goal</i></small>').replace('<style type="text/css">','<head><meta charset="utf-8"><meta name="viewport" content="width-device, initial-scale=1"><link rel="preconnect" href="https://fonts.gstatic.com"><link href="https://fonts.googleapis.com/css2?family=Titillium+Web:wght@400;600&display=swap" rel="stylesheet"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"></head><style type="text/css">#thdia {background: #000000} table{font-family: Titillium Web, sans-serif; border-collapse: collapse; box-shadow: 0 0 20px rgba(0, 0, 0, 0.15)}')

with open('templates/index.html', 'w') as f:
    f.write(x)
    print ('# FUTWATCH - index.html')
    f.close()
