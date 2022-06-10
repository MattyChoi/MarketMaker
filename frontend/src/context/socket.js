import socketio from "socket.io-client";
import React from "react";

export const socket = socketio.connect("http://localhost:9001");
export const SocketContext = React.createContext();