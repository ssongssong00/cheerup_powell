import React, { useEffect, useState } from 'react';
import Header from './components/header';
import './App.css'; // Import your CSS file

const App = () => {
  const [emotions, setEmotions] = useState({});
  const [text, setText] = useState({});
  const [youtubeVideoId, setYoutubeVideoId] = useState('NJUjU9ALj4A'); // Replace with your actual YouTube video ID

  useEffect(() => {
    // Fetch emotions
    fetch('http://192.168.0.96:5001/emotion')
      .then((response) => response.json())
      .then((data) => setEmotions(data));

    // Fetch text
    fetch('http://192.168.0.96:5001/text')
      .then((response) => response.json())
      .then((data) => setText(data));
  }, []);

  return (
    
    <div>
      <Header/>
    <div  className="container">

    <iframe
      width="700"
      height="400"
      src={`https://www.youtube.com/embed/${youtubeVideoId}?autoplay=1`}
      frameBorder="0"
      allowFullScreen
      title="Live Video"
    />
    </div>
      <h1>Emotions</h1>
      <pre>{JSON.stringify(emotions, null, 2)}</pre>

      <h1>Text</h1>
      <pre>{JSON.stringify(text, null, 2)}</pre>

      {/* Add two more round-square divs as needed */}
    </div>
  );
};

export default App;