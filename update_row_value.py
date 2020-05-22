import cv2
import numpy as np
import pickle, os, sqlite3, random


conn = sqlite3.connect("gesture_db2.db")
view_table_cmd = "UPDATE gesture SET g_name = 'Rock!' WHERE g_id = 7"
conn.execute(view_table_cmd)
conn.commit()