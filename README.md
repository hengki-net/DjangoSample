# 1. 설치 및 설정

<br/>

(1) choco 설치

>@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command " [System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"

→ cmd 껏다켜고 설치 확인

> choco –version

<br/>

(2) 파이썬 설치

> choco install -y python

→ cmd 껏다켜고 설치 확인

> python --version

<br/>

(3) 설치할 폴더 이동 (git clone한 폴더 이동)

> cd DjangoSample

<br/>

(4) venv로 가상화 생성

> python -m venv venv

<br/>

(5) 가상화 실행
> ~\venv\Scripts\activate.bat

<br/>

(4) 사용할 패키지 설치

> pip install django
> pip install djangorestframework
> pip install django-filter
> pip install django-cors-headers
> pip install cx_Oracle

<br/>
