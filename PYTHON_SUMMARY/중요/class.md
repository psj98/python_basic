중요
========

클래스
----------
* 클래스는 왜 필요한가?
    ```python
    # ex) 더하기 함수 1개
    result = 0

    def add(num):
        global result # 전역 변수 사용
        result += num
        return num

    print(add(3)) # 3
    print(add(4)) # 7
    ```

    ```python
    # ex) 더하기 함수 2개
    result1 = 0
    result2 = 0

    def add1(num):
        global result1
        result1 += num
        return num

    def add2(num):
        global result2
        result2 += num
        return num

    print(add1(3)) # 3
    print(add1(4)) # 7
    print(add2(3)) # 3
    print(add2(4)) # 7
    ```

    #### > 여러 개의 함수가 추가되면 복잡해짐 -> 클래스 사용

    ```python
    class Calculator:
        def __init__(self):
            self.result = 0
        
        def add(self, num):
            self.result += num
            return self.result

    # 객체 생성 (cal1, cal2)
    cal1 = Calculator()
    cal2 = Calculator()

    print(cal1.add(3)) # 3
    print(cal1.add(4)) # 7
    print(cal2.add(3)) # 3
    print(cal2.add(4)) # 7
    ```
    #### > 객체는 각각의 역할을 수행하고 결과값도 독립적인 값을 유지

<br>

* 클래스와 객체
    #### > 클래스(class) : 계속해서 만들어 낼 수 있는 설계 도면
    #### > 객체(object) : 클래스로 만든 피조물
    
    ```python
    # 1개의 클래스로 많은 객체 생성 가능
    class Cookie:
        pass

    # 객체 생성
    a = Cookie()
    b = Cookie()
    ```

    + 객체와 인스턴스의 차이
        #### > 인스턴스 : 클래스로 만든 객체

        > a = Cookie()에서 a는 객체

        > a 객체는 Cookie의 인스턴스

        #### > 즉, 인스턴스는 특정 객체가 어떤 클래스의 객체인지를 관계 위주로 설명할 때 사용

<br>

* 사칙연산 클래스 만들기
    + 클래스를 어떻게 만들지 먼저 구상하기
        #### > 클래스로 만든 객체를 중심으로 어떤 식으로 동작하게 할 것인지 미리 구상한 후, 생각한 것들을 하나씩 해결하면서 완성해나가는 것이 좋음

        1. 객체 생성
        2. 숫자 지정
        3. 결과 반환

    + 클래스 구조 만들기
        ```python
        class FourCal:
            pass
        ```

    + 객체에 숫자 지정할 수 있게 만들기
        #### > 메서드(method) : 클래스 안에 구현된 함수
        ```python
        class FourCal:
            # 메서드
            def setdata(self, first, second):
                self.first = first
                self.second = second
        ```

        - setdata 메서드의 매개변수
            #### > self, first, second 3개의 입력값을 받음
            ```python
            # 실제 호출
            a = FourCal()
            a.setdata(2, 3)
            ```
            > 값 2개 만 전달하는 이유?
              <br>
              - setdata 메서드의 첫 번째 매개변수 self에는 setdata 메서드를 호출한 객체 a가 자동으로 전달되기 때문

            ```python
            # 클래스 이름.메서드 형태로 호출하는 경우
            a = FourCal()
            FourCal.setdata(a, 2, 3)
            ```

        - setdata 메서드의 수행문
            ```python
            def setdata(self, first, second):
                self.first = first
                self.second = second
            ```
            > a.setdata(2, 3)처럼 호출하면 다음과 같이 해석
            ```python
            a.first = 2
            a.second = 3
            ```
            > a 객체에 객체변수 first, second가 생성되고 각각 값 2, 3 저장

            ```python
            a = FourCal()
            b = FourCal()

            a.setdata(2, 3)
            b.setdata(4, 5)

            print(a.first) # 2
            print(b.first) # 4
            ```
            > 클래스로 만든 객체의 객체변수는 다른 객체의 객체변수에 상관없이 독립적인 값을 유지

    + 더하기 기능 만들기
        ```python
        class FourCal:
            def setdata(self, first, second):
                self.first = first
                self.second = second

            def add(self):
                result = self.first + self.second
                return result

        
        a = FourCal()
        a.setdata(2, 3)

        print(a.add()) # 5
        ```

        > result = self.first + self.second는 다음과 같이 해석
        <br>
        -> result = a.first + a.second
        <br>
        -> result = 2 + 3
        
    + 빼기, 곱하기, 나누기 기능 만들기
        ```python
        class FourCal:
            def setdata(self, first, second):
                self.first = first
                self.second = second

            def add(self):
                result = self.first + self.second
                return result

            def sub(self):
                result = self.first - self.second
                return result

            def mul(self):
                result = self.first * self.second
                return result

            def div(self):
                result = self.first / self.second
                return result
        ```

