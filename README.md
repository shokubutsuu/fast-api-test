this is a short demo of fast api.

if you are using ssh connection:

SERVER SIDE:
run the following command to activate server on localhost port 8000
uvicorn server:app --host 127.0.0.1 --port 8000

CLIENT SIDE:
1. you need to make a connection to the ssh remote server running the following commmand:
ssh -L 8000:localhost:8000 <USERNAME>@<REMOTE IP> -N -p <PORT>
2. open another termial then run:
python3 client.py
