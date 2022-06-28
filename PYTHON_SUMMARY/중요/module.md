중요
========

모듈
----------
> 모듈(Module)이란, 함수나 변수 또는 클래스를 모아 놓은 파일

> 다른 파이썬 프로글매에서 불러와 사용할 수 있게끔 만든 파이썬 파일

<br>

* 모듈 만들기
    ```python
    # mod1.py
    def add(a, b):
        return a + b

    def sub(a, b):
        return a - b
    ```

    > mod1.py 파일이 바로 모듈

<br>

* 모듈 불러오기
    > 명령 프롬프트 창을 열고 mod1.py를 저장한 디렉토리로 이동한 다음 대화형 인터프리터를 실행

    ```python
    import mod1

    print(mod1.add(3, 4)) # 7
    print(mod1.sub(3, 2)) # 1
    ```
    ```python
    # import의 사용 방법
    import 모듈이름
    ```

    > 모듈 이름은 확장자를 제거한 나머지 (ex. .py를 제거한 mod1)

    #### > 모듈 이름 없이 함수 이름만 쓰고 싶은 경우
    ```python
    from 모듈 이름 import 모듈 함수
    ```
    ```python
    # ex)
    from mod1 import add

    add(3, 4) # 7
    ```

    #### > 여러 개의 함수를 사용하고 싶은 경우
    ```python
    # ex1)
    from mod1 import add, sub
    ```

    ```python
    # ex2)
    from mod1 import *
    ```

<br>

* if \_\_name\_\_ == "\_\_main\_\_":의 의미
    ```python
    # mod1.py
    def add(a, b):
        return a + b
    
    def sub(a, b):
        return a - b

    print(add(3, 4))
    print(sub(4, 3))
    ```

    > 실행 결과
    ```cmd
    C:\python mod1.py
    7
    1
    ```

    > mod1 모듈을 import할 때의 문제
    ```cmd
    >>> import mod1
    7
    1
    ```

    > 문제 방지
    ```python
    # mod1.py
    def add(a, b):
        return a + b
    
    def sub(a, b):
        return a - b

    if __name__ == "__main__":
        print(add(3, 4))
        print(sub(4, 3))    
    ```

    #### > 이렇게 하면 python mod1.py처럼 직접 파일을 실행했을 때 print문이 수행

    <br>

    #### > 대화형 인터프리터나 다른 파일에서 이 모듈을 불러서 사용할 때는 if문 다음 문장이 수행되지 않음

    <br>

* 클래스나 변수 등을 포함한 모듈
    ```python
    # mod2.py
    PI = 3.141592

    class Math:
        def solv(self, r):
            return PI * (r ** 2)

    def add(a, b):
        return a + b
    ```

    ```python
    import mod2

    print(mod2.PI) # 3.141592

    a = mod2.Math()

    print(a.solv(2)) # 12.566368
    print(mod2.add(mod2.PI, 4.4)) # 7.541592
    ```

<br>

* 다른 파일에서 모듈 불러오기
    ```py
    # modtest.py
    import mod2

    result = mod2.add(3, 4)

    print(result)
    ```

    #### > 다른 방법
    1. sys.path.append(모듈을 저장한 디렉토리) 사용하기
        ```cmd
        import sys
        ```

        #### > sys.path는 파이썬 라이브러리가 설치되어 있는 디렉토리를 보여줌
        ```cmd
        sys.path
        ['', 'C:\\Python37, ...]
        ```
        > 파이썬 모듈이 위 디렉토리에 들어있다면 모듈이 저장된 디렉토리로 이동할 필요 없이 바로 불러서 사용할 수 있음

        ```cmd
        sys.path.append("경로")
        ```

    <br>

    1. **PYTHONPATH** 환경 변수 사용하기
        ```cmd
        set PYTHONPATH=경로
        ```
        > set 명령어를 사용하여 **PYTHONPATH** 환경 변수에 mod2.py파일이 있는 **경로** 디렉토리를 설정하면 모듈을 불러와서 사용할 수 있음