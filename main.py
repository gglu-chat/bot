import socketio  
  
sio = socketio.Client(logger=True, engineio_logger=True)  
  
@sio.on('connect', namespace='/room')  
def on_connect():  
    print('----------Connected to the chatroom----------')
    on_join()
    on_message()
  
@sio.on('disconnect', namespace='/room')  
def on_disconnect():  
    print('----------Disconnected from the chatroom----------')  

@sio.on('join', namespace='/room')
def on_join():
    sio.emit('join', 
             {"type": "join", "nick": 'gglubot', "password": "password", "room": 'chat'}, 
             namespace='/room')

@sio.on('message', namespace='/room')
def on_message():
    sio.emit('message', 
             {"type": "chat", "mytext": "hi"}, 
             namespace='/room')

sio.connect('wss://gglu.onrender.com/socket.io/')  
sio.wait()