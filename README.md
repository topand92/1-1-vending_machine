## 자동 판매기 (Vending Machine)
- 1학년 1학기 전산학기초 개인 과제
- 보고서 PDF 별도

## src_v1
### Info
- main.py 파일에서 실행
- 한계
	- Python을 처음 배웠을 때 했던 과제라서 코드가 난해함
	- 음료수와 현금을 객체로써 활용해 보지 못함

### 구성
- main.py
	- 메인 루프 구현
- basic_module.py
	- 공통으로 필요한 기본 함수 모음
- consumer_module.py
	- 소비자 모드 구현
- admin_module.py
	- 관리자 모드 구현

## src_v2
### Info
- main.py 파일에서 실행
- 개선
	- 음료수와 현금을 객체로 구현
	- 바로 알아보기 어려운 난해한 코드 최소화
- 한계
	- 객체 활용 테스트를 위한 초반부만 구현, 후반부 미구현

### 구성
- main.py
	- 메인 루프 구현
- basic.py
	- 공통으로 필요한 기본 함수 모음(src_v1의 basic_module 역할 계승)
- drink.py
	- 음료수 클래스
- cash.py
	- 현금 클래스
- vending_machine.py
	- 음료수와 현금의 클래스를 받고 자동판매기 클래스의 메소드를 정의