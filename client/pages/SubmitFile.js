'use client'

import React from "react";
import { Box, Typography } from "@mui/material";
import { useRouter } from 'next/router'
import UploadBox from '../components/UploadBox'
import PageHeader from '../components/PageHeader'
import WaitModal from "@/components/WaitModal";

const filetypes = {
  'application/pdf': ['.pdf'],
  // 'application/vnd.ms-powerpoint': ['.ppt'],
  'application/vnd.openxmlformats-officedocument.presentationml.presentation': ['.pptx'],
  'text/plain': ['.txt'],
}

export default function SubmitFile () {
  const router = useRouter()
  const [waiting, setWaiting] = React.useState(false)

  async function onSuccess (uploadedFile) {
    setWaiting (true)
    
    try {
      // Generate form data
      const formData = new FormData();
      formData.append('file', uploadedFile);
      const fileType = uploadedFile.name.split(".").slice(1).pop()

      // Upload data to server
      const uploadResponse = await fetch('http://localhost:5000/upload', {
        method: 'POST',
        body: formData,
      });
            
      // Tell server to generate flashcards for the uploaded document
      const {id: documentID} = await uploadResponse.json()
      const generateResponse = await fetch(`http://localhost:5000/generatecards?id=${documentID}&dataformat=${fileType}`, {
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
			<PageHeader title='Submit File' />
			<Box style={{ display: 'flex', justifyContent: 'center' }}>
				<UploadBox
					onSuccess={onSuccess}
					onError={() => alert('ERROR')}
					acceptedTypes={filetypes}
					title='Upload a file'
					subtitle='Drag a file file here or click to browse'
				/>
			</Box>
			<Typography
				variant='h4'
				style={{
					marginTop: '1rem',
					fontSize: '1.2rem',
					display: 'flex',
					textAlign: 'center',
                    flexDirection: 'column',
                    marginTop: '2%',
				}}>
				Supported file types:
			</Typography>
			<Typography
				variant='subtitle1'
				style={{
					fontSize: '0.8rem',
					display: 'flex',
					textAlign: 'center',
					flexDirection: 'column',
				}}>
				PDF, PPTX, TXT
			</Typography>


			<WaitModal open={waiting} />
		</Box>
  );
}
