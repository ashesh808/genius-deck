import { Box, Divider, Typography } from "@mui/material";

/**
 * Shows the title of the current page. Indended to be shown at the top of every page
 * @param {Object} props
 * @param {string} props.title The text that will be shown
 * @returns {JSX.Element} A PageHeader component.
 */
export default function PageHeader ({ title }) {
  return (
    <Box style={{marginBottom: "2rem"}}>
      <Typography variant="h4" align="center" gutterBottom>
        {title}
      </Typography>
      <Divider />
    </Box>
  )
}