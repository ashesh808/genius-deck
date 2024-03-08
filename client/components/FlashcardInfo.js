import { Box, Paper, Typography, CircularProgress } from "@mui/material"

import Link from 'next/link';

import "@/components/scaleHover.css";

/**
 * Shows a small amount of info for a set of flashcards
 * @param {Object} props
 * @param {string} props.flashcardData Contains all the data describing the set of flashcards
 * @param {string} props.link A URL that the user will be routed to when they click on the component
 * @returns {JSX.Element} A FlashcardInfo component.
 */
export default function FlashcardInfo({ flashcardData, link }) {
  // Show a loading spinner if the flashcardData is not yet available
  if (!flashcardData) {
    return (
      <Paper
        elevation={3}
        style={{
          display: "flex",
          justifyContent: 'center',
          flexDirection: "column",
          alignItems: "center",
        }}
      >
        <Typography variant="h6">Loading...</Typography>
        <Box style={{display: "flex", justifyContent: "center"}}>
          <CircularProgress />
        </Box>
      </Paper>
    )
  }

  return (
    <Link href={link} style={{textDecoration: 'none'}}>
      <Paper
        elevation={3}
        style={{
          display: "flex",
          justifyContent: 'center',
          flexDirection: "column",
          alignItems: "center",
        }}
        className="scaleHover"
      >
        <Typography variant="h6">{flashcardData.title}</Typography>
        <Typography variant="subtitle2">{flashcardData.uploaddate}</Typography>
        <Typography variant="subtitle2">{flashcardData.count} Cards</Typography>
      </Paper>
    </Link>
  )
}