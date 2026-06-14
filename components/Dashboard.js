import React from 'react';
import ChartPanel from './ChartPanel';

/**
 * Dashboard
 * Main display component. Renders the ChartPanel
 * and a summary data table for the current dataset.
 */
function Dashboard({ data, category }) {
  if (!data || data.length === 0) {
    return (
      <p style={{ color: '#888', padding: '16px' }}>
        No records found for the selected filter.
      </p>
    );
  }

  return (
    <div style={styles.container}>
      {/* Chart panel */}
      <ChartPanel
        data={data}
        title={
          category === 'All'
            ? 'All Categories — Percentage Trend'
            : `${category} — Percentage Trend`
        }
      />

      {/* Summary table */}
      <div style={styles.tableWrapper}>
        <h2 style={styles.tableTitle}>Data Summary</h2>
        <table style={styles.table}>
          <thead>
            <tr>
              {['Date', 'Category', 'Count', 'Percentage (%)'].map((h) => (
                <th key={h} style={styles.th}>{h}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {data.map((row, i) => (
              <tr key={i} style={i % 2 === 0 ? styles.rowEven : styles.rowOdd}>
                <td style={styles.td}>{row.date}</td>
                <td style={styles.td}>{row.category}</td>
                <td style={styles.td}>{row.count}</td>
                <td style={{
                  ...styles.td,
                  color: row.percentage >= 50 ? '#cc0000' : '#1a1a2e',
                  fontWeight: row.percentage >= 50 ? 'bold' : 'normal',
                }}>
                  {row.percentage}%
                  {row.percentage >= 50 && ' ⚠'}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

const styles = {
  container: { width: '100%' },
  tableWrapper: {
    backgroundColor: '#ffffff',
    borderRadius: '8px',
    padding: '24px',
    boxShadow: '0 2px 8px rgba(0,0,0,0.08)',
  },
  tableTitle: {
    fontSize: '1.1rem',
    color: '#1F4E79',
    marginBottom: '16px',
  },
  table: {
    width: '100%',
    borderCollapse: 'collapse',
    fontSize: '0.9rem',
  },
  th: {
    backgroundColor: '#1F4E79',
    color: '#ffffff',
    padding: '10px 14px',
    textAlign: 'left',
  },
  td: {
    padding: '9px 14px',
    borderBottom: '1px solid #e0e0e0',
  },
  rowEven: { backgroundColor: '#f7f9fc' },
  rowOdd:  { backgroundColor: '#ffffff' },
};

export default Dashboard;
