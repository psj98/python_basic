중요
========

패키지
----------
* 패키지란?
    > 패키지(Packages)는 도트(.)를 사용하여 파이썬 모듈을 계층적으로 관리할 수 있게 해줌
    > <br>
    > 모듈 이름이 A.B인 경우에 A는 패키지 이름, B는 A 패키지의 모듈이 됨

    #### > ex)
        ```
        game/
            __init__.py
            sound/
                __init__.py
                echo.py
                wav.py
            graphic/
                __init__.py
                screen.py
                render.py
            play/
                __init__.py
                run.py
                test.py
        ```

    > game, sound, graphic, play는 디렉토리이고 확장자가 .py인 파일은 파이썬 모듈

    > 패키지 구조로 모듈을 만들면 다른 모듈과 이름이 겹치더라도 더 안전하게 사용 가능

<br>

* 패키지 만들기
    + 패키지 기본 구성 요소 준비하기
        1. 원하는 디렉토리 밑에 game 및 기타 서브 디렉토리를 생성하고 .py 파일들 생성
            ```cmd
            C:/test/game/__init__.py
            C:/test/game/sound/__init__.py
            C:/test/game/sound/echo.py
            C:/test/game/graphic/__init__.py
            C:/test/game/graphic/render.py
            ...
            ```

        2. 각 디렉토리에 \_\_init\_\_.py 파일을 만들어 놓고 내용은 일단 비워둠
         
        3. echo.py 파일
            ```py
            #echo.py
            def echo_test():
                print('echo')
            ```

        4. render.py 파일
            ```py
            #render.py
            def render_test():
                print('render')
            ```

        5. set 명령어로 PYTHONPATH 환경 변수에 해당 디렉토리 추가(여기서는 C:/test)
            ```cmd
            set PYTHONPATH = C:/test
            ```

<br>

* 패키지 안의 함수 실행하기
    1. echo 모듈을 import하여 실행
        ```py
        import game.sound.echo
        game.sound.echo.echo_test() # echo
        ```

    2. echo 모듈이 있는 디렉토리까지를 from ... import하여 실행
        ```py
        from game.sound import echo
        echo.echo_test() # echo
        ```

    3. echo 모듈의 echo_test 함수를 직접 import하여 실행
        ```py
        from game.sound.echo import echo_test
        echo_test() # echo
        ```

    4. 불가능한 것
        ```py
        import game
        game.sound.echo.echo_test() # ERROR
        ```
        > game 디렉토리의 \_\_init\_\_.py에 정의한 것만 참조 가능

        ```py
        import game.sound.echo.echo_test # ERROR
        ```

        > 도트 연산자(.)를 사용해서 import a.b.c처럼 import할 때 가장 마지막 항목인 c는 반드시 모듈 또는 패키지여야만 함

<br>

* \_\_init\_\_.py의 용도
    > \_\_init\_\_.py 파일은 해당 디렉토리가 패키지의 일부임을 알려주는 역할

    > 만약 \_\_init\_\_.py 파일이 없다면 패키지로 인식되지 X (python3.3버전부터는 상관 X)

    ```py
    from game.sound import *
    echo.echo_test() # ERROR
    ```

    > 특정 디렉토리의 모듈을 *를 사용하여 import할 때에는 \_\_all\_\_ 변수를 설정하고 import할 수 있는 모듈을 정의해주어야 함
    ```cmd
    C:/test/game/sound/__init__.py
    __all__ = ['echo']
    ```

<br>

* relative 패키지
    ```py
    # render.py 모듈이 echo.py 모듈을 사용하고 싶을 때
    from game.sound.echo import echo_test

    def render_test():
        print('render')
        echo_test()
    ```

    ```py
    from ..sound.echo import echo_test
    
    def render_test():
        print('render')
        echo_test()
    ```
    > ..은 render.py 파일의 부모 디렉토리를 의미
    <br>
    
    > . : 현재 디렉토리