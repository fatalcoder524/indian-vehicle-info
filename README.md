# indian-vehicle-info

<meta name="title" content="indian-vehicle-info">
<meta name="google-site-verification" content="5RwvfxhskLEn5yvG-pb1wefMTa_W03rH9JfpljAT0U0" />
<meta name="description" content="Trace Vehicle Number, Owner Name, Location, address, RTO Registration Number.Vehicle Registration information like location, RTO Code, District, State.">
<meta name="keywords" content="indian rto api,rto api,indian rto web scrapper,indian vehicle details,indian vehicle details api,indian vehicle registration details,indian vehicle registration details api,indian vehicle registration details web scrapper,vehicle registration details web scrapper,vehicle registration details api,vehicle registration details flask app,indian vehicle registration details flask app,indian rto flask app,indian vehicle details flask app,rto flask app">
<meta name="robots" content="index, follow">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta name="language" content="English">
<meta name="revisit-after" content="1 day">
<meta name="author" content="fatalcoder524">

| :warning: | Please read the [disclaimer](../master/README.md#disclaimer) at the end of the file before you proceed. |
| :---: | :---: |

## Introduction

With the increasing forgery cases, identity verification via one means or the other has become quite crucial. Therefore, the government and industry regulations make sure that the businesses carry out proper identity authentication of their customers to avoid any kind of identity theft. Vehicles are issued a Registration Certificate (RC) which holds the basic information about the owner and the vehicle itself. Before trusting an individual, we need to check the identity of any individual which can be easily done by Registration Certificate Check. This can be done by authenticating the basic information provided on the RC ensuring that the vehicle is registered with the Regional Transport Office (RTO) authorities and legalizes the owner.

Vehicle Registration Details from Vahan by Government of India. Data from the different State Registers situated at State Data Centers flow to the National Register.

## Prerequisites

* Python 3
* Tesseract OCR
* OpenCV
* pytesseract
* bs4

## Setup [Command line APP]

* Install Tesseract OCR.
* Change `pytesseract.pytesseract.tesseract_cmd` value in `vehicleinfo.py` to `tesseract` path.
* Install bs4, pytesseract and OpenCV.
```
pip install -r requirements.txt
```

## Usage [Command line APP]

* To use this, just run the command `python vehicleinfo.py MH47K 4272`.(Must split the Vehicle Number.Part 2 must have exactly 4 digits.)
* If the Tesseract OCR output matches with `Captcha` image, type `Y` or `y`. Else Type `N` or `n`. 
* Close the captcha window or press any key on captcha window to continue with the script.
* If the Captcha didn't match, then enter the correct Captcha.

## Deploy Flask App to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Configuration [Flask App]

* If any error occurs, check the logs using `heroku logs --tail`.

* Any errors related to tessdata, change `TESSDATA_PREFIX` in `Settings/Config Vars` in Heroku Dashboard. Default value is `./.apt/usr/share/tesseract-ocr/4.00/tessdata`. 

* To find the value for your app, run heroku bash using `heroku run bash` and execute `find -iname tessdata`.Copy this and paste it in Config Vars.

## How to use
Let us assume you have deployed this app in Heroku and you called it `your-heroku-app`.

The app provides a web client `https://your-heroku-app.herokuapp.com/` and `https://your-heroku-app.herokuapp.com/result` will have the result.

This app is available at https://vehicle-info.herokuapp.com/.

## Licence
```
MIT Licence. Copyright (c) 2020 Suraj J Pai

Check Licence file for more information.
```

## Special Thanks

@nikhilweee [CODE](https://gist.github.com/nikhilweee/9efd9731880104dd00ecf2ed8effacc5)

@anmolrajpal [REPO](https://github.com/anmolrajpal/vehicle-info)

## Disclaimer

This work is just to test my knowledge on subject matter and is not designed for any commercial or everyday use. This app is not designed for any illegal use. As per the terms and uses of https://parivahan.gov.in/ , it is completly prohibited. Please use this at your own risk.

### Disclaimer of liability

The material and information contained on this repository is for general information purposes only. You should not rely upon the material or information on the website as a basis for making any business, legal or any other decisions.

Whilst we endeavour to keep the information up to date and correct, the author makes no representations or warranties of any kind, express or implied about the completeness, accuracy, reliability, suitability or availability with respect to the website or the information, products, services or related graphics contained on the website for any purpose. Any reliance you place on such material is therefore strictly at your own risk.

The author will not be liable for any false, inaccurate, inappropriate or incomplete information presented on the website.

Although every effort is made to keep the website up and running smoothly, due to the nature of the Internet and the technology involved, the author takes no responsibility for and will not be liable for the website being temporarily unavailable due to technical issues (or otherwise) beyond its control or for any loss or damage suffered as a result of the use of or access to, or inability to use or access this website whatsoever.

To the extent not prohibited by law, in no circumstances shall the author be liable to you or any other third parties for any loss or damage (including, without limitation, damage for loss of business or loss of profits) arising directly or indirectly from your use of or inability to use, this site or any of the material contained in it.

### Fair Use Disclaimer

Copyright Disclaimer under section 107 of the Copyright Act 1976, allowance is made for “fair use” for purposes such as criticism, comment, news reporting, teaching, scholarship, education and research.

Fair use is a use permitted by copyright statute that might otherwise be infringing. 

Non-profit, educational or personal use tips the balance in favor of fair use. 

## Tags

indian rto api

rto api

indian rto web scrapper

indian vehicle details

indian vehicle details api

indian vehicle registration details

indian vehicle registration details api

indian vehicle registration details web scrapper

vehicle registration details web scrapper

vehicle registration details api

vehicle registration details flask app

indian vehicle registration details flask app

indian rto flask app

indian vehicle details flask app

rto flask app

trace vehicle owner name by vehicle number

Trace Vehicle Number, Owner Name, Location, address, RTO Registration Number

Vehicle Registration information like location, RTO Code, District, State.

Address of RTO ( Regional Transport Officer) Where vehicle is insured.

Owner name of the Vehicle.

Vehicle Engine Number, Chassis Number, Fuel Type ( Petrol / Diesel )

vehicle registration details by vehicle number
