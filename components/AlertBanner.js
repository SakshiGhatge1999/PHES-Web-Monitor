import React from 'react';

/**
 * AlertBanner (FR7)
 * Renders a visually distinct red banner when
 * the API response contains active threshold alerts.
 * Only rendered when alerts array is non-empty.
 */
function AlertBanner({ alerts }) {
  return (
    <div style={styles.banner}>
      <strong style={styles.title}>⚠ Threshold Alert</strong>
      {alerts.map((alert, index) => (
        <p key={index} style={styles.message}>{alert.message}</p>
      ))}
    </div>
  );
}

const styles = {
  banner: {
    backgroundColor: '#cc0000',
    color: '#ffffff',
    padding: '16px 20px',
    borderRadius: '6px',
    marginBottom: '20px',
  },
  title: {
    fontSize: '1rem',
    display: 'block',
    marginBottom: '8px',
  },
  message: {
    fontSize: '0.9rem',
    lineHeight: '1.5',
    marginBottom: '4px',
  },
};

export default AlertBanner;
