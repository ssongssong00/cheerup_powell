import React from 'react';
import './header.css';
import logoSrc from './FRAS_logo.png'; // Import the logo directly

function Header() {
  return (
    <div className="header">
      <a href="/" className="logo-link">
        <img src={logoSrc} alt="Logo" className="logo" />
        <span className="brand-name">FRAS</span>
      </a>
    </div>
  );
}

export default Header;