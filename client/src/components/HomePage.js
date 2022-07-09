
import React from "react";
import Actions from "./AudioActions";
import useRecorder from "../cor/userRecorder";

 function HomePage() {
   
    let [audioURL, isRecording, startRecording, stopRecording] = useRecorder();
    
    const record = () => {
        console.log("Record");
        // sendAudio()
            startRecording()
           
      }
    const stop = () => {
        console.log("stop");
            stopRecording()
           
      }

    console.log(isRecording);
  return (
    
    <div className='homePage'>      

      <h1> እንካን በድህና መጡ!
      </h1>
      <Actions audioURL = {audioURL} recordHandler={record} stopHandler={stop} ></Actions>
          

  </div>
  )
}
export default HomePage;
