import cv2
import numpy


class LineTracker:
    def __init__(self):
        self._delta = 0.0
        self.line = False  

    def process(self, img: numpy.ndarray) -> None:
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        lower_white = numpy.array([0, 0, 160])
        upper_white = numpy.array([255, 80, 255])
        mask = cv2.inRange(hsv, lower_white, upper_white)
        
        h, w, d = img.shape

        search_top = int(3 * h / 4)
        search_bot = int(3 * h / 4 + 14)
        
        mask[0:search_top, 0:w] = 0
        mask[search_bot:, 0:w] = 0
        
        M = cv2.moments(mask)
        if M['m00'] > 0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            cv2.circle(img, (cx, cy), 20, (0, 0, 255), -1)
            self.line = True  

            err = cx - w / 2
            self._delta = err

        else:
            self.line = False  

        cv2.imshow("window", img)
        cv2.imshow("mask", mask)
        cv2.waitKey(3)  

    @property
    def delta(self):
        return self._delta

    @delta.setter
    def delta(self, delta):
        self._delta = delta


def main():
    tracker = LineTracker()
    import time
    for i in range(100):
        img = cv2.imread('../worlds/ros2_car_track_thick_lines.png')
        tracker.process(img)
        if tracker.line:
            print("Line detected")
        else:
            print("No line detected")
        time.sleep(0.1)


if __name__ == "__main__":
    main()

