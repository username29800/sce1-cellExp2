# utils.py functions docs version 24\_11\_11\_0
# 세포 구조 기반 애플리케이션 패키징 라이브러리

이 라이브러리는 플래그, 허용 목록, 파일 패키징 관리를 위한 함수들을 제공합니다. '세포 구조'를 사용하는 애플리케이션의 구성 및 권한 관리를 지원하기 위해 설계되었습니다. 라이브러리는 기본(플래그), 리스트(허용 목록), 오리진(파일 패키징)의 세 가지 주요 섹션으로 구성됩니다.

각 섹션과 함수는 아래에 설명되어 있습니다.

## 섹션 1: 기본 (플래그)

이 섹션의 함수들은 플래그 파일 내 플래그를 관리합니다.

### 함수:

#### `get_flag(flag_file: str, flag_line: int) -> str`

특정 플래그 파일의 지정된 줄에서 플래그를 가져옵니다.

- **매개변수:**
  - `flag_file` (str): 플래그 파일의 경로입니다.
  - `flag_line` (int): 가져올 플래그의 줄 번호입니다.
- **반환값:** `str`: 지정된 줄의 플래그입니다.
- **예시:** `get_flag('flags.txt', 1)`

#### `set_flag(flag_file: str, flag: str) -> int`

특정 플래그 파일 내 플래그를 업데이트합니다.

- **매개변수:**
  - `flag_file` (str): 플래그 파일의 경로입니다.
  - `flag` (str): 설정할 새로운 플래그 값입니다.
- **반환값:** `int`: 항상 0을 반환합니다 (성공 시).
- **예시:** `set_flag('flags.txt', 'new_flag_value')`

#### `list_flag(flag_file: str) -> list`

플래그 파일에서 모든 줄을 읽어 반환합니다.

- **매개변수:**
  - `flag_file` (str): 플래그 파일의 경로입니다.
- **반환값:** `list`: 플래그 파일의 각 줄을 포함하는 리스트입니다.
- **예시:** `list_flag('flags.txt')`

---

## 섹션 2: 리스트 (허용 목록)

허용 목록 파일에서 항목을 추가하거나 삭제하는 기능을 제공합니다.

### 함수:

#### `get_xll(al_file: str) -> list`

허용 목록 파일의 모든 줄을 읽어 반환합니다.

- **매개변수:**
  - `al_file` (str): 허용 목록 파일의 경로입니다.
- **반환값:** `list`: 허용 목록 파일의 각 줄을 포함하는 리스트입니다.
- **예시:** `get_xll('allowlist.txt')`

#### `write_add_to_xll(al_file: str, str_write: str) -> int`

허용 목록 파일에 단일 항목을 추가합니다.

- **매개변수:**
  - `al_file` (str): 허용 목록 파일의 경로입니다.
  - `str_write` (str): 허용 목록 파일에 추가할 문자열입니다.
- **반환값:** `int`: 항상 0을 반환합니다 (성공 시).
- **예시:** `write_add_to_xll('allowlist.txt', 'new_entry')`

#### `write_add_all_to_xll(al_file: str, str_write_list: list) -> int`

허용 목록 파일에 여러 항목을 추가합니다.

- **매개변수:**
  - `al_file` (str): 허용 목록 파일의 경로입니다.
  - `str_write_list` (list): 추가할 문자열 리스트입니다.
- **반환값:** `int`: 항상 0을 반환합니다 (성공 시).
- **예시:** `write_add_all_to_xll('allowlist.txt', ['entry1', 'entry2'])`

#### `list_add_to_xll(al_file: str, str_write: str) -> list`

내부 허용 목록 리스트에 단일 항목을 추가합니다 (파일에는 저장되지 않음).

- **매개변수:**
  - `al_file` (str): 허용 목록 파일의 경로입니다.
  - `str_write` (str): 추가할 문자열입니다.
- **반환값:** `list`: 새로운 항목이 추가된 리스트입니다.
- **예시:** `list_add_to_xll('allowlist.txt', 'temp_entry')`

#### `list_add_all_to_xll(al_file: str, str_write_list: list) -> list`

내부 허용 목록 리스트에 여러 항목을 추가합니다 (파일에는 저장되지 않음).

