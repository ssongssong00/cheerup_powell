import React, { useEffect, useState } from 'react';

const App = () => {
  const [emotions, setEmotions] = useState({});
  const [text, setText] = useState({});

  useEffect(() => {
    // Fetch emotions
    fetch('http://172.21.119.147:5001/emotion')
      .then((response) => response.json())
      .then((data) => setEmotions(data));

    // Fetch text
    fetch('http://172.21.119.147:5001/text')
      .then((response) => response.json())
      .then((data) => setText(data));
  }, []);

  return (
    <div>
      <h1>Emotions</h1>
      <pre>{JSON.stringify(emotions, null, 2)}</pre>

      <h1>Text</h1>
      <pre>{JSON.stringify(text, null, 2)}</pre>
    </div>
  );
};

export default App;