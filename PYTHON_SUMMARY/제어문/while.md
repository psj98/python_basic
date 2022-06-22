제어문
========

While
----------
* while문의 기본 구조
    #### > 조건문이 참인 동안 계속해서 while문 안의 내용을 반복적으로 수행
    ```python
    while 조건문:
        수행 문장1
        수행 문장2
        수행 문장3
    ```
    ```python
    # ex)
    count = 0
    while count < 5:
        print(count)
        count += 1
    # 0
    # 1
    # 2
    # 3
    # 4    
    ```

* while문 강제로 빠져나가기
    #### > break 사용
    ```python
    count = 0
    while count < 10:
        print(count)
        count += 1
        if count == 5: # count가 5일 경우 강제로 빠져나감
            break
    ```

* while문의 맨 처음으로 돌아가기
    #### > continue 사용
    ```python
    count = 0
    while count < 10:
        count += 1
        if count % 2 == 0:
            continue # 짝수일 경우, while문의 맨 처음으로 돌아감
        print(count)
    ```

* 무한 루프
    #### > 무한 반복 : 빠져나가려면 [Ctrl+C]를 눌러서 나갈 수 있음
    ```python
    while True: 
        수행 문장1 
        수행 문장2
    ```
    ```python
    while True:
        print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")
    ```