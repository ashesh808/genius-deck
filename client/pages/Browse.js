import React, { useState, useEffect } from "react"
import { useRouter } from 'next/router';
import { Box, Typography, TextField, Button, Pagination, Grid, Container, Tooltip, MenuItem } from "@mui/material"
import SearchIcon from '@mui/icons-material/Search'
import PageHeader from '@/components/PageHeader'
import WaitModal from "@/components/WaitModal"
import FlashcardInfo from "@/components/FlashcardInfo"

const itemsPerPage = 16
const sortOptions = [
  "Upload Date",
  "Author",
]

export default function BrowseComponent({  }) {
  const router = useRouter()
  const [waiting, setWaiting] = React.useState(false)
  const [page, setPage] = useState(parseInt (router.query.page) ?? 1)
  const [searchString, setSearchString] = React.useState(router.query.page ?? "")
  const [tags, setTags] = React.useState(router.query.tags ?? "")
  const [sortBy, setSortBy] = React.useState(sortOptions[0])

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

  function onSubmit (itemID) {
    setWaiting (true)

    // This is where we will make the API call to search for the flashcards
  }

  function handleChangePage (event, page) {
    router.push({ // Update query parameter in URL
      pathname: router.pathname,
      query: { ...router.query, page }, // Update page query parameter
    })
    setPage (page)
    window.scrollTo(0, 0)
  }
  
  return (
    <Box>
      <PageHeader title="Browse for Flashcards"/>

      <Container>
        <Box
          style={{
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            justifyContent: "center",
          }}
        >
          <TextField
            fullWidth
            label="Search"
            id="searchTerms"
            margin="normal"
            autoFocus
            onChange={(event)=>setSearchString(event.target.value)}
            sx={{maxWidth: "35rem"}}
          />
          <Tooltip title="Separate each tag with a comma" placement="top-start" size="small">
            <TextField
              fullWidth
              id="searchTags"
              label="Tags"
              multiline
              maxRows={4}
              margin="normal"
              onChange={(event)=>setTags(event.target.value)}
              sx={{maxWidth: "35rem"}}
            />
          </Tooltip>
        </Box>
        <Box style={{display: "flex", alignItems: "center", justifyContent: "center", gap: "1rem"}}>
          <TextField
            id="searchSort"
            select
            label="Sort by"
            margin="normal"
            value={sortBy}
            onChange={(event)=>setSortBy(event.target.value)}
            sx={{
              maxWidth: "35rem",
            }}
          >
            {sortOptions.map((option) => (
              <MenuItem key={option} value={option}>
                {option}
              </MenuItem>
            ))}
          </TextField>
          <Button
            variant="contained"
            onClick={onSubmit}
          >
            <SearchIcon />
            Search
          </Button>
        </Box>

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

      <WaitModal open={waiting} />
    </Box>
  );
}
