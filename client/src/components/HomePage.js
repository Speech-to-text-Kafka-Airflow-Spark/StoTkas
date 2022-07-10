
import React from "react";
import Actions from "./AudioActions";
import Recorder from "../cor/Recorder";
import Server from "../cor/Server";
import { useEffect, useState } from "react";
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles((theme) => ({
  paper: {
    marginTop: theme.spacing(8),
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    backgroundImage: 'linear-gradient(0deg,var(--white) 20%,var(--desert-storm))'
  },
	transcription: {
    fontSize: 20,
    backgroundColor: 'rgba(34, 2, 40, 7)',
    color: '#ffffff',
    padding: 20,
    paddingTop: 70,
    paddingBottom: 70,
    borderRadius: 20,
    marginBottom: 50
  },
  buttonaudio: {
    backgroundColor: 'rgba(34, 2, 40, 0.593)',
    padding: 50
  }
}));

 function HomePage() {
  const classes = useStyles();
  const [transcription, receiveTranscription, sendAudio] = Server();
  const [audio, setAudio] = useState("")

  let [audioURL, isRecording, startRecording, stopRecording] = Recorder();

  const record = () => {
    console.log("Record");
    sendAudio()
		startRecording()
  }
	const stop = () => {
    console.log("stop");
		stopRecording()
  }

	console.log(isRecording);

  useEffect(() => {
    receiveTranscription()
  }, [receiveTranscription])


	return (
   
    <div className={classes.paper}>
      <div className={classes.transcription}>
        <h1>
          የኦሊምፒክ ማጣሪያ ተሳታፊዎች የሚለዩበት ቻምፒዮና እየተካሄደ ይገኛል
        </h1>
      </div>

      <div className={classes.buttonaudio}>
				<Actions audioURL = {audioURL} recordHandler={record} stopHandler={stop}></Actions>
      </div>  
      </div>
   
  );
}
export default HomePage;
