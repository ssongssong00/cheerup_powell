import React from 'react';

const InterpretationComponent = ({ containerWidth, containerHeight, contentWidth, contentHeight, contentTop, text,text1,text2,text3,text4 }) => {

    return (
    <div style={{ width: '100%', height: '100%', position: 'relative' }}>
      <div style={{ width: containerWidth || 1020, height: containerHeight || 310, left: 0, top: contentTop || 360, position: 'absolute', background: 'white', borderRadius: 25 }}>
      <p style={{ margin: 0, fontSize: '15px', color: '#333', textAlign: 'left', paddingLeft: '30px', paddingTop: '100px', zIndex: 1 }}>
        원문 : {text2} </p>
      <p style={{ margin: 0, fontSize: '15px', color: '#333', textAlign: 'left', paddingLeft: '30px', paddingTop: '50px', zIndex: 1 }}>
        번역 : {text3} </p>
      <p style={{ margin: 0, fontSize: '15px', color: '#333', textAlign: 'left', paddingLeft: '30px', paddingTop: '50px', zIndex: 1 }}>
        해설 : {text4} </p>
      </div>

      <div style={{ width: contentWidth || 920, height: contentHeight || 50, paddingLeft: 50, paddingRight: 50, paddingTop: 15, paddingBottom: 15, left: 0, top: contentTop || 360, position: 'absolute', background: '#FAFAFA', borderRadius: 25 }}>
        {/* Add a <p> element for text */}
        <p style={{ margin: 5, fontSize: '16px', color: '#404040', textAlign: 'left' }}>{text}</p>
        <p style={{ margin: 5, fontSize: '13px', color: '#5B5B5B', textAlign: 'left' }}>{text1}</p>

      </div>
    </div>
  );
};

export default InterpretationComponent;