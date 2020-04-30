from flask import Flask , render_template
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
pytesseract.pytesseract.tesseract_cmd = r'tesseract'
home_url = 'https://parivahan.gov.in/rcdlstatus/'
post_url = 'https://parivahan.gov.in/rcdlstatus/vahan/rcDlHome.xhtml'
session = requests.Session()
my_headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15"}
r = session.get(url=home_url,headers=my_headers)
cookies = r.cookies
soup = BeautifulSoup(r.text, 'html.parser')
viewstate = soup.select('input[name="javax.faces.ViewState"]')[0]['value']
button = soup.find("button",{"type": "submit"})	
img_test=soup.find("img",{"id": "form_rcdl:j_idt34:j_idt41"})
iresponse = session.get("https://parivahan.gov.in"+img_test['src'])
img = Image.open(BytesIO(iresponse.content))
img.save("downloadedpng.png")

@app.route("/")
def resolve(img):
	enhancedImage = enhance()
	custom_config = r'--oem 1 --psm 8 -c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz'
	return pytesseract.image_to_string(enhancedImage, config=custom_config)

def enhance():
	img = cv2.imread('downloadedpng.png', 0)
	kernel = np.ones((2,2), np.uint8)
	img_erosion = cv2.erode(img, kernel, iterations=1)
	img_dilation = cv2.dilate(img_erosion, kernel, iterations=1)
	erosion_again = cv2.erode(img_dilation, kernel, iterations=1)
	final = cv2.GaussianBlur(erosion_again, (1, 1), 0)
	cv2.imwrite("Captcha.png",final)
	return final
	
def home_view():
	custom_config = r'--oem 1 --psm 8 -c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz'
	captcha_text = resolve(img)
	extracted_text = captcha_text.replace(" ", "").replace("\n", "")
	return render_template("index.html",{imglink="downloadedpng.png",captchaText=extracted_text})

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
    file = request.files['file']
    hocr = request.form.get('hocr') or ''
    ext = '.hocr' if hocr else '.txt'
    if file and allowed_file(file.filename):
      folder = os.path.join(app.config['TEMP_FOLDER'], str(os.getpid()))
      os.mkdir(folder)
      input_file = os.path.join(folder, secure_filename(file.filename))
      output_file = os.path.join(folder, app.config['OCR_OUTPUT_FILE'])
      file.save(input_file)

      command = ['tesseract', input_file, output_file, '-l', request.form['lang'], hocr]
      proc = subprocess.Popen(command, stderr=subprocess.PIPE)
      proc.wait()

      output_file += ext

      if os.path.isfile(output_file):
        f = open(output_file)
        resp = jsonify( {
          u'status': 200,
          u'ocr':{k:v.decode('utf-8') for k,v in enumerate(f.read().splitlines())}
        } )
      else:
        resp = jsonify( {
          u'status': 422,
          u'message': u'Unprocessable Entity'
        } )
        resp.status_code = 422

      shutil.rmtree(folder)
      return resp
    else:
      resp = jsonify( { 
        u'status': 415,
        u'message': u'Unsupported Media Type' 
      } )
      resp.status_code = 415
      return resp
  else:
    resp = jsonify( { 
      u'status': 405, 
      u'message': u'The method is not allowed for the requested URL' 
    } )
    resp.status_code = 405
    return resp