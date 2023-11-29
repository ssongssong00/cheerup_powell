import React from 'react';

const StanceComponent = ({ width, height, left, top }) => {
  return (
    <div style={{ width: '100%', height: '100%', position: 'relative' }}>
      <div
        style={{
          width: width || 350,
          height: height || 350,
          left: left || 670,
          top: top || 0,
          position: 'absolute',
          background:
            'linear-gradient(166deg, rgba(234.60, 0, 255, 0.27) 0%, rgba(94.06, 15.65, 144.50, 0.49) 22%, rgba(24.93, 70.31, 187, 0.81) 55%, rgba(35.22, 71.77, 165.75, 0.89) 73%, rgba(4.66, 38.16, 124.31, 0.97) 93%, #001751 100%, #001751 100%)',
          borderRadius: 35,
        }}
      />
    </div>
  );
};

export default StanceComponent;