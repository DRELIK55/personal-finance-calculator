#!/bin/bash
echo "=== Flake8 Analysis ===" > analysis_report.txt
flake8 . >> analysis_report.txt
echo -e "\n=== Pylint Analysis ===" >> analysis_report.txt
pylint calculator.py operations.py main.py >> analysis_report.txt
echo -e "\n=== Bandit Analysis ===" >> analysis_report.txt
# Добавили --encoding utf-8 для корректной работы с русскими буквами
PYTHONIOENCODING=utf-8 bandit -r . --encoding utf-8 >> analysis_report.txt
echo "Анализ завершен. Результаты в analysis_report.txt"