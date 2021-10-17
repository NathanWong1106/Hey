import './App.css';
import React, {useState, useEffect} from "react";
import socketIOClient from "socket.io-client"
const ENDPOINT = "http://localhost:3000"


function App() {
  const [response, setResponse] = useState("");
  const [cameraStates, setCameraStates] = useState(new Map());

  useEffect(() =>{ 
    const socket = socketIOClient(ENDPOINT);
    socket.on("connect", () => {
      console.log("connected")
    })
    socket.on('ping', data => {
      setCameraStates(new Map(JSON.parse(data.state)))
      setResponse(data);
    });

  }, []);
  return (

    <div className="App">
      <h1> Hello</h1>
      {
        [...cameraStates.keys()].map(key => {
          return(
            <div>
              AHHHHHHHHH
            </div>
          )
        })
      }
      <script src="/socket.io-client/dist/socket.io.js"></script>
    </div>

  );
}

export default App;
