# -*- coding: utf-8 -*-
"""
@Author: Mathiyazhagan Ramaniselva
@Date: 27.03.2023
"""

import threading
import time
import cv2
import numpy as np

_CAMERA_NO = 0
_FONT_SIZE = 1
_BOUNDING_BOX_LINE_WIDTH = 2

_PERSONE_1_NAME = "Mathi"
_UNKNOWN_PERSON = "Unknown"

from application_modules.logger_module import Logger_Module
import common.common_definitions as comm_def

class Face_Recognizer:
    _logger = Logger_Module()
    def __init__(self, mode_monitor, alert_manager):
        self._logger.logInfo("Face_Recognizer Init Started")

        self.__mode_monitor = mode_monitor
        self.__alert_manager = alert_manager

        self.__faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.__camera = cv2.VideoCapture(_CAMERA_NO)
        self.__face_recog = cv2.face.LBPHFaceRecognizer_create()
        self.__face_recog.read('trainningData.yml')
        self.__id = 0
        self.is_alert_detected = 0

        self.__mode = self.__mode_monitor.get_mode()
        self.__mode_monitor.register_mode_monitor_callback(self.mode_callback)

        threading.Thread(target=self.__face_recognizer, daemon=True).start()

        self._logger.logInfo("Face_Recognizer Init Completed")

    def mode_callback(self, mode):
        self.__mode = mode

    def alert_callback(self, alert_handle):
        if alert_handle[0] == comm_def._RESET:
            self.is_alert_detected = 0

    def __face_recognizer(self):
        self._logger.logInfo("Face_Recognizer Thread Started")
        __unknown_face_counter = 0

        while True:
            if self.__mode == comm_def._SECURITY_MODE:
                ret, __frame = self.__camera.read()

                if ret == True:
                    __gray_frame = cv2.cvtColor(__frame, cv2.COLOR_BGR2GRAY)
                    faces = self.__faceDetect.detectMultiScale(__gray_frame, 1.3, 5)

                    for(x,y,w,h) in faces:
                        cv2.rectangle(__frame, (x, y), (x+w, y+h), (0, 255, 0), _BOUNDING_BOX_LINE_WIDTH)
                        self.__id, conf = self.__face_recog.predict(__gray_frame[y:y+h,x:x+w])

                        if conf < 50:
                            if self.__id == 1:
                                self.__id = _PERSONE_1_NAME
                                __unknown_face_counter = 0
                                __blue = 0
                                __green = 255
                                __red = 0
                        else:
                            self.__id = _UNKNOWN_PERSON
                            __unknown_face_counter = __unknown_face_counter + 1
                            __blue = 0
                            __green = 0
                            __red = 255

                        if __unknown_face_counter >= 10:
                            self.is_alert_detected = 1
                            self.__alert_manager.set_alert(comm_def._ALERT, "Unknow Person Detected")
                        
                        __font = cv2.FONT_HERSHEY_COMPLEX_SMALL
                        
                        cv2.putText(__frame, str(self.__id), (x, y+h), __font, _FONT_SIZE, (__blue, __green, __red), _BOUNDING_BOX_LINE_WIDTH, cv2.LINE_AA)
                    cv2.imshow('Face', __frame) 
                    if cv2.waitKey(10)==ord('q'):
                        break

            if self.is_alert_detected == 1:
                time.sleep(10)
            else:
                time.sleep(0.2)