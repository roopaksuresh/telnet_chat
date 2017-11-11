# telnet_chat
A simple python app for sending text messages through telnet. Group messages are possible

The app is divided into two
  *Server
  *Client

*Server*
  Program hosts a socket on a given port to initate a chat. It continuously listens to this port and broadcasts any message input at this port to all the user in the client list that it maintains.
  
*Client*
  Program acts as the client interface. Any message can be typed onto the screen and hit [Enter] to send the message. Which is then broadcasted to every user connected to that port using a chat server serving that port.
