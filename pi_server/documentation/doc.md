# Kibblepi - Developed at SolipsIA
#Configuration Raspberrypi:

##Creation service in /lib/systemd/system
+ pi@raspberrypi:/lib/systemd/system $ sudo nano kibblepi_server.service

##Start the service manually
+ sudo systemctl start kibblepi_server.service
##Stop the service manually
+ sudo systemctl stop kibblepi_server.service

##Enable the service automatically
+ sudo systemctl enable kibblepi_server.service

##Disable the service automatically
+ sudo systemctl disable kibblepi_server.service