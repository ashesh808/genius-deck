import React from 'react';
import { Box, Paper, Grid, Button, Typography } from '@mui/material';
import Link from 'next/link';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';
import AddLinkIcon from '@mui/icons-material/AddLink';
import DataObjectIcon from '@mui/icons-material/DataObject';
import SearchIcon from '@mui/icons-material/Search';
import SchoolTwoToneIcon from '@mui/icons-material/SchoolTwoTone';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import UploadFileIcon from '@mui/icons-material/UploadFile';

const sideBarData = [
  {
    title: 'Submit File',
    icon: CloudUploadIcon,
    url: '/SubmitFile',
  },
  {
    title: 'Submit Link',
    icon: AddLinkIcon,
    url: '/SubmitLink',
  },
  {
    title: 'Card Data',
    icon: DataObjectIcon,
    url: '/JSONData',
  },
  {
    title: 'Browse',
    icon: SearchIcon,
    url: '/Browse?page=1',
  },
  {
    title: 'Profile',
    icon: AccountCircleIcon,
    url: '/Profile/test?page=1',
  },
  {
    title: 'Uploaded Files',
    icon: UploadFileIcon,
    url: '/UploadedFiles?page=1',
  },
];

const websiteName = "GeniusDeck"
const footerText = "Made for MICS 2024"

/**
 * Acts as a way for users to brose the site. Intended to always be displayed on the left
 * @returns {JSX.Element} A SideBar component.
 */
export default function SideBar() {
  return (
    <Box sx={{ display: 'flex', flexDirection: 'column', height: '100%' }}>
      <Paper elevation={10} sx={{ flex: 1, display: 'flex', flexDirection: 'column', backgroundColor: '#B0B0B0', padding: '0.5rem' }}>
        <Grid container rowSpacing={1} direction="column" justifyContent="center" alignItems="center">
          <Grid item style={{display: "flex", justifyContent: "center", flexDirection: "column"}}>
            <Link href="/">
              <SchoolTwoToneIcon style={{width: "7rem", height: "7rem"}} />
            </Link>
            <Typography align="center" variant="h4" style={{fontSize: "1.2rem"}}>
                {websiteName}
            </Typography>
          </Grid>

          {sideBarData.map((item, index) => (
            <Grid item key={index} sx={{ width: '100%' }}>
              <Link href={item.url}>
                <Button variant="contained" startIcon={<item.icon />} fullWidth>
                  {item.title}
                </Button>
              </Link>
            </Grid>
          ))}
        </Grid>
      </Paper>

      <Box style={{backgroundColor: "#808080", padding: "0.5rem"}}>
        <Typography align="center" variant="subtitle1" style={{fontSize: "0.8rem"}}>
            {footerText}
        </Typography>
      </Box>
    </Box>
  );
}