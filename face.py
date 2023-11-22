import os
import cv2
from glob import glob
import datetime

if __name__ == "__main__":
    data = glob(os.path.join("faces", "*.jpg"))
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    output_folder = 'results'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for path in data:
        name = path.split("/")[-1]

        image = cv2.imread(path, cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
        
        cv2.imshow("image", image)
        k = cv2.waitKey(0)

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_filename = f"result_{timestamp}.jpg"
        output_path = os.path.join(output_folder, output_filename)

        if k == 27:         # wait for ESC key to exit
            cv2.destroyAllWindows()
        elif k == ord('s'):# wait for 's' key to save and exit
            cv2.imwrite(output_path, image)
            cv2.destroyAllWindows()