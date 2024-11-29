# app/logging.py
import logging

logging.basicConfig(filename='../raid.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(module)s:%(message)s')