import React from "react";
import { useRouter } from 'next/router'
import { Box, TextField, InputAdornment, Button } from "@mui/material";
import PageHeader from '../components/PageHeader'
import YouTubeIcon from '@mui/icons-material/YouTube';
import BackupIcon from '@mui/icons-material/Backup';
import WaitModal from "@/components/WaitModal";

export default function YouTubeLink () {
  const router = useRouter()
  const [waiting, setWaiting] = React.useState(false)
  const [urlText, setUrlText] = React.useState("")

  async function onSubmit () {
    setWaiting (true)
    
    try {
      // Upload data to server
      const sendResponse = await fetch(`http://localhost:5000/sendyoutubeurl?url=${urlText}`, {
        method: 'POST',
      });
      
      // Tell server to generate flashcards for the uploaded document
      const { id: documentID } = await sendResponse.json()
      const generateResponse = await fetch(`http://localhost:5000/generatecards?id=${documentID}&dataformat=yt`, {
        method: 'GET',
      })

      if (generateResponse.ok) {
        // Transition to the flashcards page using the given ID
        const { id: flashcardsID } = await generateResponse.json()
        router.push(`/Flashcards/${flashcardsID}`)
      } else {
        // Handle error
        console.error('Error submitting data');
        alert('Error submitting data');
      }
    } catch (error) {
      console.error(error);
      alert(error);
    }

    setWaiting(false)
  }
  
  return (
    <Box>
      <PageHeader title="YouTube Link" />
      <Box style={{display: "flex", alignItems: "center", flexDirection: "column", gap: "1rem"}}>
        <TextField
          id="youtubelink"
          label="YouTube Link"
          variant="outlined"
          fullWidth
          autoFocus
          onChange={(event)=>setUrlText(event.target.value)}
          style={{maxWidth: "30rem"}}
          InputProps={{
            startAdornment: (
              <InputAdornment position="start">
                <YouTubeIcon />
              </InputAdornment>
            ),
          }}
        />
        <Button
          startIcon={<BackupIcon />}
          variant="contained"
          onClick={onSubmit}
        >
          Submit
        </Button>
      </Box>

      <WaitModal open={waiting} />
    </Box>
  );
}
