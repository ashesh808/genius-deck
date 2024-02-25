'use client'

import React, { useCallback } from "react";
import { Box, Paper, Typography, Input, IconButton } from "@mui/material";
import CloudUploadIcon from '@mui/icons-material/CloudUpload';
import { useDropzone } from 'react-dropzone';

/**
 * Allows users to upload files by dragging them into the box or using their file browser
 * @param {Object} props
 * @param {string} props.title The big text at the top of the box
 * @param {string} props.subtitle The small text at the bottom of the box
 * @param {string} props.onSuccess The function called when the file is selected. It will pass the file object as the first param
 * @param {string} props.onError The function called when the file is selected. It will pass the error string as the first param
 * @param {Array} props.acceptedTypes An array of MIME types that determine which files are able to be selected
 * @returns {JSX.Element} An UploadBox component.
 */
export default function UploadBox ({ title, subtitle, onSuccess, onError, acceptedTypes }) {
  const {
    acceptedFiles: files,
    fileRejections,
    getRootProps,
    getInputProps,
    isDragActive
  } = useDropzone({
    accept: acceptedTypes,
    maxFiles: 1,
    multiple: false,
    onDrop: (acceptedFiles, fileRejections) => {
      if (fileRejections.length > 0) {
        onError(`Invalid file type. Accepted types: ${acceptedFiles.join(', ')}`);
      } else if (acceptedFiles.length === 1) {
        onSuccess(acceptedFiles[0]);
      }
    },
  })

  return (
    <Box sx={{
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      minHeight: '200px',
      border: '2px dashed #dcdcdc',
      borderRadius: '4px',
      cursor: 'pointer',
      padding: '20px',
      outline: 'none',
      transition: 'border 0.24s ease-in-out',
      backgroundColor: isDragActive ? '#f0f0f0' : 'white',
      maxWidth: "30rem",
      width: "100%",
      textAlign: 'center',
    }}>
      <Typography variant="h5" gutterBottom>
        {title}
      </Typography>
      <Box {...getRootProps()} style={{ cursor: 'pointer' }}>
        <Input {...getInputProps()} />
        <IconButton color="primary" component="span" disabled={isDragActive}>
          <CloudUploadIcon fontSize="large" />
        </IconButton>
        <Typography>
          {subtitle}
        </Typography>
      </Box>
    </Box>
  );
}
