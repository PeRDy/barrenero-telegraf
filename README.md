# Barrenero Telegraf
Extension for Barrenero that harvests information and send it using Telegraf.

* **Version**: 1.0.0
* **Status**: Production/Stable
* **Author**: José Antonio Perdiguero López

This extension provides an automatic way of harvesting Barrenero status through its API and send it through Telegraf.

Full [documentation](http://barrenero.readthedocs.io) for Barrenero project.

## Help us Donating
This project is free and open sourced, you can use it, spread the word, contribute to the codebase and help us donating:

* **Ether**: `0x566d41b925ed1d9f643748d652f4e66593cba9c9`
* **Bitcoin**: `1Jtj2m65DN2UsUzxXhr355x38T6pPGhqiA`
* **PayPal**: `barrenerobot@gmail.com`

## Requirements
* Docker. [Official docs](https://docs.docker.com/engine/installation/).

## Quick start
Run the service: `docker run -v /etc/barrenero/barrenero-telegraf/:/etc/telegraf/ perdy/barrenero-telegraf:latest telegraf`

