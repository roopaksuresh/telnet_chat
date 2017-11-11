# telnet_chat
A simple python app for sending text messages through telnet. Group messages are possible

The app is divided into two

  1. *Server*
  2. *Client*

*Server*
  Program hosts a socket on a given port to initate a chat. It continuously listens to this port and broadcasts any message input at this port to all the user in the client list that it maintains.
  
*Client*
  Program acts as the client interface. Any message can be typed onto the screen and hit [Enter] to send the message. Which is then broadcasted to every user connected to that port using a chat server serving that port.
  
PS: the program was initially copied so that i could learn python sockets. I then tweaked it so that *username* is shown which earlier used to be a user id during the chat.
