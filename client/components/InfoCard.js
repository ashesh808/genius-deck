"use client";

import React from "react";
import { Typography, Paper, Box } from "@mui/material";
import "./clickable.css";
import { useEffect } from "react";
import InfoIcon from "@mui/icons-material/Info";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import IconButton from "@mui/material/IconButton";

/**
 * Shows quiz questions to the user in flashcard format. Users can click to reveal the answer
 * @param {Object} props
 * @param {string} props.cardNumber The index of this card
 * @param {string} props.questionText The question
 * @param {string} props.answerText The answer
 * @param {boolean} props.showAnswer Flips the card if true
 * @param {Function} props.setShowAnswer Used to set showAnswer when the user clicks on a card
 * @returns {JSX.Element} An InfoCard component.
 */
export default function InfoCard({
    cardNumber,
    questionText,
    answerText,
    showAnswer,
    setShowAnswer,
    showExplanation,
    setShowExplanation,
    explanation = NULL,
}) {
    const [rotateAnimation, setRotateAnimation] = React.useState(false); //true is 180deg, false is 0deg

    useEffect(() => {
        setShowAnswer(false);
        setRotateAnimation(rotateAnimation); //keep current state so it doesnt flip
    }, [cardNumber]);

    return (
        <Box sx={{ display: "flex", justifyContent: "center" }}>
            <Paper
                elevation={5}
                className="clickable"
                style={{
                    padding: "1rem",
                    transform: rotateAnimation
                        ? "rotateY(180deg)"
                        : "rotateY(0deg)",
                    minHeight: "17rem",
                    maxWidth: "30rem",
                    width: "100%",
                }}
                onClick={() => {
                    setShowAnswer(!showAnswer);
                    setRotateAnimation(!rotateAnimation); //flip card
                    if (showExplanation) {
                        setShowExplanation(false);
                    }
                }}
            >
                <Box
                    style={{
                        transform: rotateAnimation
                            ? "rotateY(180deg)"
                            : "rotateY(0deg)",
                    }}
                >
                    {showAnswer && explanation && (
                        <IconButton
                            onClick={(e) => {
                                e.stopPropagation(); //prevent card from flipping when clicking the info button
                                setShowExplanation(!showExplanation);
                                console.log(showExplanation);
                            }}
                        >
                            {showExplanation ? ( //if showExplaination is true, show the back arrow
                                <ArrowBackIcon />
                            ) : (
                                <InfoIcon />
                            )}
                        </IconButton>
                    )}
                    <Typography align="center" variant="h4">
                        {showAnswer
                            ? showExplanation
                                ? "Explaination"
                                : "Answer"
                            : "Question"}{" "}
                        #{cardNumber}
                    </Typography>
                    <Typography align="center" variant="body1">
                        {showAnswer
                            ? showExplanation
                                ? explanation
                                : answerText
                            : questionText}
                    </Typography>
                </Box>
            </Paper>
        </Box>
    );
}
