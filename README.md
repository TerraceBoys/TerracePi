# TerracePi
Repository for raspberry pi fun

2 Running threads:  
1. Tracks Roxbury Crossing train arrival times from MBTA API  
    - Refreshes every 10 seconds  
2. Tracks Boston current weather condition from Weather Underground API  
    - Refreshes every 15 seconds  

### Setup
1. Install (python virtualenv)[http://docs.python-guide.org/en/latest/dev/virtualenvs/]
2. Setup and workon a new virtual environment
3. `cd` into the TerracePi repo and run `pip install -r requirements.txt` You might get an error when 
trying to install`rgbmatrix`. This is fine
4. Install rgbmatrix
```
git clone https://github.com/hzeller/rpi-rgb-led-matrix
cd rpi-rgb-led-matrix
make build-python
make install-python
```