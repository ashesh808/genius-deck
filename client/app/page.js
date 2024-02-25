import { Box, Grid, Typography } from "@mui/material"
import CssBaseline from '@mui/material/CssBaseline';
import PageHeader from '../components/PageHeader'
import SideBar from "@/components/SideBar";

let style = {
  display: "flex",
  minHeight: "100vh",
  flexDirection: "column",
  justifyContent: "space-between"
}

export default function Home() {
  return (
    <Box style={style}>
      <CssBaseline />
      <Grid container spacing={0} style={{height: "100vh"}}>
        <Grid item xs={3} md={2}>
          <SideBar />
        </Grid>
        <Grid item xs={9} md={10}>
          <Box sx={{padding: "1rem"}}>
            {/* Content goes here */}
            <PageHeader title="Welcome!" />
            <Typography align="center" variant="body1">
              Please selection an option on the left to begin!
            </Typography>
          </Box>
        </Grid>
      </Grid>
    </Box>
  )
}
