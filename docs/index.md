# 디아2 멀티로더

## 프로그램 소개

이 프로그램은 한 컴퓨터에서 여러 "디아블로2 리저렉션" (이하 D2R) 클라이언트를 실행하는 프로그램입니다. 컴퓨터 사양만 충분하다면 실행할 수 있는 클라이언트의 개수는 제한 없습니다.

![멀티로더 실행](images/i014947699719.gif)

프로그램에 사용된 대표 아이콘 이미지는 "문화포털"에서 서비스 되는 전통문양을 활용하였습니다. (링크: <https://www.culture.go.kr>) 강릉상석 귀신문 외에 5개 정도의 귀신문이 돌아가면서 적용됩니다. 메뉴 및 UI 아이콘은 오픈소스 아이콘 라이브러리 [Lucide](https://lucide.dev/) (ISC 라이선스)를 사용합니다.

![귀신문1](images/icon1.png)
![귀신문2](images/그림2.png)
![귀신문3](images/그림3.png)
![귀신문4](images/그림4.png)
![귀신문5](images/그림5.png)

!!! danger "이용 전 반드시 읽어주세요"
    **하나의 컴퓨터에서 D2R을 여러 개 실행하는 것은 블리자드가 허용하는 방식이 아니며, 계정이 영구 정지될 수 있습니다.**
    안전한 다중 실행 방법은 존재하지 않습니다. 이 프로그램에는 탐지를 회피하기 위한
    기능이 전혀 들어 있지 않습니다.

    **이 프로그램의 사용으로 발생하는 모든 문제에 대한 책임은 사용자 본인에게 있습니다.**
    자세한 내용은 아래 [주의사항](#주의사항)을 읽어주세요. 같은 내용을 프로그램 최초
    실행 시에도 안내합니다.

## 주의사항

### 배틀넷 계정 정지

D2R을 하나의 컴퓨터에서 여러 개 실행하는 것은 블리자드가 허용하는 방식이 아닙니다. 블리자드는 운영정책에서 다음과 같이 정하고 있습니다.

*제3자 외부 프로그램은 회사가 배포하는 프로그램 내에 포함되지 않거나, 별도로 이루어진 파일 또는 프로그램이며 이를 통하여 회사가 의도하지 않거나 허용하지 않은 이득을 취하고자 하는 프로그램입니다. 또한, 일반적인 고객들은 얻을 수 없는 게임 및 서비스 정보를 얻거나 파일을 조작 또는 변환 하는 프로그램 역시 포함 됩니다. 이러한 허용되지 않은 제3자 외부 프로그램의 개발, 공유, 배포, 이용할 경우 제재가 진행될 수 있습니다. 허용되지 않는 제3자 외부 프로그램 사용이 확인되면 다음과 같은 제재를 받을 수 있습니다. 1) 계정 정지*

- 참고링크: "배틀넷 운영정책", <https://kr.battle.net/support/ko/article/75793>
  (참고용 주소이며 운영사 사정으로 바뀔 수 있습니다)

**안전한 다중 실행 방법은 존재하지 않습니다.** 멀티 클라이언트를 쓰던 이용자의 계정이 정지된 사례가 다수 보고되고 있습니다. 다만 블리자드가 정지 사유를 밝히지 않으므로 그 정지가 멀티 클라이언트 사용 때문이었는지는 확인된 바 없습니다. 원인으로 확인되지 않았다는 것이 원인이 아니라는 뜻은 아니며, 마찬가지로 안전하다는 뜻도 아닙니다.

블리자드가 무엇을 어떻게 탐지하는지, 언제 제재하는지는 공개되어 있지 않습니다. 따라서 **지금까지 정지되지 않았다는 사실은 앞으로도 안전하다는 근거가 되지 않습니다.** 제재는 예고 없이, 사용한 시점보다 한참 뒤에 이루어질 수 있습니다.

### 탐지 회피 기능은 없습니다

이 프로그램에는 블리자드의 안티치트(Warden) 탐지를 회피하기 위한 우회 알고리즘이나 은폐 기능이 전혀 들어 있지 않습니다. 여러 클라이언트를 실행하고 창을 배치하는 편의 기능만 제공합니다.

그러므로 탐지되었을 때 이 프로그램이 이용자를 보호해 줄 수단은 아무것도 없습니다.

### PC방 사용 금지

명령줄 방식으로 실행하면 계정과 비밀번호가 프로세스의 명령줄 인자로 남아, 아래 이미지와 같이 작업 관리자에서 평문으로 보입니다. 같은 컴퓨터를 쓰는 사람은 물론, **실행 중인 프로그램의 명령줄을 훑는 악성코드(인포스틸러 등)도 이를 그대로 가져갈 수 있습니다.**

PC방 등 공용 컴퓨터나 보안이 취약한 환경에서는 절대로 사용하지 마십시오.

![작업관리자](images/taskmgr.png)

### 계정 파일 암호화

계정 파일은 **암호화 키를 설정한 경우에만** 암호화되어 저장됩니다. 키를 설정하지 않으면 계정 정보가 암호화되지 않은 상태로 저장됩니다. 설정 방법은 [상세 설정](settings/advanced.md)을 참고하세요.

어느 경우든 사용하는 컴퓨터 자체가 안전하지 않으면 계정 정보는 보호되지 않습니다.

### 책임의 범위

이 프로그램을 내려받거나 설치하거나 실행함으로써 생기는 계정 정지, 아이템과 캐릭터의 손실, 그 밖의 모든 손해에 대한 책임은 **이용자 본인에게** 있습니다.

블리자드가 제재를 할지, 한다면 언제 어느 계정에 할지는 제작자가 알 수도 없고 관여할 수도 없는 영역입니다. 그래서 제작자는 다음을 하지 않습니다.

- 계정 정지에 대한 이의 제기나 계정 복구를 대신하거나 도와드리지 않습니다.
- 계정 정지, 아이템과 캐릭터의 손실에 대해 금전적인 보상이나 배상을 하지 않습니다.
- 이 프로그램의 사용법을 안내하거나 문제를 해결해 드릴 의무를 지지 않습니다. 후원을 하셨더라도 마찬가지입니다.

이 프로그램은 어떠한 보증도 없이 "있는 그대로" 제공됩니다. 다만 위 내용이 법률상 배제할 수 없는 책임까지 면제한다는 뜻은 아닙니다.

이 프로그램은 개인적인 목적으로 만들어져 무상으로 배포됩니다. 다운로드와 사용에 어떠한 대가도 받지 않습니다.

위 내용을 읽고 이해했으며 그 위험을 스스로 감수하는 데 동의하는 경우에만 사용해 주십시오. 동의하지 않으시면 이 프로그램을 사용하지 마시고 삭제해 주십시오.

## 구현방법

파이썬(Python)으로 구현되어 있습니다. PySide, win32api, subprocess, Crypto 가 주요 사용된 모듈입니다. UI는 LGPL인 PySide 사용합니다. 프로세스를 찾거나 핸들을 닫거나 하는 프로세스 관련된 처리는 win32api를 사용합니다. 클라이언트 명령줄 실행에는 subprocess 모듈을 사용합니다. 암호화에는 Crypto 모듈을 사용합니다. 스크립트는 keyboard, mouse 모듈을 사용해서 구현했습니다.
개발에 사용된 프로그램 및 모듈의 라이선스와 홈페이지는 아래와 같습니다.

|모듈|라이선스|홈페이지|
|-----|-----|-----|
|Lucide Icons|ISC|<https://lucide.dev/>|
|comtypes|MIT|<https://github.com/enthought/comtypes>|
|debugpy|MIT|<https://github.com/microsoft/debugpy>|
|dxcam|MIT|<https://github.com/ra1nty/DXcam>|
|keyboard|MIT|<https://github.com/boppreh/keyboard>|
|mouse|MIT|<https://github.com/boppreh/mouse>|
|numpy|BSD 3-Clause|<https://numpy.org/>|
|Pillow|HPND|<https://python-pillow.org/>|
|psutil|BSD 3-Clause|<https://github.com/giampaolo/psutil>|
|pycryptodome|BSD / Public Domain|<https://www.pycryptodome.org/>|
|PyInstaller|GPL 2.0 (w/ exception)|<https://pyinstaller.org/>|
|pyperclip|BSD|<https://github.com/asweigart/pyperclip>|
|PySide6|LGPL v3|<https://wiki.qt.io/Qt_for_Python>|
|PyQtDarkTheme-fork|MIT|<https://pyqtdarktheme.readthedocs.io>|
|pywin32|PSF|<https://github.com/mhammond/pywin32>|
|pywinstyles|CC0|<https://github.com/Akascape/py-window-styles>|
|requests|Apache 2.0|<https://github.com/psf/requests>|
|screeninfo|MIT|<https://github.com/rr-/screeninfo/tree/master>|
|selenium|Apache 2.0|<https://www.selenium.dev/>|
|vdf|MIT|<https://github.com/ValvePython/vdf>|
|webdriver-manager|Apache 2.0|<https://github.com/SergeyPirogov/webdriver_manager>|
|winocr|MIT|<https://github.com/GitHub30/winocr>|
|zipencrypt|MIT|<https://github.com/devthat/zipencrypt>|
|vscode|MIT|<https://github.com/microsoft/vscode>|

## 주요 기능

- **멀티 클라이언트 실행** - 컴퓨터 사양만 충분하다면 제한 없이 여러 클라이언트 실행합니다. [링크](features/multi-launcher.md)
- **다양한 인증 방식** - 명령줄, 웹 토큰, 배틀넷 런처 방식 지원합니다. [링크](features/account-management.md)
- **자동화 스크립트** - 게임 생성, 참가, 나가기 등 자동화를 지원합니다. [링크](features/script.md)
- **창 관리** - 게임 클라이언트 창의 레이아웃 저장 및 적용을 지원합니다. [링크](features/layout-manager.md)
- **테러존 트래커** - 현재/다음 테러존 지역 표시합니다. [링크](features/terror-zone.md)
- **우버 트래커** - 우버 디아블로 상태를 추적합니다. [링크](features/uber-tracker.md)

## 빠른 시작

- [설치](getting-started/installation.md) - 프로그램 다운로드 및 설치 방법
- [첫 실행](getting-started/first-run.md) - 기본 설정 및 계정 등록 방법
- [멀티 런처](features/multi-launcher.md) - 여러 클라이언트 실행하는 방법

## 실행 방식

먼저 인증 방식에 대해서 이해가 필요합니다. 명령줄(command line) 방식과 토큰(token) 방식이 있습니다. 명령줄 방식은 "디아블로2 오리지날"부터 제공하던 기능으로 아이디, 비밀번호를 게임 클라이언트(d2r.exe)의 파라미터로 주고 실행하여 인증하는 방식입니다. 실제로 도스창에서 아래 예와 같이 입력해서 실행하면 해당 계정으로 접속됩니다.
```
  d2r.exe -username abc@abc.net -password mypassword
```
참고 링크: <https://d2mods.info/forum/viewtopic.php?t=67329>
토큰 방식은 아이디, 비밀번호를 이용해서 미리 인증을 하고 이때 생성된 토큰으로 로그인 하는 방식입니다. 토큰은 지하철 승차권이나 놀이공원 입장권과 유사하다고 생각하시면 됩니다. 정확하게는OAuth방식이나 이후 편의상 토큰 방식으로 호칭하겠습니다. 배틀넷 런처도 내부적으로는 토큰 방식을 사용합니다.
이 프로그램에서는 아래와 같이 세가지 인증방식을 지원합니다.

|인증방식|내용|비고|
|-----|-----|-----|
|명령줄|아이디, 비밀번호를 파라미터로 주고 명령줄로 실행|인증기 사용 불가|
|웹 토큰|배틀넷 사이트에서 인증, 웹 토큰 생성, 저장 웹 토큰으로 실행|인증기 사용 가능|
|배틀넷 런처|배틀넷 런처를 스크립트로 제어 실행|인증기 사용 가능|

계정 설정에서 인증방식을 지정할 수 있습니다. 모든 인증방식에는 아이디, 비밀번호가 필요합니다. 웹 토큰 방식은 추가로 웹 토큰을 발급받아서 저장해야 합니다. 배틀넷 런처 방식은 배틀넷 런처를 스크립트로 제어하여 실행합니다. ~~블리자드에서 '23년 10월부터 위에 명령줄 방식으로 아시아(한국) 서버 접속하는 것을 차단했습니다.~~ 다시 명령줄 방식을 지원합니다. 이 프로그램에서는 추가로 웹 토큰 방식이나 배틀넷 런처를 통한 실행과 접속을 사용합니다. 인증 방식은 OTP를 사용하는 경우에는 "웹 토큰" 방식을 그 외에는 "명령줄" 방식을 추천합니다. "배틀넷 런처" 방식은 "웹 토큰" 방식이 구현되기 전에 임시적으로 사용한 방식이고 스크립트를 이용해서 **비동기적**으로 실행되기에 문제가 많이 발생합니다.

!!! tip "추천"
    OTP 사용 시 **웹 토큰** 방식, 그 외에는 **명령줄** 방식을 추천합니다.

## 멀티 클라이언트

D2R클라이언트의 중복 실행을 막기 위해서 프로세스에서 특정 핸들을 확인하는데, 멀티 클라이언트 실행하기 위해서 아래의 해당하는 핸들을 닫습니다.
```
  \Sessions\[임의숫자]\BaseNamedObjects\DiabloII Check For Other Instances
```
- 참고 링크: <https://us.forums.blizzard.com/en/d2r/t/how-to-multiple-d2r-instances-requires-two-accounts/60546>

이 프로그램에서는 자체 구현한 함수를 이용해서 해당하는 핸들을 닫습니다. process explorer(이하 PE)로 하는 방법과 같은 방식입니다.

## 문의 및 지원

GitHub: [saintsc-ai/d2r-manual](https://github.com/saintsc-ai/d2r-manual)
