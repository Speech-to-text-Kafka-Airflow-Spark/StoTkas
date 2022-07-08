import { Container } from '@mui/material';
import React, {useEffect, useState} from "react";
import { makeStyles } from '@mui/material/styles';



export default function HomePage() {
    const classes = useStyles();
    const [transcription, receiveTranscription, sendAudio] = useServer();
  return (
    <Container component="main" maxWidth="xs">      
    <div className="paper">
      <h1>
       እንካን በድህና መጡ!
      </h1>
                  <Typography className="transcription" color="textSecondary" align="center" gutterBottom>
            {transcription}
          </Typography>
      
    </div>
  </Container>
  )
}
