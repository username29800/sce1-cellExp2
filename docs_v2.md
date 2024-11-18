1. 프로젝트 개요

프로젝트 철학

이 프로젝트는 세포 생물학의 작동 방식을 모방한 보안 시스템을 개발합니다. 시스템은 감염 탐지 및 반응, 세포 간 통신, 그리고 Python 기반 네트워크 시뮬레이션을 통해 사이버 위협에 효과적으로 대응하는 데 중점을 둡니다.

주요 기능

1. 감염 탐지 및 복구
세포의 상태를 지속적으로 모니터링하고 비정상적인 동작(감염)을 감지하면 즉시 자가 진단 및 복구를 수행합니다.


2. 세포 간 통신
감염 여부 및 상태 정보를 교환하며, 네트워크 상의 다른 세포들에게 복구 지침을 전파합니다.


3. 네트워크 시뮬레이션
Python으로 구축된 가상 환경에서 다중 세포의 협력 및 경쟁을 테스트하며, 향후 물리적 하드웨어 확장을 염두에 둡니다.



활용 가능성

보안 시스템의 자율 운영 및 빠른 대응

네트워크 상의 바이러스 확산 및 복구 시뮬레이션

학문적 연구 또는 사이버보안 훈련 환경으로 활용



---

2. 파일 트리와 설명

./
├── .git/                     # Git 저장소 관련 파일
├── .idea/                    # PyCharm 프로젝트 파일
├── cell_0/                   # 개별 세포 디렉터리
│   ├── main.py               # 세포 초기화 및 작업 수행 스크립트
│   ├── utils.py              # 유틸리티 함수 정의
│   ├── keepalive.py          # 자가진단 및 복구 로직 구현
│   ├── setup.py              # 초기 설치 및 환경 설정 스크립트
│   ├── appdata.zip           # allow.txt에 정의된 파일 백업
│   ├── filedesc/             # 파일 목록 및 내용 디렉터리
│   └── t_cell_0_0.zip        # 통신용 패키지 파일
├── post/                     # 데이터 전송 및 로그 디렉터리
│   ├── dir_keepalive         # Git 등록 방지용 빈 디렉터리
│   └── t_cell_0_0/           # 데이터 교환을 위한 세부 디렉터리
├── __pycache__/              # Python 캐시 디렉터리
├── utils_docs.md             # 유틸리티 함수 설명 문서
├── docs_easy.md              # 사용 설명서 초안
├── devc.txt                  # 개발자 기록 파일
├── lc                        # 기타 파일


---

3. 주요 스크립트의 역할

1. main.py

역할:

세포의 초기화 및 상태 점검

작업 수행 후 결과를 출력하거나 전송


구성 요소:

avail(): 세포 상태를 확인하여 비활성화 상태일 경우 종료

wrtout(): 작업 결과를 출력 파일에 저장

outpost(): 패키징된 데이터를 전송


2. utils.py

역할:

공통적으로 사용되는 함수 정의

플래그 처리, 파일 목록 관리, 압축 및 복구 기능 제공


3. keepalive.py

역할:

세포 상태를 주기적으로 점검

apoptosis_init(): 감염 발생 시 데이터 백업 후 세포 제거


4. packager.py

역할:

데이터 압축 및 패키징

감염 샘플, 허용 파일 목록 및 기타 데이터를 저장하거나 전송


5. setup.py

역할:

최초 실행 시 파일 초기화 및 allowlist 생성

init 옵션으로 초기 설치 수행



---

4. 실행 방법

Python 버전 및 필수 라이브러리

Python 3.8 이상

필수 라이브러리: shutil, os, subprocess, zipfile


주요 실행 파일

1. setup.py
초기화:

python setup.py init


2. main.py
세포 실행:

python main.py



입력/출력 포맷

입력: allow.txt, appdata.zip 등

출력: 상태 로그 및 결과 데이터 파일(out_*.txt)



---

5. 작동 원리 설명

작동 과정 요약

1. Setup: setup.py 실행 후 초기 파일 설정 및 압축 해제


2. Initialization: main.py가 상태를 확인하고 작업 수행


3. Self-Maintenance: keepalive.py가 문제를 감지하고 복구


4. Data Exchange: packager.py로 데이터 전송 및 백업



플로우 다이어그램

Setup

setup.py 실행 → allow.txt 생성 → 초기 압축 파일 복구


Main Process

main.py → 상태 확인(keepalive.py) → 작업 결과 출력(outpost)


Communication

packager.py로 데이터 패키징 → post/에 데이터 저장


Error Handling

비정상 상태 감지 → apoptosis_init() 실행 → 세포 비활성화 및 복구




---

6. 유틸리티 문서화

utils.py 주요 함수

1. auto_flag(flag_file)

매개변수: 플래그 파일 경로

반환값: 현재 상태 플래그 문자열

역할: 세포 상태를 자동으로 확인



2. xll_find_missing(al_file, scan_dir)

매개변수: allowlist 파일 경로, 검색 디렉터리

반환값: 누락된 파일 목록

역할: allowlist와 비교해 손실된 파일 확인





---

7. 향후 개선 방향

1. 디렉터리 구조 간소화

중요 파일 중심으로 디렉터리 통합

불필요한 빈 디렉터리 제거



2. 추가 기능

동적 세포 간 네트워크 구성

감염 경로 추적 및 시각화 기능



3. 코드 최적화

pandas 또는 asyncio를 활용해 데이터 처리 및 병렬 작업 성능 개선




아래는 utils.py의 모든 함수를 신입 개발자가 이해하고 활용할 수 있도록 작성한 상세한 문서입니다.


---

utils.py 함수 문서화


---

1. Basics Section

equal_str(list_a)

