import React from "react";
import { useRouter } from 'next/router'
import { Box } from "@mui/material";
import UploadBox from '../components/UploadBox'
import WaitModal from "@/components/WaitModal";
import PageHeader from '../components/PageHeader'

const filetypes = {
  'application/json': ['.json'],
}

export default function JSONData () {
  const router = useRouter()
  const [waiting, setWaiting] = React.useState(false)

  function onSuccess(acceptedFiles) {
    setWaiting(true);
  
    try {
      const file = acceptedFiles;
  
      if (!file) {
        throw new Error("No file selected");
      }
  
      if (!file.type.includes("json")) {
        throw new Error("Invalid file type. Please upload a JSON file.");
      }
  
      const reader = new FileReader();
  
      reader.onload = () => {
        try {
          const jsonData = JSON.parse(reader.result);
  
          // Now you can use jsonData in your application
          console.log(jsonData);
  
          router.push({
            pathname: "/Flashcards/JSON",
            query: { data: JSON.stringify(jsonData) },
          });
        } catch (parseError) {
          throw new Error("Error parsing JSON: " + parseError.message);
        }
      };
  
      reader.onerror = (error) => {
        throw new Error("Error reading file: " + error.message);
      };
  
      reader.readAsText(file);
    } catch (error) {
      console.error(error.message);
      setWaiting(false);
      alert(error.message);
    }
  }
  
  
  
  return (
    <Box>
      <PageHeader title="Upload Flashcard JSON Data" />
      <Box style={{display: "flex", justifyContent: "center"}}>
        <UploadBox
          title="Upload Flashcard Data"
          subtitle="Drag a JSON file here or click to browse"
          onSuccess={onSuccess}
          onError={()=>alert ("ERROR")}
          acceptedTypes={filetypes}
        />
      </Box>

      <WaitModal open={waiting} />
    </Box>
  );
}
