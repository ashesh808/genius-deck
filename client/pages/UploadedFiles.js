import React, { useState, useEffect } from "react"
import { useRouter } from 'next/router';
import { Box, Typography, Button, Pagination, Grid, Container } from "@mui/material"
import PageHeader from '@/components/PageHeader'
import FileInfo from '@/components/FileInfo'

const itemsPerPage = 16

export default function UserFiles() {
  const router = useRouter();
  const [page, setPage] = useState(parseInt (router.query.page) ?? 1)
  
  // TEMP MOCK DATA
  let fileData = []
  for (let i = 0; i < 20; i++) {
    const data = {
      id: i + 1,
      title: "Test File " + (i + 1),
      uploaddate: `${i} January 2021`,
      expiredate: `${i} February 2021`,
    }
    fileData.push (data)
  }
  const numOfSets = fileData.length

  // This will be called when the final delete button is pressed
  function handleFileDeleted (fileData) {
    alert (`File "${fileData.title}" deleted`)
  }

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

  return (
    <Box>
      <PageHeader title="Uploaded Files" />

      <Container>
        <Typography align="left" variant="h5" paddingBottom="1rem">
          {numOfSets} Uploaded Files
        </Typography>
      
        <Grid container spacing={{ xs: 2, md: 3 }} columns={{ xs: 4, sm: 8, md: 16 }} justifyContent="center" alignItems="center" paddingBottom={2}>
          {fileData.slice((page-1)*itemsPerPage, page*itemsPerPage).map((fileObj, index) => (
            <Grid item key={index} xs={2} sm={3} md={4}>
              <FileInfo fileData={fileObj} fileDeleted={handleFileDeleted}/>
            </Grid>
          ))}
        </Grid>
        {
          fileData.length > 0 &&
          <Box style={{ display: "flex", justifyContent: "center", marginBottom: "0.5rem"}}>
            <Pagination count={Math.ceil (numOfSets/itemsPerPage)} page={page ?? 1} onChange={handleChangePage} />
          </Box>
        }
      </Container>
    </Box>
  )
}