- **매개변수:**
  - `al_file` (str): 허용 목록 파일의 경로입니다.
  - `str_write_list` (list): 추가할 문자열 리스트입니다.
- **반환값:** `list`: 새로운 항목이 추가된 리스트입니다.
- **예시:** `list_add_all_to_xll('allowlist.txt', ['temp1', 'temp2'])`

#### `list_del_from_xll(al_file: str, str_del: str) -> list`

내부 허용 목록 리스트에서 단일 항목을 제거합니다.

- **매개변수:**
  - `al_file` (str): 허용 목록 파일의 경로입니다.
  - `str_del` (str): 제거할 문자열입니다.
- **반환값:** `list`: 제거된 항목이 반영된 리스트입니다.
- **예시:** `list_del_from_xll('allowlist.txt', 'entry_to_remove')`

#### `list_del_all_from_xll(al_file: str, str_del_list: list) -> list`

내부 허용 목록 리스트에서 여러 항목을 제거합니다.

- **매개변수:**
  - `al_file` (str): 허용 목록 파일의 경로입니다.
  - `str_del_list` (list): 제거할 문자열 리스트입니다.
- **반환값:** `list`: 제거된 항목들이 반영된 리스트입니다.
- **예시:** `list_del_all_from_xll('allowlist.txt', ['remove1', 'remove2'])`

#### `write_del_from_xll(al_file: str, str_del: str) -> int`

허용 목록 파일에서 단일 항목을 제거합니다.

- **매개변수:**
  - `al_file` (str): 허용 목록 파일의 경로입니다.
  - `str_del` (str): 제거할 문자열입니다.
- **반환값:** `int`: 항상 0을 반환합니다 (성공 시).
- **예시:** `write_del_from_xll('allowlist.txt', 'remove_entry')`

#### `write_del_all_from_xll(al_file: str, str_del_list: list) -> int`

허용 목록 파일에서 여러 항목을 제거합니다.

- **매개변수:**
  - `al_file` (str): 허용 목록 파일의 경로입니다.
  - `str_del_list` (list): 제거할 문자열 리스트입니다.
- **반환값:** `int`: 항상 0을 반환합니다 (성공 시).
- **예시:** `write_del_all_from_xll('allowlist.txt', ['remove1', 'remove2'])`

---

## 섹션 3: 오리진 (파일 패키징)

zip 파일을 사용하여 파일 패키징 및 압축 해제를 관리하는 함수입니다.

### 함수:

#### `unpack_org(org_file: str) -> int`

zip 파일을 현재 작업 디렉토리로 압축 해제합니다.

- **매개변수:**
  - `org_file` (str): zip 파일의 경로입니다.
- **반환값:** `int`: 항상 0을 반환합니다 (성공 시).
- **예시:** `unpack_org('archive.zip')`

#### `pack_org(org_dir: str) -> int`

지정된 디렉토리를 zip 파일로 만듭니다.

- **매개변수:**
  - `org_dir` (str): 아카이브할 디렉토리입니다.
- **반환값:** `int`: 항상 0을 반환합니다 (성공 시).
- **예시:** `pack_org('my_directory')`

#### `pre_pack_org(org_dir: str, file_list: list) -> int`

파일 목록을 지정된 디렉토리로 이동합니다.

- **매개변수:**
  - `org_dir` (str): 대상 디렉토리입니다.
  - `file_list` (list): 이동할 파일 목록입니다.
- **반환값:** `int`: 항상 0을 반환합니다 (성공 시).
- **예시:** `pre_pack_org('target_directory', ['file1.txt', 'file2.txt'])`

---

이 라이브러리는 다양한 파일 관리 기능을 제공하여 '세포 구조' 기반 애플리케이션의 플래그 관리, 허용 목록 설정, 파일 패키징 작업을 효과적으로 처리할 수 있도록 돕습니다. 각 섹션은 특정 기능을 담당하며, 플래그 관리와 허용 목록 추가/삭제는 보안 및 접근 제어를 강화하는 데 활용될 수 있습니다. 또한, 파일을 압축하거나 압축을 해제하는 기능은 애플리케이션 배포와 같은 패키징 작업을 보다 수월하게 만듭니다.
