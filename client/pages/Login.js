import React from "react";

import { Box, Button, TextField } from "@mui/material";
const Login = () => {
    return (
        <div
            style={{
                display: "flex",
                flexDirection: "column",
                justifyContent: "center",
                alignItems: "center",
                height: "70vh",
            }}
        >
            <Box
                component="form"
                sx={{
                    border: "1px solid black",
                    borderRadius: "20px",
                    padding: "20px",
                    "& .MuiTextField-root": { m: 1, width: "40ch" },
                }}
                noValidate
                autoComplete="off"
            >
                <h1 style ={{
                    textAlign: "center",
                    marginBottom: "20px",
                }}>Login</h1>
                <div>
                    <TextField
                        required
                        sx={{ margintop: "20px" }}
                        id="outlined-required"
                        label="Username"
                    />
                </div>
                <div>
                    <TextField
                        required
                        id="outlined-password-input"
                        label="Password"
                        type="password"
                        autoComplete="current-password"
                    />
                </div>
                <Button
                    variant="contained"
                    sx={{
                        display: "flex",
                        justifyContent: "center",
                        alignItems: "center",
                        width: "100%",
                        marginTop: "10px",
                        marginBottom: "20px",
                    }}
                >
                    Login
                </Button>
            </Box>
        </div>
    );
};

export default Login;
