# Kibblepi - Developed at SolipsIA
#Configuration Raspberrypi:

##Creation service in /lib/systemd/system
+ pi@raspberrypi:/lib/systemd/system $ sudo nano kibblepi_start_server.service

##Start the service manually
+ sudo systemctl start kibblepi_start_server.service
##Stop the service manually
+ sudo systemctl stop kibblepi_start_server.service

##Enable the service automatically
+ sudo systemctl enable kibblepi_start_server.service

##Enable the service automatically
+ sudo systemctl enable kibblepi_start_server.service