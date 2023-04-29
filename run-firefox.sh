#!/bin/bash
python3 -m pytest -v -s --test_object START --driver Firefox --driver-path driver/geckodriver.exe
