1. 프로그램 할 디렉토리를 생성한다. ( fastapi-test )
2. cmd에서 해당 디렉토리로 이동한다.
3. 아래 명령어를 실행한다. 
   git clone https://github.com/coding-eunbong73/fastapi-test.git .
   
4. pycharm으로 프로젝트를 생성한다. 생성시, 위에 생성한 디렉토리를 선택한다.
   프로젝트 생성시, virtual 환경을 venv로 하여 생성한다.


5. pycharm에서 terminal을 연다. (virtual env 환경이 안되어 있으면 활성화 한다.)
   venv/Scripts/activate 실행
   
6. terminal에서 fastapi, requests library 설치한다.
   pip install fastapi[all]
   pip install uvicorn[standard]
   pip install requests
   