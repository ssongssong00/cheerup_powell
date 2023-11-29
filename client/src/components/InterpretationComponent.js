import React from 'react';

const InterpretationComponent = ({ containerWidth, containerHeight, contentWidth, contentHeight, contentTop }) => {
  return (
    <div style={{ width: '100%', height: '100%', position: 'relative' }}>
      <div style={{ width: containerWidth || 1020, height: containerHeight || 330, left: 0, top: contentTop || 360, position: 'absolute', background: 'white', borderRadius: 25 }} />
      <div style={{ width: contentWidth || 920, height: contentHeight || 50, paddingLeft: 50, paddingRight: 50, paddingTop: 15, paddingBottom: 15, left: 0, top: contentTop || 360, position: 'absolute', background: '#FAFAFA', borderRadius: 25 }}>
      </div>
    </div>
  );
};

export default InterpretationComponent;