설명: 주어진 문자열 리스트의 각 요소에서 개행 문자(\n)를 제거합니다.

매개변수:

list_a (list): 문자열을 포함하는 리스트.


반환값:

(list): 개행 문자가 제거된 리스트.


사용 예시:

equal_str(["line1\n", "line2\n"]) 
# 반환: ["line1", "line2"]


substr(str_origin, str_sub)

설명: str_origin에서 str_sub의 모든 문자를 제거한 나머지 부분을 반환합니다.

매개변수:

str_origin (str): 원본 문자열.

str_sub (str): 제거하려는 문자열.


반환값:

(str): 제거 후의 문자열.


사용 예시:

substr("hello world", "hello") 
# 반환: " world"



---

2. Flag Handling Section

get_flag(flag_file, flag_line)

설명: 특정 파일에서 지정된 줄의 플래그를 반환합니다.

매개변수:

flag_file (str): 플래그 파일 경로.

flag_line (int): 플래그가 위치한 줄 번호 (1부터 시작).


반환값:

(str): 해당 줄의 플래그 값.


사용 예시:

get_flag("status.txt", 1) 
# 반환: "active" (예: flag = active인 경우)


format_flag(flag_file, flag_line)

설명: 특정 플래그 라인의 값을 flag = 뒤의 문자열로 포맷팅합니다.

매개변수:

flag_file (str): 플래그 파일 경로.

flag_line (int): 플래그가 위치한 줄 번호.


반환값:

(str): 플래그 값만 반환.


사용 예시:

format_flag("status.txt", 1) 
# 반환: "active"


auto_flag(flag_file)

설명: 파일에서 첫 번째로 발견되는 flag = 값의 플래그를 반환합니다.

매개변수:

flag_file (str): 플래그 파일 경로.


반환값:

(str): 자동으로 찾은 플래그 값.


사용 예시:

auto_flag("status.txt") 
# 반환: "active"


auto_find(flag_file, find_str)

설명: 특정 문자열(예: 키-값 쌍)과 일치하는 첫 번째 값을 찾아 반환합니다.

매개변수:

flag_file (str): 플래그 파일 경로.

find_str (str): 검색하려는 키 문자열.


반환값:

(str): 일치하는 값.


사용 예시:

auto_find("status.txt", "al") 
# 반환: "allow.txt"


set_flag(flag_file, flag)

설명: 플래그 파일에서 기존의 플래그 값을 지정된 값으로 업데이트합니다.

매개변수:

flag_file (str): 플래그 파일 경로.

flag (str): 설정하려는 플래그 값.


반환값:

(int): 성공 여부(0).


사용 예시:

set_flag("status.txt", "inactive")



---

3. Allowlist Handling

get_xll(al_file)

설명: Allowlist 파일의 내용을 읽어 리스트 형태로 반환합니다.

매개변수:

al_file (str): Allowlist 파일 경로.


반환값:

(list): Allowlist 항목 리스트.


사용 예시:

get_xll("allow.txt") 
# 반환: ["main.py", "utils.py"]


xll_find_match(al_file, scan_dir)

설명: Allowlist 파일과 지정 디렉터리의 파일 목록을 비교해 일치하는 파일을 반환합니다.

매개변수:

al_file (str): Allowlist 파일 경로.

scan_dir (str): 검색할 디렉터리.


반환값:

(list): Allowlist에 존재하고 디렉터리 내에 있는 파일 이름 리스트.


사용 예시:

xll_find_match("allow.txt", ".")
# 반환: ["main.py"]


xll_find_missing(al_file, scan_dir)

설명: Allowlist 파일과 지정 디렉터리의 파일 목록을 비교해 누락된 파일을 반환합니다.

매개변수:

al_file (str): Allowlist 파일 경로.

scan_dir (str): 검색할 디렉터리.


반환값:

(list): Allowlist에 존재하지만 디렉터리에 없는 파일 이름 리스트.


사용 예시:

xll_find_missing("allow.txt", ".")
# 반환: ["keepalive.py"]


xll_find_unknown(al_file, scan_dir)

설명: Allowlist에 없는 파일을 검색 디렉터리에서 찾아 반환합니다.

매개변수:

al_file (str): Allowlist 파일 경로.

scan_dir (str): 검색할 디렉터리.


반환값:

(list): Allowlist에 없는 파일 이름 리스트.


사용 예시:

xll_find_unknown("allow.txt", ".")
# 반환: ["temp.py"]



---

4. Origin File Handling

unpack_org(org_file, ext='.zip')

설명: 지정된 org_file을 압축 해제합니다.

매개변수:

org_file (str): 압축 파일 경로.

ext (str): 파일 확장자 (기본값: .zip).


반환값:

(int): 성공 여부(0).


사용 예시:

unpack_org("origin.zip")


pack_org(org_dir)

설명: 지정된 디렉터리를 압축 파일로 만듭니다.

매개변수:

org_dir (str): 압축하려는 디렉터리 경로.


반환값:

(int): 성공 여부(0).


사용 예시:

pack_org("backup_dir")


one_pack_org(org_dir, file_list)

설명: 지정된 파일 리스트를 포함하는 새로운 압축 파일을 생성합니다.

매개변수:

org_dir (str): 생성할 디렉터리 이름.

file_list (list): 압축할 파일 리스트.


반환값:

(int): 성공 여부(0).


사용 예시:

one_pack_org("origin", ["main.py", "utils.py"])



---

이 문서는 **utils.py**의 주요 함수와 사용법을 체계적으로 정리한 것으로, 신입 개발자가 프로젝트를 쉽게 이해하고 함수 활용에 능숙해지도록 돕습니다. 추가적인 예제나 자세한 설명이 필요하면 알려주세요!

