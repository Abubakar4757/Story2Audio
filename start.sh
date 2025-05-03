#!/bin/bash

# Start gRPC server in the background
python run_server.py &

# Start frontend (e.g., Streamlit)
streamlit app.py