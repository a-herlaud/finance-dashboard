# DASHBOARD TOOL BOX

## Common Nomenclature streamlit project

```
my_streamlit_app/
│
├── app.py                  # Main entry point
├── requirements.txt
├── README.md
├── .env
├── .gitignore
│
├── pages/                  # Multi-page Streamlit apps
│   ├── 1_Dashboard.py
│   ├── 2_Analysis.py
│   ├── 3_Chatbot.py
│   └── 4_Settings.py
│
├── components/             # Reusable UI widgets
│   ├── sidebar.py
│   ├── charts.py
│   ├── tables.py
│
├── services/               # Business logic
│   ├── prediction.py
│   ├── analytics.py
│   └── preprocessing.py
│
├── utils/
│   ├── helpers.py
│   ├── config.py
│   ├── constants.py
│   └── logging.py
│
├── assets/
│   ├── images/
│   ├── css/
│   └── icons/
│
└── config/
    ├── settings.yaml
    └── prompts.yaml