import streamlit as st
from multiapp import MultiApp
from apps import(
classes,
all,
)

apps = MultiApp()

# Add all your application here
apps.add_app("結果", classes.app)
apps.add_app("分析", all.app)

# The main app
apps.run()
