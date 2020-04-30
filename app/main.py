from flask import Flask , render_template,session
import pytesseract
import sys
import re
import os
import requests
import cv2
import base64
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
app.secret_key = 'dljsaklqk24e21cjn!Ew@@dsa5'
app.config['TEMP_FOLDER'] = '/tmp'
pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'
home_url = 'https://parivahan.gov.in/rcdlstatus/'
post_url = 'https://parivahan.gov.in/rcdlstatus/vahan/rcDlHome.xhtml'

def resolve():
	enhancedImage = enhance()
	custom_config = r'--oem 1 --psm 8 -c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz'
	return pytesseract.image_to_string(enhancedImage, config=custom_config)

def enhance():
	img = cv2.imread('/tmp/downloadedpng.jpg', 0)
	kernel = np.ones((2,2), np.uint8)
	img_erosion = cv2.erode(img, kernel, iterations=1)
	img_dilation = cv2.dilate(img_erosion, kernel, iterations=1)
	erosion_again = cv2.erode(img_dilation, kernel, iterations=1)
	final = cv2.GaussianBlur(erosion_again, (1, 1), 0)
	cv2.imwrite("/tmp/Captcha.jpg",final)
	return final

@app.route("/")
def home_view():
	ses = requests.Session()
	my_headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15"}
	r = ses.get(url=home_url,headers=my_headers)
	cookies = r.cookies
	session["cookies"]=cookies
	soup = BeautifulSoup(r.text, 'html.parser')
	viewstate = soup.select('input[name="javax.faces.ViewState"]')[0]['value']
	session["viewstate"]=viewstate
	button = soup.find("button",{"type": "submit"})	
	img_test=soup.find("img",{"id": "form_rcdl:j_idt34:j_idt41"})
	session["button"]=button['id']
	iresponse = session.get("https://parivahan.gov.in"+img_test['src'])
	img = Image.open(BytesIO(iresponse.content))
	img.save(os.path.join("/tmp/","downloadedpng.jpg"))
	buffered = BytesIO(iresponse.content)
	img.save(buffered, format="JPEG")
	img_str = base64.b64encode(buffered.getvalue())
	custom_config = r'--oem 1 --psm 8 -c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz'
	captcha_text = resolve()
	extracted_text = captcha_text.replace(" ", "").replace("\n", "")
	#extracted_text ="test4"
	return render_template("index.html",imglink="data:image/png;base64,"+img_str.decode("utf-8"),captchaText=extracted_text)

@app.route('/result',methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		data = {
			'javax.faces.partial.ajax':'true',
			'javax.faces.source': session.get("button",None),
			'javax.faces.partial.execute':'@all',
			'javax.faces.partial.render': 'form_rcdl:pnl_show form_rcdl:pg_show form_rcdl:rcdl_pnl',
			session.get("button",None):session.get("button",None),
			'form_rcdl':'form_rcdl',
			'form_rcdl:tf_reg_no1': request.form['first'],
			'form_rcdl:tf_reg_no2': request.form['second'],
			'form_rcdl:j_idt34:CaptchaID':request.form['captcha'],
			'javax.faces.ViewState': session.get("viewstate",None)
			}
		headers = {
			'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'Accept': 'application/xml, text/xml, */*; q=0.01',
			'Accept-Language': 'en-us',
			'Accept-Encoding': 'gzip, deflate, br',
			'Host': 'parivahan.gov.in',
			'DNT': '1',
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15',
			'Cookie': 'JSESSIONID=%s; has_js=1' % cookies['JSESSIONID'],
			'X-Requested-With':'XMLHttpRequest',
			'Faces-Request':'partial/ajax',
			'Origin':'https://parivahan.gov.in',
			'Referer':'https://parivahan.gov.in/rcdlstatus/',
			'Connection':'keep-alive'
			# 'User-Agent': 'python-requests/0.8.0',
			# 'Access-Control-Allow-Origin':'*',
		}

		# MARK: Added delay
		sleep(2.0)

		r = ses.post(url=post_url, data=data, headers=headers, cookies=cookies)
		soup = BeautifulSoup(r.text, 'html.parser')
		table = SoupStrainer('tr')
		soup = BeautifulSoup(soup.get_text(), 'html.parser', parse_only=table)
		resp = jsonify( {
			u'status': 200,
			u'details':soup.get_text()
				} )
		return resp