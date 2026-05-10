@echo off
cd /d "E:\vishnu viswas\ai_valuation"

call ai_valuation\Scripts\activate

start "" streamlit run .\src\ui\streamlit_app.py