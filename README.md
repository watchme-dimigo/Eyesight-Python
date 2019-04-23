# Eye Tracker with OpenCV

- [x] 얼굴 인식 ([haarcascade_frontalface_default](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml))
  - [x] use the largest face if multiple faces are found
  - [x] use the previous detection if no faces are found
    - [ ] previous detection이 감지된 시간을 고려하여 일시적으로 얼굴이 발견되지 않은 경우에만 사용(사용자가 실제로 자리를 비운 경우 감지되지 않아야 함)
  - [ ] 각 detection 간 시간을 고려하여 face 간 면적이 심하게 차이나는 경우 이전 데이터를 사용하거나 면적을 조정

- [ ] 눈 인식([haarcascade_eye.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_eye.xml))
  - [ ] eye blink detection
  - [ ] eye tracking
