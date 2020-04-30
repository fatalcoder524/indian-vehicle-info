# indian-vehicle-info

## Introduction

With the increasing forgery cases, identity verification via one means or the other has become quite crucial. Therefore, the government and industry regulations make sure that the businesses carry out proper identity authentication of their customers to avoid any kind of identity theft. Vehicles are issued a Registration Certificate (RC) which holds the basic information about the owner and the vehicle itself. Before trusting an individual, we need to check the identity of any individual which can be easily done by Registration Certificate Check. This can be done by authenticating the basic information provided on the RC ensuring that the vehicle is registered with the Regional Transport Office (RTO) authorities and legalizes the owner.

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

## Special Thanks

@nikhilweee [CODE](https://gist.github.com/nikhilweee/9efd9731880104dd00ecf2ed8effacc5)

@anmolrajpal [REPO](https://github.com/anmolrajpal/vehicle-info)

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