<br>

* 생성자(Constructor)
    #### > 생성자(Constructor)란 객체가 생성될 때 자동으로 호출되는 메서드
    ```python
    # 초기값이 설정되지 않아서 ERROR
    a = FourCal()
    a.add() # ERROR
    ```
    > 파이썬 메서드 이름으로 __init__를 사용하면 생성자가 됨

    ```python
    class FourCal:
        # 생성자(Constructor)
        def __init__(self, first, second):
            self.first = first
            self.second = second

        def setdata(self, first, second):
            self.first = first
            self.second = second

        def add(self):
            result = self.first + self.second
            return result

        def sub(self):
            result = self.first - self.second
            return result

        def mul(self):
            result = self.first * self.second
            return result

        def div(self):
            result = self.first / self.second
            return result
    ```

    > first와 second에 해당되는 값을 전달하여 객체를 생성하면 해결 가능
    ```python
    a = FourCal(2, 3)

    print(a.first) # 2
    print(a.second) # 3
    
    a.add() # 5
    a.mul() # 6
    ```

<br>

* 클래스의 상속
    #### > 상속(Inheritance)이란, 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있게 만드는 것

    ```python
    class 클래스 이름(상속할 클래스 이름)
    ```
    ```python
    # FourCal 클래스를 상속하는 제곱을 구하는 MoreFourCal 클래스 생성
    class MoreFourCal(FourCal):
        def pow(self):
            result = self.first ** self.second
            return result

    a = MoreFourCal(2, 3)
    print(a.add()) # 5
    print(a.pow()) # 8
    ```

    > 상속하는 이유?
    >> 보통 상속은 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경하려고 할 때 사용
    <br>
    >> 하지만, 기존 클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않는 상황이라면 상속 사용

<br>

* 메서드 오버라이딩
    ```python
    # 4를 0으로 나누려고 하기 때문에 ERROR
    a = FourCal(4, 0)
    a.div()
    ```

    #### > FourCal 클래스를 상속하는 SafeFourCal 클래스 생성
    ```python
    class SafeFourCal(FourCal):
        def div(self):
            if self.second == 0:
                return 0
            else:
                return self.first / self.second
    ```

    #### > 메서드 오버라이딩(Overriding) : 부모 클래스(상속한 클래스)에 있는 메서드를 동일한 이름으로 다시 만드는 것
    > 메서드를 오버라이딩하면 부모클래스의 메서드 대신 오버라이딩한 메서드가 호출됨

<br>

* 클래스 변수
    ```python
    class Family:
        lastname = '김'

    print(Family.lastname) # 김
    ```
    > lastname이 클래스 변수
    
    > 클래스이름.클래스변수로 사용 가능

    ```python
    a = Family()

    Family.lastname = '박'

    print(a.lastname) # '박'
    ```
    > 클래스 변수는 클래스로 만든 모든 객체에 공유된다는 특징이 있음

    ```python
    a.lastname = '최'
    print(a.lastname) # 최
    print(Family.lastname) # 박
    ```
    > 객체 변수와 클래스 변수는 상관없음