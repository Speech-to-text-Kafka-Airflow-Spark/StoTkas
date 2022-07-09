import React , { useState } from 'react'
import { Fab } from '@mui/material';
import MicIcon from '@mui/icons-material/Mic';
import MicOffIcon from '@mui/icons-material/MicOff';
import { AudioPlayer } from 'mui-audio-player';



export default function AudioActions(audioUrl, recordHandler, stopHandler ) {
    const [currentState, setCurrentState] = useState("idle");
    //  console.log(recordHandler);
    //  console.log(stopHandler);
    const onStart = () => {
        setCurrentState("recording");
        recordHandler()
      }
      const onStop = () => {
        console.log(currentState);
        setCurrentState("stopped");
        console.log(currentState);
    
        stopHandler()
      }

      console.log(currentState);
      

    if (currentState === "idle") {  

        return (    
        <div className="root">
          <Fab>
            <MicIcon onClick={onStart}/>
          </Fab>
        </div> 
        );
      } 
      else if (currentState === "recording") {    
        return (    
        <div className="root">
          <Fab>
            <MicOffIcon onClick={onStop}/>
          </Fab>
        </div> 
        );
      } 
    return (
        <div className='audio'>
        <AudioPlayer 
          elevation={1}
          width="100%"
          variation="default"
          spacing={3}
          src={audioUrl} />
      </div>
  )
}

