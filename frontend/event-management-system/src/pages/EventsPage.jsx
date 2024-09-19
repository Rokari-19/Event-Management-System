import React, { useState, useEffect } from "react";
import axios from "axios";


axios.defaults.baseURL = "http://127.0.0.1:8000";

export default function EventsPage() {
  const [post, setPost] = useState([]);

  useEffect(() => {
    axios.get("/api/v1/events/").then((data) => {
      // console.log(data);
      setPost(data?.data);
    });
  }, []);

  return (
    <div>
      {post.map((item, i) => {
        return (
          <a href="#">
            <div key={i} className="reactCard">
              <img className="cardImage" src={item?.get_event_thumb} />
              <h4 className="cardTitle">{item?.organizer}</h4>
              <h1 className="cardTitle">{item?.event_name}</h1>
              <p className="cardText">{item?.event_desc}</p>
              <span>
                <p className="cardText">{item?.event_start}</p>
                <p className="cardText">{item?.event_start}</p>
              </span>
            </div>
          </a>
        );
      })}
    </div>
  );
}



// create an events detail view in backend
