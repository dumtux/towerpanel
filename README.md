# TowerPanel - Operating Panel Webapp for TowerController III

Sponsored by [TowerSoftware](http://www.towersoftwareltd.com/)


## Experimental Running

Open 1st terminal.
This command will create two psudo serial port devices - `./ttySensor` and `./ttyOmega` connected together.

```
socat -d -d -v pty,rawer,echo=0,link=./reader pty,rawer,echo=0,link=./writer
```

Run in 2nd terminal
This script will emit endless dummy data to `./ttyOmega`.
And it will print the incoming data from `./ttyOmega`.

```
# activate venv
python serial_echo.py
```


Run the WebSocket server in 3rd terminal.
Open [http://localhost:8000] to play with it.

```
# activate venv
uvicorn ws_server:app
```
