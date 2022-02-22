#!/opt/homebrew/bin/python3
import yfinance as yf
from tools.yfinance_downloader import download

download('BTC-USD')
