# **Audio Recording**

- 오늘의 강의: **[유튜브 클론코딩: From #13.0 to #13.5](https://nomadcoders.co/wetube/lectures/2751)**
- 오늘의 과제: 위의 강의를 시청하신 후, 아래 코드 챌린지를 제출하면 됩니다.
- 제출기간: 2일 챌린지! 48시간. 금요일 오전 6시까지

Today's solution comes from **[jht981029](https://nomadcoders.co/users/jht981029)**! Great CSS!

## **Tasks**

Today we will make an audio recorder, it's just like the video recorder that we made on the course, but only with `audio:true, video:false`. The user will also be able to download the recording file when the recording is over.

`오디오 녹음기`를 만들어봅시다. 이 오디오 녹음기는 `audio:true, video:false` 이어야 합니다. 사용자는 녹음이 끝나면 녹음 파일을 다운로드할 수 있어야 합니다.

Features:

- 최대 5초 동안 녹음하세요.
- 녹음한 것을 웹 사이트에서 들을 수 있도록 사용자에게 녹음 미리 듣기를 제공하세요.(오디오 플레이어 만들기)
- `Start Recording`버튼을 만들고, 녹음이 끝나면 `Download Recording`버튼을 만드세요.

## **Hints:**

- **[audio](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio)**

## **TA's 힌트**

- **[regeneratorRuntime](https://www.npmjs.com/package/regenerator-runtime)**: Front-end에서 동기화 처리를 위해 사용하는 npm 패키지입니다.
- **[EventTarget.removeEventListener()](https://developer.mozilla.org/ko/docs/Web/API/EventTarget/removeEventListener)**: 이벤트를 리스너를 제거하는 자바스크립트의 메서드입니다.
- **[MediaDevices.getUserMedia()](https://developer.mozilla.org/ko/docs/Web/API/MediaDevices/getUserMedia)**: 사용자에게 미디어 입력 장치 사용 권한을 요청하는 메서드입니다.
- **[MediaStream Recording API](https://developer.mozilla.org/en-US/docs/Web/API/MediaStream_Recording_API)**: MediaStream을 녹음하는 API입니다.
- **[setTimeout()](https://developer.mozilla.org/en-US/docs/Web/API/setTimeout)**: 타이머가 만료되면 함수 또는 지정된 코드 조각을 실행하는 타이머를 설정하는 메서드입니다.
- **`[<a>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/a)`**
