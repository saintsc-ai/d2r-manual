"""MkDocs 로컬 미리보기 서버

사용법:
    py serve.py          포그라운드 실행 (live reload, Ctrl+C로 종료)
    py serve.py start    백그라운드 실행
    py serve.py stop     백그라운드 서버 종료
    py serve.py restart  백그라운드 서버 재시작
"""

import os
import signal
import subprocess
import sys

PID_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".mkdocs.pid")
WORK_DIR = os.path.dirname(os.path.abspath(__file__))


def run():
    """포그라운드 실행 (폴링 방식 파일 감시로 live reload 지원)"""
    # watchdog의 네이티브 감시가 D: 드라이브에서 안 되므로 폴링 방식으로 강제 전환
    import watchdog.observers
    from watchdog.observers.polling import PollingObserver
    watchdog.observers.Observer = PollingObserver

    os.environ["PYTHONIOENCODING"] = "utf-8"
    os.chdir(WORK_DIR)

    from mkdocs.commands.serve import serve
    serve(dev_addr="127.0.0.1:8000")


def start():
    """백그라운드 실행"""
    if os.path.exists(PID_FILE):
        with open(PID_FILE) as f:
            pid = int(f.read().strip())
        try:
            os.kill(pid, 0)
            print(f"이미 실행 중입니다 (PID: {pid})")
            print("http://127.0.0.1:8000/d2r-manual/")
            return
        except OSError:
            os.remove(PID_FILE)

    os.environ["PYTHONIOENCODING"] = "utf-8"
    proc = subprocess.Popen(
        [sys.executable, "-m", "mkdocs", "serve"],
        cwd=WORK_DIR,
        creationflags=subprocess.CREATE_NEW_PROCESS_GROUP,
    )
    with open(PID_FILE, "w") as f:
        f.write(str(proc.pid))
    print(f"서버 시작 (PID: {proc.pid})")
    print("http://127.0.0.1:8000/d2r-manual/")


def stop():
    if not os.path.exists(PID_FILE):
        print("실행 중인 서버가 없습니다.")
        return

    with open(PID_FILE) as f:
        pid = int(f.read().strip())
    try:
        os.kill(pid, signal.SIGTERM)
        print(f"서버 종료 (PID: {pid})")
    except OSError:
        print(f"프로세스({pid})가 이미 종료되었습니다.")
    os.remove(PID_FILE)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else None
    if cmd is None:
        run()
    elif cmd == "start":
        start()
    elif cmd == "stop":
        stop()
    elif cmd == "restart":
        stop()
        start()
    else:
        print(__doc__)
