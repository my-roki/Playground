import logging
from datetime import datetime

# # logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")
# logging.basicConfig(level=logging.ERROR, format="%(asctime)s [%(levelname)s] %(message)s")

# # debug < info < warning < error < critical
# logging.debug("who did that?!")
# logging.info("ready to RPA")
# logging.warning("this script is old version. need to fix.")
# logging.error("error:!@$%!@#$^@#!@$#%^#")
# logging.critical("critical error happens.")


# 터미널과 파일에 함께 로그 남기기
    # 시간 [로그레벨] 메시지 형태로 로그를 작성
logFomatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger()
    # 로그 레벨을 설정
logger.setLevel(logging.DEBUG)

    # 스트림(TERMINAL)
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFomatter)
logger.addHandler(streamHandler)

    # 파일
filename = datetime.now().strftime("mylogfile_%Y%m%d%H%M%S.log")
fileHandler = logging.FileHandler(filename, encoding="utf-8")
fileHandler.setFormatter(logFomatter)
logger.addHandler(fileHandler)


logger.debug("로그를 남겨보는 테스트를 진행중입니다.")




