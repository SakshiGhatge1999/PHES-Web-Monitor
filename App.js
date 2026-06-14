import React, { useState, useEffect } from 'react';
import Dashboard from './components/Dashboard';
import FilterPanel from './components/FilterPanel';
import AlertBanner from './components/AlertBanner';
import './App.css';

const API_BASE = process.env.REACT_APP_API_URL || 'http://localhost:5000';
const CATEGORIES = ['All', 'Anxiety', 'Confusion', 'Distrust', 'Fear', 'Acceptance'];

function App() {
  const [data, setData] = useState([]);
  const [alerts, setAlerts] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState('All');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchData(selectedCategory);
  }, [selectedCategory]);

  const fetchData = async (category) => {
    setLoading(true);
    setError(null);
    try {
      const url =
        category === 'All'
          ? `${API_BASE}/api/dashboard`
          : `${API_BASE}/api/dashboard?emotion=${category}`;

      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`Server error: ${response.status}`);
      }
      const json = await response.json();
      setData(json.data || []);
      setAlerts(json.alerts_triggered || []);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <header className="app-header">
        <h1>PHES-Web</h1>
        <p>Public Health Emotional and Stance Monitor</p>
      </header>

      <main className="app-main">
        {/* FR7: alert banner renders only when alerts exist */}
        {alerts.length > 0 && <AlertBanner alerts={alerts} />}

        {/* FR6: filter panel */}
        <FilterPanel
          categories={CATEGORIES}
          selected={selectedCategory}
          onChange={setSelectedCategory}
        />

        {loading && <p className="loading">Loading data...</p>}
        {error && <p className="error">Error: {error}</p>}
        {!loading && !error && <Dashboard data={data} category={selectedCategory} />}
      </main>
    </div>
  );
}

export default App;
