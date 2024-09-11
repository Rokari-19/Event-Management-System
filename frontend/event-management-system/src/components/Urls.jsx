import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import EventsPage from "../pages/EventsPage";
import EventDetail from "../pages/EventsDetail";
import NotFoundPage from "../pages/NotFoundPage";

export default function Urls() {
    return(
        <Router basename="/">
            <Routes>

                <Route exact path="/" element={<EventsPage />}/>
                <Route path="/event/:event_id" element={<EventDetail />} />
                <Route path="*" element={<NotFoundPage />} />

            </Routes>
        </Router>
    )
}

/* 
 the way I did it in this application is by creating a separate file called URLs.JSX
 

 I run each of the routes inside this file
 todo:

 import axios and setup url routing
*/