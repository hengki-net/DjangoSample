# 1. 설치 및 설정

(1) choco 설치

>@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command " [System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"

→ cmd 껏다켜고 설치 확인

> choco –version


(2) 파이썬 설치 

> choco install -y python

→ cmd 껏다켜고 설치 확인

> python --version


(3) 설치할 폴더 이동 (git clone한 폴더 이동)

> cd DjangoSample


(4) venv로 가상화 생성 

> python -m venv venv


(5) 가상화 실행
> ~\venv\Scripts\activate.bat


(4) 사용할 패키지 설치

> pip install django

> pip install djangorestframework

> pip install django-filter

> pip install django-cors-headers

> pip install cx_Oracle

