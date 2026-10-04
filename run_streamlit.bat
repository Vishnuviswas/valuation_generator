@echo off

cd /d D:\ai_valuation

call ai_valuation_env\Scripts\activate

python -m streamlit run src\ui\streamlit_app.py

pause