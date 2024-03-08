import React, { useState, useEffect } from "react"
import { useRouter } from 'next/router';
import { Box, Paper, Typography, Pagination, Grid, Container } from "@mui/material"
import PageHeader from '@/components/PageHeader'
import FlashcardInfo from '@/components/FlashcardInfo'

const itemsPerPage = 16

// TODO: automatically go to page 1 if the page number is invalid or not provided
// (right now it will show as NaN if one isn't provided)
export default function Profile () {
  const router = useRouter();
  const UserID = router.query.UserID;
  const [page, setPage] = useState(parseInt (router.query.page) ?? 1)

  // TEMP MOCK DATA
  const userdata = {
    username: "Test User",
    joindate: "1 January 2021",
  }
  let flashcardData = []
  for (let i = 0; i < 20; i++) {
    const flashcard = {
      id: i + 1,
      title: "Test Set " + (i + 1),
      uploaddate: "1 January 2021",
      count: Math.floor (Math.random () * (100 - 1) + 1),
    }
    flashcardData.push (flashcard)
  }
  const numOfSets = flashcardData.length

  function handleChangePage (event, page) {
    // I kinda wish this part used a useEffect instead, but I couldn't get the routing to work
    // This code also doesn't check if the new page number is valid. It just relies on the pagination component
    router.push({ // Update query parameter in URL
      pathname: router.pathname,
      query: { ...router.query, page }, // Update page query parameter
    })
    window.scrollTo(0, 0)
    
    setPage (page)
  }

  // This will be used to fetch the profile data later on
  React.useEffect(()=>{
    async function getFlashcardData() {
      // Get user profile information

      // Username

      // Array of flashcards IDs and titles

      // Extract size of flashcard array

      // Check if the current page number is valid for the current size of the flashcards array
    }
  }, [])

  React.useEffect(()=>{
    if(router.isReady) {
      setPage (parseInt (router.query.page) ?? 1)
    }
  }, [router.isReady])

  return (
    <Box>
      <PageHeader title="Profile" />
      <Box
        style={{
          display: "flex",
          alignItems: "center",
          flexDirection: "column",
        }}
      >
        <Paper 
          elevation={5}
          style={{
            minHeight: '6rem',
            maxWidth: "30rem",
            width: "100%",
            display: "flex",
            justifyContent: 'center',
            flexDirection: "column",
            alignItems: "center",
            padding: "1rem"
          }}
        >
          <Typography variant="h5">{userdata.username}</Typography>
          <Typography variant="subtitle">Joined: {userdata.joindate}</Typography>
        </Paper>
      </Box>
      <Container style={{marginTop: "1rem"}}>
        <Typography align="left" variant="h5" paddingY={1}>
          {numOfSets} Flashcard Sets
        </Typography>
        <Grid container spacing={{ xs: 2, md: 3 }} columns={{ xs: 4, sm: 8, md: 16 }} justifyContent="center" alignItems="center" paddingBottom={2}>
          {flashcardData.slice((page-1)*itemsPerPage, page*itemsPerPage).map((flashcardObj, index) => (
            <Grid item key={index} xs={2} sm={3} md={4}>
              <FlashcardInfo flashcardData={flashcardObj} link={`/Flashcards/${flashcardObj.id}`} />
            </Grid>
          ))}
        </Grid>
        {
          flashcardData.length > 0 &&
          <Box style={{ display: "flex", justifyContent: "center", marginBottom: "0.5rem"}}>
            <Pagination count={Math.ceil (numOfSets/itemsPerPage)} page={page ?? 1} onChange={handleChangePage} />
          </Box>
        }
      </Container>
    </Box>
  )
}