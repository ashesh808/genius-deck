'use client'

import React from "react";
import { Typography, Box, Modal, Button, Paper, CircularProgress } from '@mui/material';

/**
 * Shows a pop-up with a load bar. Intended to be shown while waiting for a server response
 * @param {Object} props
 * @param {string} props.open Determines whether the modal should be open 
 * @returns {JSX.Element} A WaitModal component.
 */
export default function WaitModal ({ open }) {
  return (
    <div>
      <Modal
        open={open}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
        sx={{display: "flex", alignItems: "center", justifyContent: "center"}}
      >
        <Paper sx={{padding: "2rem"}}>
          <Box style={{display: "flex", justifyContent: "center"}}>
            <CircularProgress />
          </Box>
          <Typography id="modal-modal-title" variant="h6" marginTop="1rem">
            Please wait...
          </Typography>
        </Paper>
      </Modal>
    </div>
  );
}