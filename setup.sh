@echo off
mkdir %USERPROFILE%\.streamlit\
echo [general] > %USERPROFILE%\.streamlit\credentials.toml
echo email = \"tjibrilmohammed@gmail.com\" >> %USERPROFILE%\.streamlit\credentials.toml
echo [server] > %USERPROFILE%\.streamlit\config.toml
echo headless = true >> %USERPROFILE%\.streamlit\config.toml
echo port = %PORT% >> %USERPROFILE%\.streamlit\config.toml
echo enableCORS = false >> %USERPROFILE%\.streamlit\config.toml
