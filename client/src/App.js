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
      <StanceComponent width={350} height={350} left={670} top={0} text="Current Stance" text1="Hawkish" text2 = "본 스탠스 수치는 지난 30초 동안의 연준의장 발화 내용을 분석한 값입니다." text3 = "0점에 가까울 수록 비둘기파, 100점에 가까울수록 매파를 나타냅니다."/> 
      <StanceComponent width={175} height={170} left={1035} top={0} text="Current Face Emotion" text1 = "Negative"/>
      <StanceComponent width={175} height={170} left={1035} top={180} text="Current Voice Tone Emotion" text1 = "Neutral"/>
      <div>
      <InterpretationComponent
        containerWidth={1020}
        containerHeight={330}
        contentWidth={920}
        contentHeight={50}
        contentTop={360}
        text = "실시간 해석"
        text1 = "30초 단위로 기자회견 스크립트와 그에 대한 해석 및 해설을 제공합니다."
        text2 = "In light of the uncertainties and risks, and how far we have come, the Committee is proceeding carefully"
        text3 = "불확실성과 위험성, 그리고 우리가 얼마나 멀리 왔는지에 비추어 볼 때, 위원회는 신중하게 진행하고 있습니다."
        text4 = "신중하게 진행한다는 말은 정책 결정에 있어 신중한 접근법을 반영합니다. 이는 매파적 편향을 유지하는 것과 추가적인 금리 인상을 배제할 수 있는 잠재적인 경기 둔화를 인정하는 것 사이의 균형을 암시합니다. 현재의 경제 불확실성과 위험을 고려한 신중한 의사결정에 중점을 두고 있습니다. "
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