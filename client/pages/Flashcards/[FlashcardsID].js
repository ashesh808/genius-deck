import React, { useState, useEffect } from "react"
import { useRouter } from 'next/router';
import { Box, Avatar, Tooltip, Pagination, Grid } from "@mui/material"
import ShuffleIcon from '@mui/icons-material/Shuffle';
import ReplayIcon from '@mui/icons-material/Replay';
import "../../components/clickable.css";
import InfoCard from "../../components/InfoCard"
import SpeakContent from "../../components/SpeakContent"
import PageHeader from '../../components/PageHeader'
import DownloadIcon from '@mui/icons-material/Download';

//put If subDir is JSON like Flashcards/JSON then get the query data and parse it 

export default function Flashcards () {
  
  const [currentPage, setCurrentPage] = useState(1);
  const [shuffledCards, setShuffledCards] = useState([]);
  const [showAnswer, setShowAnswer] = useState(false);

  const router = useRouter();
  const { FlashcardsID } = router.query;

  React.useEffect(()=>{
    async function getFlashcardData() {

      if (FlashcardsID === undefined) {
        return;
      }
      
      //flashcardID is undefined when refreshing the page
      console.log(FlashcardsID)
      if (FlashcardsID === "JSON") {
        //get from json query data
        console.log("fetching JSON from query data")
        const data = router.query.data
        setShuffledCards(JSON.parse(data))
        //console.log(JSON.parse(data))

      } else {
    
      try {
        // Get flash card data
        const flashcardResponse = await fetch(`http://localhost:5000/getflashcarddata?id=${FlashcardsID}`, {
          method: 'GET',
        })

        const flashcard_data = await flashcardResponse.json()
        const combinedArray = [].concat(...flashcard_data)
        if (Array.isArray (flashcard_data) === true) {
          setShuffledCards (combinedArray)
        }
        else {
          // Handle error
          console.error('Error getting flashcard data');
          alert('Error getting flashcard data');
        }

      } catch (error) {
        console.error(error);
        alert(error);
      }
    }
  }
    getFlashcardData()
  }, [FlashcardsID])

  if (shuffledCards.length <= 0) return null

  const shuffleCards = () => {
    // Use a copy of the original cards array to avoid mutating the original array
    const newShuffledCards = [...shuffledCards];
    for (let i = newShuffledCards.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [newShuffledCards[i], newShuffledCards[j]] = [newShuffledCards[j], newShuffledCards[i]];
    }
    setShuffledCards(newShuffledCards);
    setCurrentPage(1); // Reset to the first page after shuffling
  };
  
  const handleChangePage = (event, page) => {
    setCurrentPage(page);
  };

  const downloadJson = () => {
    const jsonContent = JSON.stringify(shuffledCards, null, 2);
    const blob = new Blob([jsonContent], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'flashcards.json';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  const currentCardIndex = (currentPage - 1) % shuffledCards.length;

  const currentCard = shuffledCards[currentCardIndex];

  return (
    <Box>
      <PageHeader title="Learn" />

      <Box style={{ display: "flex", justifyContent: "center", marginBottom: "0.5rem"}}>
        <Pagination count={shuffledCards.length} page={currentPage} onChange={handleChangePage} />
      </Box>
      
      <Box style={{ paddingRight: "5rem", paddingLeft: "5rem" }}>
        <InfoCard cardNumber={currentCardIndex + 1} questionText={currentCard.question} answerText={currentCard.answer} showAnswer={showAnswer} setShowAnswer={setShowAnswer} />
      </Box>

      <Box style={{display: "flex", justifyContent: "center", paddingRight: "5rem", paddingLeft: "5rem"}}>
        <Grid
          container
          justifyContent="center"
          alignItems="center"
          style={{
            marginTop: "1rem",
            marginBottom: "1rem",
            maxWidth: "30rem",
            width: "100%"
          }}>
          <Grid item xs={2}>
            <Tooltip title="Regenerate">
              <Avatar className="clickable">
                <ReplayIcon style={{ color: 'black' }}/>
              </Avatar>
            </Tooltip>
          </Grid>
          <Grid item xs={2}>
            <Tooltip title="Shuffle" onClick={shuffleCards}>
              <Avatar className="clickable">
                <ShuffleIcon style={{ color: 'black' }}/>
              </Avatar>
            </Tooltip>
          </Grid>
          <Grid item xs={2}>
          <Tooltip title="Download JSON" onClick={downloadJson}>
            <Avatar className="clickable">
              <DownloadIcon style={{ color: 'black' }} />
            </Avatar>
          </Tooltip>
        </Grid>
          <Grid item xs={4} />
          <Grid item xs={2} style={{display: "flex", justifyContent: "flex-end"}} >
              {showAnswer
                ? <SpeakContent textToSpeak={currentCard.answer} />
                : <SpeakContent textToSpeak={currentCard.question} />
              }
          </Grid>
        </Grid>
      </Box>
    </Box>
  )
}
