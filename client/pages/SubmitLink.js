import React from "react";
import { useRouter } from 'next/router'
import { Box, TextField, InputAdornment, Button, Typography } from "@mui/material";
import PageHeader from '../components/PageHeader'
import BackupIcon from '@mui/icons-material/Backup';
import AddLinkIcon from '@mui/icons-material/AddLink';
import WaitModal from "@/components/WaitModal";

const regexPatterns = [
  {
    pattern: /^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube(-nocookie)?\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|live\/|v\/)?)([\w\-]+)(\S+)?$/,
    type: 'youtube',
    route: 'sendyoutubeurl',
    format: 'yt',
  },
  {
    pattern: /(?<![@\w])(((http|https)(:\/\/))?([\w\-_]{2,})(([\.])([\w\-_]*)){1,})([\w.,@?^=%&amp;:\/~+#-]*[\w@?^=%&amp;\/~+#-])/,
    type: 'wikipedia',
    route: 'sendwikiurl',
    format: 'wiki',
  },
]

export default function SubmitLink () {
  const router = useRouter()
  const [waiting, setWaiting] = React.useState(false)
  const [urlText, setUrlText] = React.useState("")

  async function onSubmit () {
    setWaiting (true)
    
    try {
      // Check if the URL is valid
      let patternObj = null

      for (let i = 0; i < regexPatterns.length; i++) {
        const item = regexPatterns[i]

        if (item.pattern.test(urlText)) {
          patternObj = item
          break
        }
      }

      if (!patternObj) {
        alert('Invalid URL')
        setWaiting(false)
        return
      }

      // Upload data to server
      const sendResponse = await fetch(`http://localhost:5000/${patternObj.route}?url=${urlText}`, {
        method: 'POST',
      });
      
      // Tell server to generate flashcards for the uploaded document
      const { id: documentID } = await sendResponse.json()
      const generateResponse = await fetch(`http://localhost:5000/generatecards?id=${documentID}&dataformat=${patternObj.format}`, {
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
      <PageHeader title="Submit Link" />
      <Box style={{display: "flex", alignItems: 'center', justifyContent: "center", flexDirection: 'column'}}>
        <TextField
          id="submitlink"
          label="Submit Link"
          variant="outlined"
          fullWidth
          autoFocus
          onChange={(event)=>setUrlText(event.target.value)}
          onKeyPress={(event) => {if (event.key=='Enter') onSubmit()}}
          style={{maxWidth: "30rem"}}
          InputProps={{
            startAdornment: (
              <InputAdornment position="start">
                <AddLinkIcon />
              </InputAdornment>
            ),
          }}
        />
        <Button
          startIcon={<BackupIcon />}
          variant="contained"
          onClick={onSubmit}
          style={{
            marginTop: '1rem',
          }}
        >
          Submit
        </Button>
        <Typography 
          variant="h4"
          style={{
            marginTop: '1rem',
            fontSize: '1.2rem',
          }}>
          Supported link types:
        </Typography>
        <Typography
          variant="subtitle1"
          style={{
            fontSize: '0.8rem',
          }}
        >
          YouTube, Wikipedia
        </Typography>
      </Box>

      <WaitModal open={waiting} />
    </Box>
  );
}
