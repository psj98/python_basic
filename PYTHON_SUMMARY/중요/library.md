중요
========

라이브러리
----------
* sys
    > 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈

    + sys.argv - 명령 행에서 인수 전달하기
        ```py
        # argv_test.py
        import sys

        print(sys.argv)
        ```

        ```cmd
        python argv_test.py you need python
        ['argv_test.py', 'you', 'need', 'python']

    + sys.exit - 강제로 스크립트 종료하기

        ```cmd
        sys.exit()
        ```

    + sys.path - 자신이 만든 모듈을 불러와 사용하기
        > 파이썬 모듈들이 저장되어 있는 위치를 나타냄

        ```py
        import sys

        sys.path # [모듈 저장 위치]
        ```
        <br>

        > 경로 추가
        ```py
        import sys

        sys.path.append("C:/doit/mymod")
        ```

<br>

* pickle
    > 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈
    
    > ex) pickle 모듈의 dump 함수를 사용하여 딕셔너리 객체인 data를 그대로 파일에 저장하는 방법
    ```py
    import pickle

    f = open('test.txt', 'wb')

    data = {1: 'py', 2: 'good'}
    pickle.dump(data, f)

    f.close()
    ```

    ```py
    import pickle

    f = open('test.tx', 'rb')
    data = pickle.load(f)
    
    print(data) # {2: 'good', 1: 'py'}
    ```

<br>

* os
    > 환경 변수나 디렉토리, 파일 등의 OS 자원을 제어할 수 있게 해주는 모듈

    + os.environ - 내 시스템의 환경 변수값을 알고 싶을 때
        ```py
        # 현재 시스템의 환경 변수 값을 딕셔너리 객체로 반환
        import os

        os.environ # environ({'PROGRAMFILES': 'C:\\Program Files', ...})
        ```

        ```py
        # PATH 환경 변수 내용
        os.environ['PATH'] # C:\\ProgramData\\ ...
        ```

    + os.chdir - 디렉토리 위치 변경
        > 현재 디렉토리 위치 변경 가능
        ```py
        os.chdir('C:\WINDOWS')
        ```

    + os.getcwd - 디렉토리 위치 반환
        > 현재 디렉토리 위치 반환
        ```py
        os.getcwd() # C:\WINDOWS
        ```

    + os.system - 시스템 명령어 호출
        ```py
        os.system('dir')
        ```

    + os.popen - 실행한 시스템 명령어의 결괏값 돌려받기
        ```py
        f = os.popen("dir")

        print(f.read()) # 파일 객체 내용 보기
        ```

    + 기타 유용한 os 관련 함수
        - os.mkdir(디렉토리)
            > 디렉토리 생성

        - os.rmdir(디렉토리)
            > 디렉토리 삭제. 단, 디렉토리가 비어있어야 삭제 가능

        - os.unlink(파일)
            > 파일 지움

        - os.rename(src, dst)
            > src라는 이름의 파일을 dst라는 이름으로 변경

<br>

* shutil
    > 파일을 복사해주는 모듈
        
    > 디렉토리 이름일 경우, 파일 이름으로 디렉토리에 복사

    > 동일한 파일 이름이 있을 경우 덮어씀

    ```py
    # src를 dst로 복사
    import shutil

    shutil.copy('src.txt', 'dst.txt')
    ```

<br>

* glob
    > 특정 디렉토리에 있는 파일 이름 모두를 알아야 할 경우 사용

    + glob(pathname) - 디렉토리에 있는 파일들을 리스트로 만들기
        > *, ? 등 메타 문자를 써서 원하는 파일만 읽어들일 수 있음

        ```py
        # aa로 시작하는 파일을 모두 찾아서 읽어들임
        import glob

        glob.glob('C:/test/aa*')
        ```

<br>

* tempfile
    > 파일을 임시로 만들어서 사용할 때 유용

    + tempfile.mkstemp() - 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 반환
        ```py
        import tempfile
        filename = tempfile.mkstemp()
        filename # 'C:\WINDOWS...\~-275151-0'
        ```

    + tempfile.TemporaryFile() - 임시 저장 공간으로 사용할 파일 객체 반환
        > 기본적으로 wb 모드를 가짐

        > f.close()가 호출되면 파일 객체는 자동으로 사라짐

        ```py
        import tempfile

        f = tempfile.TemporaryFile()

        f.close()
        ```

<br>

* time
    + time.time
        > UTC(협정 세계 표준시)를 사용하여 현재 시간을 실수 형태로 반환

        > 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초 단위로 반환

        ```py
        import time
        
        time.time()
        ```

    + time.localtime
        > time.time()이 돌려준 실수값을 연도, 월, 일, 시, 분, 초, ... 의 형태로 바꿔주는 함수

        ```py
        time.localtime(time.time()) # time.struct_time(tm_year=2013, tm_mon=5, tm_mday=21, tm_hour=16, tm_min=48, tm_sec=42, tm_wday=1, tm_yday=141, tm_isdst=0)
        ```

    + time.asctime
        > time.localtime에 의해 반환된 튜플 형태의 값을 인수로 받아 날짜와 시간을 알아보기 쉬운 형태로 돌려줌

        ```py
        time.asctime(time.localtime(time.time())) # 'Sat Apr 28 20:50:20 2001'
        ```

    + time.ctime
        > time.asctime(time.localtime(time.time()))을 간단하게 표시

        > 현재 시간만 반환

        ```py
        time.ctime() # 'Sat Apr 28 20:56:31 2001'
        ```

    + time.strftime
        > 시간에 관계된 것을 세밀하게 표현하는 여러 가지 포맷 코드 제공

        ```py
        time.strftime('출력할 형식 포맷 코드', time.localtime(time.time()))
        ```

        - %a : 요일 줄임말
            > ex) Mon
        - %A : 요일	
            > ex) Monday
        - %b : 달 줄임말	
            > ex) Jan
        - %B : 달
            > ex) January
        - %c : 날짜와 시간 출력
            > ex) 06/01/01 17:22:21
        - %d : 날(day)
            > ex) [01, 31]
        - %H : 시간(hour) - 24시간 출력 형태
            > ex) [00, 23]
        - %I : 시간(hour) - 12시간 출력 형태
            > ex) [01, 12]
        - %j : 1년 중 누적 날짜
            > ex) [001, 366]
        - %m : 달
            > ex) [01, 12]
        - %M : 분
            > ex) [01, 59]
        - %p : AM or PM
            > ex) AM
        - %S : 초
            > ex) [00, 59]
        - %U : 1년 중 누적 주 - 일요일을 시작으로
            > ex) [00, 53]
        - %w : 숫자로 된 요일
            > ex) [0(일요일), 6]
        - %W : 1년 중 누적 주 - 월요일을 시작으로
            > ex) [00, 53]
        - %x : 현재 설정된 로케일에 기반한 날짜 출력
            > ex) 06/01/01
        - %X : 현재 설정된 로케일에 기반한 시간 출력
            > ex) 17:22:21
        - %Y : 년도 출력
            > ex) 2001
        - %Z : 시간대 출력
            > ex) 대한민국 표준시
        - %% : 문자
            > ex) %
        - %y : 세기부분을 제외한 년도 출력
            > ex) 01

            ```py
            import time

            time.strftime('%x', time.localtime(time.time())) # '05/01/01'
            time.strftime('%c', time.localtime(time.time())) # '05/01/01 17:22:21'
            ```

    + time.sleep
        > 일정한 시간 간격을 두고 루프 실행 가능
        ```py
        # 1초 간격
        import time

        for i in range(10):
            print(i)
            time.sleep(1)
        ```

<br>

* calendar
    > 달력을 볼 수 있게 해주는 모듈

    + calendar.calendar(연도) - 그 해의 전체 달력을 볼 수 있음
        ```py
        import calendar

        print(calendar.calendar(2022))
        ```

        ```py
        # 위와 동일
        calendar.prcal(2022)
        ```

        ```py
        # 2022년 6월의 달력만 보여줌
        calendar.prmonth(2022,6)
        ```

    + calendar.weekday
        > weekday(연도, 월, 일) - 그 날짜에 해당하는 요일 정보 반환

        > 월요일 0, 화요일 1, 수요일 2, 목요일 3, 금요일 4, 토요일 5, 일요일 6 반환

        ```py
        calendar.weekday(2015, 12, 31) # 3
        ```

    + calendar.monthrange
        > monthrange(연도, 월) - 입력받은 달의 1일이 무슨 요일인지와 그 달이 며칠까지 있는지를 튜플 형태로 반환

        ```py
        calendar.monthrange(2015,12) # (1, 31)
        ```

<br>

* random
    > 난수(규칙이 없는 임의의 수)를 발생시키는 모듈

    ```py
    import random

    random.random() # 랜덤 실수 값
    ```

    ```py
    # 1 ~ 10 사이의 정수 중 랜덤 값
    random.randint(1, 10)
    ```

    ```py
    # ex)
    import random

    def random_pop(data):
        number = random.randint(0, len(data) - 1)

        return data.pop(number)

    if __name__ == "__main__":
        data = [1, 2, 3, 4, 5]

        while data: 
            print(random_pop(data))

    # 2
    # 4
    # 1
    # 3
    # 5
    ```

    > choice 함수 - 입력으로 받은 리스트에서 무작위로 하나를 선택하여 반환
    ```py
    # ex) 더 직관적으로
    def random_pop(data):
        number = random.choice(data)
        data.remove(number)

        return number
    ```

    > random.shuffle - 리스트의 항목을 무작위로 섞음
    ```py
    data = [1, 2, 3, 4, 5]
    random.shuffle(data)
    ```

<br>

* webbrowser
    > 자신의 시스템에서 사용하는 기본 웹 브라우저를 자동으로 실행하는 모듈

    ```py
    import webbrowser
    
    webbrowser.open('http://google.com')
    ```

    > open 함수는 웹 브라우저가 이미 실행된 상태라면 입력 주소로 이동
    
    > 만약 웹 브라우저가 실행되지 않은 상태라면 새로 웹 브라우저를 실행한 후 해당 주소로 이동

    <br>

    > open_new 함수 : 이미 웹 브라우저가 실행된 상태이더라도 새로운 창으로 해당 주소가 열림
    ```py
    webbrowser.open_new("http://google.com")
    ```

<br>

* threading
    > 한 프로세스 안에서 2가지 또는 그 이상의 일을 동시에 수행 가능

    ```py
    # ex) 총 25초 걸림
    import time

    def long_task():  # 5초의 시간이 걸리는 함수
        for i in range(5):
            time.sleep(1)  # 1초간 대기
            print("working:%s\n" % i)

    print("Start")

    for i in range(5):  # long_task를 5회 수행
        long_task()

    print("End")
    ```

    ```py
    # ex) thread 사용 (5초)
    import time
    import threading # 스레드를 생성 모듈

    def long_task():
        for i in range(5):
            time.sleep(1)
            print("working:%s\n" % i)

    print("Start")

    threads = []
    for i in range(5):
        t = threading.Thread(target = long_task)  # 스레드 생성
        threads.append(t) 

    for t in threads:
        t.start()  # 스레드를 실행한다.

    print("End")
    ```
    > 위의 경우 Start와 End가 먼저 출력되고 그 이후 스레드의 결과가 출력됨

    ```py
    # ex) 오류 수정
    import time
    import threading

    def long_task():
        for i in range(5):
            time.sleep(1)
            print("working:%s\n" % i)

    print("Start")

    threads = []
    for i in range(5):
        t = threading.Thread(target=long_task)
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()  # join으로 스레드가 종료될때까지 기다

    print("End")
    ```