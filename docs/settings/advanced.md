# 고급 설정

설정파일(d2r.ini)을 직접 편집하여 고급 설정을 변경할 수 있습니다.

## 설정파일 위치

실행 파일과 같은 폴더의 `d2r.ini`

!!! tip "설정파일 생성"
    **환경설정 → 환경설정 저장/읽기 → 현재 설정을 파일로 저장**

## 주요 설정 항목

### [Settings] 섹션

```ini
[Settings]
version = v3.1                    # 프로그램 버전
digit_size = 2                    # 게임 번호 자릿수
hangul_keyboard = False           # 한/영키 분리 키보드 사용
launcher_wait_timeout = 30        # 배틀넷 런처 대기 시간(초)
layout_count = 7                  # 레이아웃 개수
masking_rate = 0.2                # 마스킹 비율
resize_window = False             # 스크립트 실행 시 창 리사이즈
script_delay_time = 0.09          # 스크립트 명령어 간 지연(초)
server = Korea                    # 기본 서버
token_headless = True             # 토큰 생성 시 브라우저 숨김
token_otp_timeout = 30            # OTP 대기 시간(초)
```

### [Servers] 섹션

```ini
[Servers]
Korea = kr.actual.battle.net
USA = us.actual.battle.net
Europe = eu.actual.battle.net
Test = test.actual.battle.net
```

### [Game Information] 섹션

```ini
[Game Information]
name = MAG                        # 게임 제목 접두어
password = 0402                   # 게임 비밀번호
count = 0                         # 게임 번호
```

## 단축키 설정

### [Hotkeys] 섹션

```ini
[Hotkeys]
ctrl+a = auto                     # 자동
ctrl+n = create                   # 게임 생성
ctrl+j = join                     # 게임 참가
ctrl+x = exit                     # 게임 나가기
ctrl+l = legacy                   # 레거시 모드
ctrl+t = title                    # 창 제목 토글
ctrl+plus = plus                  # 게임 번호 증가
ctrl+- = minus                    # 게임 번호 감소
ctrl+alt+1 = win1                 # 1번 클라이언트 활성화
ctrl+alt+2 = win2                 # 2번 클라이언트 활성화
# ... win3 ~ win10
```

### 단축키 지정 방식

**방법 1: 스크립트명 사용**

```ini
ctrl+8 = custom1
```

`[Scripts]` 섹션에 `custom1`이 정의되어 있어야 함

**방법 2: 스크립트 파일 지정**

```ini
ctrl+8 = scripts\custom1.script
```

상대경로 또는 절대경로 가능, 확장자는 `.script`만 허용

### 사용 가능한 키

- 수식키: `alt`, `ctrl`, `shift`, `windows`
- 방향키: `left alt`, `right alt`, `left ctrl` 등
- 일반키: 알파벳, 숫자
- 숫자패드: `num 0` ~ `num 9`, `num enter`, `num /`

조합 예: `ctrl+shift+a`, `alt+1`

!!! warning "숫자키 구분 불가"
    `num 1`과 `1`은 같은 키로 인식됩니다.

## 스크립트 설정

### [Scripts] 섹션

스크립트 명령어를 정의합니다.

```ini
[Scripts]
create = activate,
    click 850 55,
    # ... (생략)
    send enter,
    sleep 0.2
```

### 스크립트 문법

- 명령어 간: 콤마(`,`)로 구분
- 파라미터 간: 공백으로 구분
- 주석: `#`으로 시작

### 주요 명령어

| 명령어 | 설명 | 예시 |
|--------|------|------|
| `activate` | 창 활성화 | `activate` |
| `click x y` | 좌표 클릭 | `click 850 55` |
| `move x y` | 마우스 이동 | `move 0.5 0.5` |
| `send key` | 키 입력 | `send enter` |
| `copy text` | 클립보드 복사 | `copy {game_name}` |
| `sleep n` | n초 대기 | `sleep 0.5` |
| `beep` | 비프음 | `beep` |
| `resize w h` | 창 크기 조정 | `resize 1280 720` |

### 반복문

```ini
loop {all_games},
    activate,
    beep,
end
```

| 변수 | 설명 |
|------|------|
| `{all_games}` | 모든 게임 |
| `{master_game}` | 메인 게임만 |
| `{slave_games}` | 부 게임들만 |

### 좌표 지정

**고정 좌표**

```ini
click 850 55
```

**비율 좌표** (0 ~ 1 사이 값)

```ini
click 0.5 0.5    # 정중앙
```

## 한/영키 문제

103/106키 한글 키보드 사용 시 단축키가 동작하지 않는 경우:

```ini
hangul_keyboard = True
```

## 스크립트 속도 조정

```ini
script_delay_time = 0.1
```

- 값을 낮추면 빨라짐 (오동작 가능)
- 값을 높이면 느려짐 (안정적)
- 권장: 0.075 ~ 0.15

개별 명령어에 지연:

```ini
create = sleep 1,      # 1초 대기 후 시작
    click 850 55,
    # ...
```
