'use client'

import React from "react";
import { Box, Paper, Typography, Input, IconButton } from "@mui/material";
import { useRouter } from 'next/router'
import UploadBox from '../components/UploadBox'
import PageHeader from '../components/PageHeader'
import WaitModal from "@/components/WaitModal";

const filetypes = {
  'application/pdf': ['.pdf'],
}

export default function UploadPDF () {
  const router = useRouter()
  const [waiting, setWaiting] = React.useState(false)

  async function onSuccess (uploadedFile) {
    setWaiting (true)
    
    try {
      // Generate form data
      const formData = new FormData();
      formData.append('file', uploadedFile);

      // Upload data to server
      const uploadResponse = await fetch('http://localhost:5000/uploadpdf', {
        method: 'POST',
        body: formData,
      });
            
      // Tell server to generate flashcards for the uploaded document
      const {id: documentID} = await uploadResponse.json()
      const generateResponse = await fetch(`http://localhost:5000/generatecards?id=${documentID}&dataformat=pdf`, {
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
      <PageHeader title="Upload PDF" />
      <Box style={{display: "flex", justifyContent: "center"}}>
        <UploadBox
          onSuccess={onSuccess}
          onError={()=>alert ("ERROR")}
          acceptedTypes={filetypes}
          title="Upload a PDF"
          subtitle="Drag a PDF file here or click to browse"
        />
      </Box>

      <WaitModal open={waiting} />
    </Box>
  );
}
