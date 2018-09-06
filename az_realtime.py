from ib_api import IBApp
from utils import *


def init_ib_app():
    cfg = get_config('ib')
    return IBApp(cfg['ServerHost'], int(cfg['ServerPort']), int(cfg['ClientId']))


def main():
    app = init_ib_app()
    app.req_market_data(1000, )



if __name__ == '__main__':
    main()
