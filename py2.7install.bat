cd C:\
@powershell -NoProfile -ExecutionPolicy unrestricted -Command "iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))" && SET PATH=%PATH%;%systemdrive%\chocolatey\bin
cinst python
REM This Script will install Chocolatey and Python 2.7 (2.7.6 to be exact), which is what my program is written in.
