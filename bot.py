from telegram.ext import Updater, CommandHandler
import time
import datetime
import logging
import sys


formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh = logging.FileHandler('fancy.log')
fh.setFormatter(formatter)
sh = logging.StreamHandler(sys.stdout)
sh.setFormatter(formatter)
logging.basicConfig(level=logging.INFO, handlers=[fh, sh], format=formatter)

logger = logging.getLogger(__name__)
start_time = time.time()


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"' % (update, error))


def start(bot, update):
    logger.info('send start command')
    date1 = datetime.datetime.fromtimestamp(int(start_time))
    date2 = datetime.datetime.fromtimestamp(int(time.time()))
    delta = (date2 - date1)
    update.message.reply_text(str(delta))


def main():
    updater = Updater(token='511667757:AAHMM0NRF4njpnuFbF_pWRQhqF3w5Aojjw8',
                      request_kwargs=({'proxy_url': 'socks5://telegram.vpn99.net:55655'}))
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_error_handler(error)
    updater.start_polling(poll_interval=2, timeout=30, read_latency=5)
    updater.idle()


if __name__ == '__main__':
    main()