import React, { useEffect, useState } from 'react';
import Header from './components/header';
import StanceComponent from './components/StanceComponent'; // Import StanceComponent
import InterpretationComponent from './components/InterpretationComponent'; // Import StanceComponent

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
    <div className="background_color">
      <Header />
      <StanceComponent width={350} height={350} left={670} top={0} /> 
      <StanceComponent width={175} height={170} left={1035} top={0} />
      <StanceComponent width={175} height={170} left={1035} top={180} />
      <div>
      <InterpretationComponent
        containerWidth={1020}
        containerHeight={330}
        contentWidth={920}
        contentHeight={50}
        contentTop={360}
      />
      {/* Use the component with different sizes as needed */}
      <InterpretationComponent
        containerWidth={1020}
        containerHeight={330}
        contentWidth={920}
        contentHeight={50}
        contentTop={720}
      />
    </div>
      <iframe
        width="650"
        height="350"
        src={`https://www.youtube.com/embed/${youtubeVideoId}?autoplay=1`}
        frameBorder="0"
        allowFullScreen
        title="Live Video"
      />
    </div>
  );
};

export default App;