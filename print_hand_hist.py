import cv2
import numpy as np
import pickle, os, sqlite3, random

def get_hand_hist():
	with open("hist", "rb") as f:
		hist = pickle.load(f)
	return hist


hand_hist = get_hand_hist()
print(hand_hist)