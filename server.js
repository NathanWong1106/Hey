const express = require('express');
const app = express(); // app setup
const http = require('http');
const socket = require('socket.io');
const server = http.createServer(app);
const net = require('net');
const fs = require('fs');

var cam_state = new Map();

/* static files
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});*/

server.listen(3000, function(){
  console.log('listening on *:3000');
});

var io = socket(server) // socket setup

io.on('connection', (socket) => {
    console.log('User connected');
    id = "Employee 1"; // payload.id from cameras
    state = true; // payload.state from cameras
    if(id.includes("Camera")){
        socket.join("cam"); // camera room
        room = "cam"
        
    } else if(id.includes("Employee")){
        socket.join("emp"); // employee room
        room = "emp"
    }
    socket.on("receive state", () => { // payload
        cam_state.set(id, state);
    })
    console.log(cam_state);
    socket.on("receive ping", () => { // from employees, 5-sec intervals
        socket.to("emp").emit(cam_state) // Broadcast map
    });    
    socket.on('disconnect', () => {
        console.log('User disconnected');
    });
});