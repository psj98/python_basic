입출력
========

파일 읽고 쓰기
----------
* 파일 생성
    ```python
    파일 객체 = open(파일 이름, 파일 열기 모드)
    
    ```

    + 파일 열기 모드
        - r : 읽기 모드 - 파일을 읽기만 할 때 사용
        - w : 쓰기 모드 - 파일에 내용을 쓸 때 사용
            #### > 해당 파일이 이미 존재할 경우, 원래 있던 내용이 모두 사라지고, 해당 파일이 존재하지 않으면 새로운 파일이 생성
        - a : 추가 모드 - 파일의 마지막에 새로운 내용을 추가시킬 때 사용
            ```python
            # ex)
            f = open('test.txt', 'w') # 새로운 파일 생성
            f.close()
            ```

    + 현재 디렉토리에 생성
        ```python
        f = open('C:/ex/test.txt', 'w')
        f.close() # 파일 객체를 닫아 주는 역할
        ```

    + 파일 경로와 슬래시(/)
        #### > 슬래시(/) 사용
        ```python
        'C:/ex/test.txt'
        ```

        #### > 역슬래시(\\) 2개 사용
        ```python
        'C:\\ex\\test.txt'
        ```

        #### > 문자열 앞에 r 문자(Raw String) 덧붙여 사용
        ```python
        # \n과 같은 이스케이프 문자가 있을 경우 대비
        r'C:\note\test.txt'
        ```

* 파일을 쓰기 모드로 열어 출력값 적기
    ```python
    f = open('C:/ex/test.txt', 'w')
    for i in range(1, 6):
        data = f'{i}번째 줄'
        f.write(data) # 파일에 쓰기
    f.close()
    ```

* 프로그램의 외부에 저장된 파일을 읽는 여러 가지 방법
    + readline 함수 이용하기
        ```python
        f = open('C:/ex/test.txt', 'r')
        line = f.readline() # 줄 읽기
        print(line)
        f.close()
        ```

        ```python
        while True:
            line = f.readline()
            if not line: # 더 이상 읽을 줄이 없을 경우
                break
            print(line)
        f.close()
        ```

    + readlines 함수 사용하기
        #### > 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 반환
        ```python
        f = open('C:/ex/test.txt', 'r')
        line = f.readlines()
        for line in lines:
            print(line)
        f.close()
        ```

        #### > 줄 바꿈 문자 제거 - strip() 사용
        ```python
        f = open('C:/ex/test.txt', 'r')
        line = f.readlines()
        for line in lines:
            line = line.strip()
            print(line)
        f.close()
        ```

    + read 함수 사용하기
        #### > 파일의 내용 전체를 문자열로 반환
        ```python
        f = open('C:/ex/test.txt', 'r')
        data = f.read()
        print(data)
        f.close()
        ```

* 파일에 새로운 내용 추가하기
    #### > 파일을 추가 모드('a')로 열면 기존 값 유지 가능
    ```python
    f = open('C:/ex/test.txt', 'a')
    for i in range(6, 11):
        data = f'{i}번째 줄'
        f.write(data)
    f.close()
    ```

* with문과 함께 사용하기
    ```python
    # 기존 방식
    f = open('test.txt', 'w')
    f.write('python is best')
    f.close()
    ```

    #### > 파일을 열고 닫는 것을 자동으로 처리해주기 위해 with문 사용
    ```python
    with open('test.txt', 'w') as f:
        f.write('python is best')
    ```