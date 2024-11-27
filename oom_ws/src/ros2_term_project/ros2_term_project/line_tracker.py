import cv2
import numpy as np


class LineTracker:
    def __init__(self):
        self._delta = 0.0
        self.line = False
        self.left_center = None
        self.right_center = None
        self.mid_point = None

    def process(self, img: np.ndarray) -> None:
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        lower_white = np.array([0, 0, 160])
        upper_white = np.array([255, 80, 255])
        mask = cv2.inRange(hsv, lower_white, upper_white)

        h, w, d = img.shape

        search_top = int(2 * h / 3)
        search_bot = int(3 * h / 4 + 14)
        mask[0:search_top, 0:w] = 0
        mask[search_bot:, 0:w] = 0

        left_mask = mask[:, :w // 2]
        right_mask = mask[:, w // 2:]

        self.left_center = self._find_centroid(left_mask, w_offset=0)
        self.right_center = self._find_centroid(right_mask, w_offset=w // 2)

        if self.left_center:
            cv2.circle(img, self.left_center, 10, (255, 0, 0), -1)
        if self.right_center:
            cv2.circle(img, self.right_center, 10, (0, 255, 0), -1)

        if self.left_center and self.right_center:
            lx, ly = self.left_center
            rx, ry = self.right_center
            self.mid_point = (int((lx + rx) / 2), int((ly + ry) / 2))
            cv2.circle(img, self.mid_point, 10, (0, 0, 255), -1)
            self.line = True
            self._delta = (lx + rx) / 2 - w / 2

        cv2.imshow("window", img)
        cv2.imshow("mask", mask)
        cv2.waitKey(3)  

    def _find_centroid(self, mask: np.ndarray, w_offset: int) -> tuple:
        M = cv2.moments(mask)
        if M['m00'] > 0:
            cx = int(M['m10'] / M['m00']) + w_offset
            cy = int(M['m01'] / M['m00'])
            return (cx, cy)
        return None

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
        img = cv2.imread('sample2.png')
        tracker.process(img)
        if tracker.line:
            print("Line detected")
        else:
            print("No line detected")
        time.sleep(0.1)


if __name__ == "__main__":
    main()

