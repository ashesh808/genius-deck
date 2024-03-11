import React, { useState, useEffect } from "react"
import { Box, Paper, Typography, CircularProgress, Modal, Button, IconButton } from "@mui/material"

import DeleteIcon from '@mui/icons-material/Delete';
import DeleteForeverIcon from '@mui/icons-material/DeleteForever';

import "@/components/scaleHover.css";

/**
 * Shows a small amount of info for an uploaded file
 * @param {Object} props
 * @param {Object} props.fileData Contains all the data describing the uploaded file
 * @param {Function} props.fileDeleted A function that will be called when the file is deleted. props.fileData will be passed as the first param
 * @returns {JSX.Element} A FileInfo component.
 */
export default function FileInfo({ fileData, fileDeleted }) {
  const [modalOpen, setModalOpen] = useState(false)
  const [hovered, setHovered] = useState(false)

  // Executes when the user clicks on the info card
  function handleClick () {
    setModalOpen(true)
  }

  // Show a loading spinner if the fileData is not yet available
  if (!fileData) {
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
    <Box>
      <Paper
        elevation={3}
        sx={{
          display: "flex",
          justifyContent: 'center',
          flexDirection: "column",
          alignItems: "center",
          transition: 'background-color 0.3s',
          '&:hover': {
            backgroundColor: '#ff00008f',
            "& $deleteIcon": {
              visibility: "visible",
            },
          }
        }}
        className="scaleHover"
        onMouseEnter={() => setHovered(true)}
        onMouseLeave={() => setHovered(false)}
        onClick={handleClick}
      >
        <Typography variant="h6">{fileData.title}</Typography>
        <Typography variant="subtitle2">Uploaded: {fileData.uploaddate}</Typography>
        <Typography variant="subtitle2">Expires: {fileData.expiredate}</Typography>
        {
          hovered && (
            <DeleteIcon 
              sx={{
                position: "absolute",
                top: "50%",
                left: "50%",
                transform: 'translate(-50%, -50%)',
                height: "75%",
                width: "auto"
              }}
            />
          )
        }
      </Paper>

      {
        modalOpen && (
          <Modal
            open={open}
            sx={{display: "flex", alignItems: "center", justifyContent: "center"}}
            onClose={() => setModalOpen(false)}
          >
            <Paper sx={{padding: "2rem"}}>
              <Typography id="modal-modal-title" variant="h6" marginTop="1rem">
                Are you sure you want to delete this file?
              </Typography>
              <Typography variant="subtitle1">
                This cannot be undone!
              </Typography>
              <Box style={{display: "flex", justifyContent: "center", gap: "1rem", marginTop: "1rem"}}>
                <Button
                  variant="contained"
                  color="error"
                  startIcon={<DeleteForeverIcon />}
                  onClick={() => {
                    fileDeleted && fileDeleted(fileData)
                    setModalOpen(false)
                  }}
                >
                  Delete
                </Button>
                <Button
                  onClick={() => setModalOpen(false)}
                >
                  Cancel
                </Button>
              </Box>
            </Paper>
          </Modal>
        )
      }
    </Box>
  )
}