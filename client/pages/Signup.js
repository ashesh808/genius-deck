import React from "react";
import { useState } from "react";
import { Box, Button, TextField } from "@mui/material";
import { useRouter } from "next/router";

const Signup = () => {
    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const [isLoading, setIsLoading] = useState(false);

    const router = useRouter();

    const handleLogin = async (event) => {
        event.preventDefault();
        try {
            //check for empty fields
            if (!username || !password || !email) {
                return window.alert("Please fill out all fields");
            }
            setIsLoading(true);
            const res = await fetch("http://localhost:5000/register", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    username: "username",
                    email: "email",
                    password: "password",
                }),
            });

            if (!res.ok) {
                throw new Error("Register failed");
                return window.alert("Register failed");
            }

            const data = await res.json();

            if (data.error) {
                return window.alert(data.error);
            }

            setError("");

            console.log(`Login successful!`);
            // Redirect after successful login
            router.push("http://localhost:3000");
        } catch (error) {
            console.error(error.message);
            window.alert(error.message);
        } finally {
            setIsLoading(false);
        }
    };

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
                onSubmit={handleLogin}
                sx={{
                    border: "1px solid black",
                    borderRadius: "20px",
                    padding: "20px",
                    "& .MuiTextField-root": { m: 1, width: "40ch" },
                }}
                noValidate
                autoComplete="off"
            >
                <h1
                    style={{
                        textAlign: "center",
                        marginBottom: "20px",
                    }}
                >
                    Sign Up
                </h1>
                <div>
                    <TextField
                        required
                        sx={{ margintop: "20px" }}
                        id="outlined-required"
                        label="Username"
                        onChange={(e) => setUsername(e.target.value)}
                    />
                </div>
                <div>
                    <TextField
                        required
                        id="outlined-required"
                        label="Email"
                        onChange={(e) => setEmail(e.target.value)}
                    />
                </div>
                <div>
                    <TextField
                        required
                        id="outlined-password-input"
                        label="Password"
                        type="password"
                        autoComplete="current-password"
                        onChange={(e) => setPassword(e.target.value)}
                    />
                </div>
                <Button
                    type="submit"
                    variant="contained"
                    disabled={isLoading}
                    sx={{
                        display: "flex",
                        justifyContent: "center",
                        alignItems: "center",
                        width: "100%",
                        marginTop: "10px",
                        marginBottom: "20px",
                    }}
                >
                    Register
                </Button>
            </Box>
        </div>
    );
};

export default Signup;
