import { Box, Grid } from "@mui/material"
import CssBaseline from '@mui/material/CssBaseline';
import SideBar from "@/components/SideBar"

let style = {
  display: "flex",
  minHeight: "100vh",
  flexDirection: "column",
  justifyContent: "space-between"
}

export default function MyApp ({ Component, pageProps }) {
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
            <Component {...pageProps} />
          </Box>
        </Grid>
      </Grid>
    </Box>
  )
}