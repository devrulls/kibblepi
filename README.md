# Kibblepi - Developed at SolipsIA

This is an internship project developed at SolipsIA to validate the skills acquired in the professional title "Concepteur Développeur d’applications" at the GRETA Littoral - Montpellier.
This project consists in the creation of a cat kibble distributor, called "Kibblepi", this distributor will allow you to feed your pet whenever you want, 
through a web application developed with the Streamlit framework and server side developed with the micro-framework flask. 
(Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries)


## Technologies:
- [Streamlit](https://streamlit.io/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)

### Prerequisites

| WEB-SERVER             | WEB-APP       |
|------------------------|---------------|
| Python 3.7.3           | Python 3.10.2 |
| Flask                  | Streamlit     |
| Raspberry Pi OS Buster | -             |
| VNC Viewer             | -             |
| Arduino Software       | -             |


## Streamlit Web–App
- Python V3.10.2 [Download](https://www.python.org/downloads/)

## Raspberry server Web–Server
 
- RaspberryPi OS Buster [Download](https://downloads.raspberrypi.org/raspios_armhf/images/raspios_armhf-2021-05-28/)
- Python V-3.7.3 [Download](https://www.python.org/downloads/release/python-373/)
- VNC Viewer [Download](https://www.realvnc.com/en/connect/download/viewer/)
- Arduino-Software [Download](https://www.arduino.cc/en/software)

Hardware :

- Raspberry Pi-3 Model B
- Adafruit 16-Channel PWM / Servo HAT for Raspberry PI
- Accessory kit-Arduino

### Setup env
```commandline
pip install pipenv
pipenv install -r path/to/requirements.txt
pipenv --venv path/to/venv
pipenv shell  # to activate this project’s virtualenv
```

## Deploying The App
+ Heroku [WebApp](https://kibblepi.herokuapp.com/)

This app is deployed on heroku and is connected to your github repository with the main branch. 
Heroku allows you to control the branches of your developing apps by allowing you to configure your github pushes to automatically build and deploy to that app.

        

