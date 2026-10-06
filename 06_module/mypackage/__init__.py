# __init__.py (패키지 초기화 파일)
# 패키지가 로드할 때 실행되는 초기화 파일

# 1. 패키지를 import 할 때 실행되어야 하는 초기화 코드 (환경 확인, 설정값 로드)
print("__init__ 1")

# 2. 패키지 메타데이터 작성 (버전, 작성자)
VERSION = "1.0.0"

# 3. 패키지 re-export
from mypackage.mymath import add  # 절대 임프트
from .mymath import add           # 상대 임포트    
