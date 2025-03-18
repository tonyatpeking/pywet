cd ..\..
REM make pywet-pypi-test directory
mkdir pywet-pypi-test
cd pywet-pypi-test
uv run --refresh-package pywet --with pywet --no-project -- python -c "import pywet; pywet.main()"