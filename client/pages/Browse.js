import React from "react";
import { useRouter } from 'next/router'
import { Box, Paper, Button, List, ListItem, ListItemText } from "@mui/material";
import PageHeader from '../components/PageHeader';
import WaitModal from "@/components/WaitModal";

let BrowseData = [
  {
    ID: 2532153,
    numOfCards: 42
  },
  {
    ID: 857373,
    numOfCards: 3
  },
  {
    ID: 88382,
    numOfCards: 15
  },
  {
    ID: 55521,
    numOfCards: 13
  },
];

export default function BrowseComponent({  }) {
  const router = useRouter()
  const [waiting, setWaiting] = React.useState(false)

  function onSubmit (itemID) {
    setWaiting (true)

    // This is where we make our first API call
    fetch('https://jsonplaceholder.typicode.com/todos/1')
    .then(response => response.json())
    .then(data => {
      // Close the WaitModal after receiving the response
      setWaiting(false);

      // Additional logic with the response data
      alert(JSON.stringify (data));

      router.push('/Flashcards/5555')
    })
    .catch(error => {
      // Handle errors, close the WaitModal, and show an error message
      setWaiting(false);
      console.error("Error fetching data:", error);
      alert("Error fetching data. Please try again.\n" + error);
    })
  }
  
  return (
    <Box display="flex" flexDirection="column" alignItems="center">
      <PageHeader title="Browse for Flashcards"/>
      <List>
        {BrowseData.map((item) => (
          <Paper elevation={3} key={item.ID} style={{ margin: '10px', padding: '10px', maxWidth: "35rem", minWidth: "25rem" }}>
            <ListItem>
              <ListItemText primary={`ID: ${item.ID} - Cards: ${item.numOfCards}`} />
              <Button variant="contained" color="primary" onClick={()=>onSubmit(item.ID)}>
                Open
              </Button>
            </ListItem>
          </Paper>
        ))}
      </List>

      <WaitModal open={waiting} />
    </Box>
  );
}
