import time
import json
import os
import logging
import requests
import tweepy
from threading import Thread
from http.client import IncompleteRead
from twython import TwythonStreamer
from twython import Twython

def read_config_file(self, filename):
    with open(filename, "r") as f:
        s = f.read()
    d = json.loads(s)
    APP_KEY = d["APP_KEY"]
    APP_SECRET = d["APP_SECRET"]
    TERMS_FILE = d["TERMS_FILE"]
    STORAGE_PATH = d["STORAGE_PATH"]
    return APP_KEY, APP_SECRET, TERMS_FILE, STORAGE_PATH

def get_oauth_link(self, APP_KEY, APP_SECRET):
    twitter = Twython(APP_KEY, APP_SECRET)
    auth = twitter.get_authentication_tokens()
    OAUTH_TOKEN = auth['oauth_token']
    OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
    url = (auth['auth_url'])
    r = requests.get(url)
    logging.info(
        "Go to the URL below, log in, and copy-paste the PIN you get to "
        "'code.txt':"
    )
    logging.info(url)
    return url, OAUTH_TOKEN, OAUTH_TOKEN_SECRET
    print(url)

# echo "" > code.txt

def wait_for_pin_code(self):
    while True:
        if not os.path.exists("code.txt"):
            time.sleep(5)
            logging.debug(
                "'code.txt' file doesn't exists, waiting to start listening"
                " to twitter until it is created"
            )
        else:
            pincode = 0
            with open("code.txt") as f:
                pincode = int(f.read().strip())
                logging.info("Pincode read succesfully:" + str(pincode))
            return str(pincode)

def remove_old_code_file(self):
    if os.path.exists("code.txt"):
        os.remove("code.txt")

def auth_with_pin(self, APP_KEY, APP_SECRET, OAUTH_TOKEN, 
                  OAUTH_TOKEN_SECRET, pincode):
    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    final_step = twitter.get_authorized_tokens(pincode)
    logging.debug("Old OATH_TOKEN: " + str(OAUTH_TOKEN))
    logging.debug("Old OAUTH_TOKEN_SECRET: " + str(OAUTH_TOKEN_SECRET))
    OAUTH_TOKEN = final_step['oauth_token']
    OAUTH_TOKEN_SECRET = final_step['oauth_token_secret']
    logging.debug("New OATH_TOKEN: " + str(OAUTH_TOKEN))
    logging.debug("New OAUTH_TOKEN_SECRET: " + str(OAUTH_TOKEN_SECRET))
    return OAUTH_TOKEN, OAUTH_TOKEN_SECRET

class TooLongTermException(Exception):
    def __init__(self, index):
        self.index = index

    def get_too_long_index(self):
        return self.index

class StreamListener(TwythonStreamer):
    def __init__(self, APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                 comm_list):
        super().__init__(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        self.tweet_list = comm_list

    def on_success(self, data):
        self.tweet_list.append(data)
        logging.info("tweet captured")

    def on_error(self, status_code, data):
        logging.error(status_code)
        logging.error(data)
        if int(status_code) == 406:
            data = str(data)
            try:
                index = int(data.strip().split()[4])
                logging.error("to remove index:" + str(index))
                raise TooLongTermException(index)
            except ValueError:
                logging.debug("ValueError while trying to extract number")


def get_authentication():
    auth = Authentication()
    logging.basicConfig(
        format='%(levelname)s: %(asctime)s - %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p',
        level=logging.INFO
    )

    logging.info("Removing old pincode file")
    auth.remove_old_code_file()

    logging.info("Loading config file")
    APP_KEY, APP_SECRET, TERMS_FILE, STORAGE_PATH = auth.read_config_file("config.json")

    logging.info("Getting OAuth data")
    url, OAUTH_TOKEN, OAUTH_TOKEN_SECRET = auth.get_oauth_link(APP_KEY, APP_SECRET)

    logging.info("Waiting for pin code")
    pincode = auth.wait_for_pin_code()

    logging.info("Authorizing with pin code")
    OAUTH_TOKEN, OAUTH_TOKEN_SECRET = auth.auth_with_pin(
        APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET, pincode
    )

    logging.info("Start listening....")

    filter_terms = []
    with open(TERMS_FILE) as f:
        for term in f:
            filter_terms.append(term.strip())
    logging.info("List of terms to filter" + str(filter_terms))

    return APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET, filter_terms, 
    STORAGE_PATH


def twitter_listener(
    APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET, comm_list):    
    streamer = StreamListener(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
    comm_list)
    while True:
        try:
            streamer.statuses.filter(track=[', '.join(filter_terms)], language='en')
        except requests.exceptions.ChunkedEncodingError:
            print('error, but under control\n')
            pass
        except IncompleteRead:
            print('incompletetereaderror, but under control')
            pass
        except TooLongTermException as e:
            index_to_remove = e.get_too_long_index()
            filter_terms.pop(index_to_remove)

def twitter_writer(comm_list):
    internal_list = []
    time_start = time.time()
    while True:
        if len(internal_list) > 100:
            file_name = STORAGE_PATH + str(round(time.time())) + ".json"
            with open(file_name, 'w+', encoding='utf-8') as output_file:
                json.dump(internal_list, output_file, indent=4)
                internal_list = []
                logging.info('------- Data dumped -------')
                time_stop = time.time()
                logging.info('Time taken for 100 tweets: {0:.2f}s'.format(
                    time_stop - time_start
                ))
                time_start = time.time()
        else:
            for i in range(len(comm_list)):
                internal_list.append(comm_list.pop())
            time.sleep(1)

if __name__ == '__main__':
    # Get the authentication
	APP_KEY = "MGMrvZLxwJI4sFcfXI20zLSHw"
	APP_SECRET = "Qg7Zb9St2aRYtjMpS30c0GRLoXGfPYqmkbS1y9CUFXN1n7hSVw"
	OAUTH_TOKEN = "958288187922767872-botZBbO5foM72uPJUa7aIiJdsIjENhN"
	OAUTH_TOKEN_SECRET = "YR3T506bpGRCSYFIrx535KK6JyYuaIB7XsJD1faNARbaZ"
	STORAGE_PATH= "./tweets/"
	filter_terms=["india"]

# Creating the authentication object
	auth = tweepy.OAuthHandler(APP_KEY, APP_SECRET)
# Setting your access token and secret
	auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
	# Creating the API object while passing in auth information
	api = tweepy.API(auth) 

	twitter = Twython(APP_KEY, APP_SECRET)
	authi = twitter.get_authentication_tokens()


comm_list =[]

    # Start the threads
listener = Thread(target = twitter_listener, args = (
        APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET, comm_list ))
listener.start()
writer = Thread(target = twitter_writer, args = (comm_list,))
writer.start()
writer.join()
listener.join()   