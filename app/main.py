from flask import Flask 
import re
import os
import requests
import cv2
import json 
import numpy as np
from time import sleep
try:
    import Image
except ImportError:
    from PIL import Image, ImageEnhance
from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlretrieve
from io import BytesIO

app = Flask(__name__) 
home_url = 'https://parivahan.gov.in/rcdlstatus/'
post_url = 'https://parivahan.gov.in/rcdlstatus/vahan/rcDlHome.xhtml'

@app.route("/") 
def home_view(): 
		r = requests.get(url=home_url)
		cookies = r.cookies
		soup = BeautifulSoup(r.text, 'html.parser')
		viewstate = soup.select('input[name="javax.faces.ViewState"]')[0]['value']
		button = soup.find("button",{"type": "submit"})	
		img_test=soup.find("img",{"id": "form_rcdl:j_idt34:j_idt41"})
		return """<html>
		<body>
		<form action = '/result' method = 'POST'>
         <p>Vehicle Reg. No. Part1 <input type = 'text' name = 'first' placeholder='MH47K'/></p>
         <p>Vehicle Reg. No. Part2 <input type = 'text' name = 'second' placeholder='4272'/></p>
		 <p><img src='https://parivahan.gov.in{{img_test['src']}}></p>
         <p>Captcha <input type = 'text' name = 'captcha' /></p>
         <p><input type = 'submit' value = 'submit' /></p>
      </form>
   </body>
</html>"""

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return """
	  <!doctype html>
<html>
   <body>
      <table border = 1>
         {% for key, value in result.items() %}
            <tr>
               <th> {{ key }} </th>
               <td> {{ value }} </td>
            </tr>
         {% endfor %}
      </table>
   </body>
</html>
	  """