import React from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Line } from 'react-chartjs-2';

ChartJS.register(
  CategoryScale, LinearScale, PointElement,
  LineElement, BarElement, Title, Tooltip, Legend
);

/**
 * ChartPanel
 * Renders a Chart.js line chart of percentage over time
 * for the current filtered dataset.
 */
function ChartPanel({ data, title }) {
  if (!data || data.length === 0) {
    return <p style={{ color: '#888', padding: '16px' }}>No data to display.</p>;
  }

  const labels = data.map((d) => d.date);
  const percentages = data.map((d) => d.percentage);
  const category = data[0]?.category || 'All';

  // Colour based on category
  const colourMap = {
    Anxiety:    'rgba(231, 76,  60,  0.8)',
    Confusion:  'rgba(230, 126, 34,  0.8)',
    Distrust:   'rgba(142, 68,  173, 0.8)',
    Fear:       'rgba(41,  128, 185, 0.8)',
    Acceptance: 'rgba(39,  174, 96,  0.8)',
  };
  const colour = colourMap[category] || 'rgba(31, 78, 121, 0.8)';

  const chartData = {
    labels,
    datasets: [{
      label: `${category} (%)`,
      data: percentages,
      borderColor: colour,
      backgroundColor: colour.replace('0.8', '0.15'),
      borderWidth: 2,
      pointRadius: 4,
      tension: 0.3,
      fill: true,
    }],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: { position: 'top' },
      title: { display: true, text: title || `${category} Trend` },
    },
    scales: {
      y: {
        min: 0,
        max: 100,
        title: { display: true, text: 'Percentage (%)' },
      },
      x: {
        title: { display: true, text: 'Date' },
      },
    },
  };

  return (
    <div style={styles.wrapper}>
      <Line data={chartData} options={options} />
    </div>
  );
}

const styles = {
  wrapper: {
    backgroundColor: '#ffffff',
    borderRadius: '8px',
    padding: '24px',
    boxShadow: '0 2px 8px rgba(0,0,0,0.08)',
    marginBottom: '24px',
  },
};

export default ChartPanel;
