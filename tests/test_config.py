import ptrading
import datetime

def test_config_init():
	time_unit = ptrading.utils.TimeUnit.ONE_MINUTE
	tickers = ["AAPL", "MSFT"]
	pre_market = False
	start_date = datetime.datetime(2020, 3, 18)
	end_date = datetime.datetime(2020, 4, 20)

	config = ptrading.config.Config(tickers, pre_market, time_unit, start_date, end_date)
	assert True

def test_user_config_init():
	principal = 50000

	user_config = ptrading.config.UserConfig(principal)
	assert True
