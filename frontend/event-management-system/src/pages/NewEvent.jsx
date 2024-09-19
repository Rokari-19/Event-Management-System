import React from "react";
import axios from "axios";

axios.defaults.baseURL = "127.0.0.1:8000";



export default function NewEvent() {
    return(
        <h1 className="font semibold">
            new event
        </h1>
    )
};

