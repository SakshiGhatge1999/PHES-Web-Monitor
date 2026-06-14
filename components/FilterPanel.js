import React from 'react';

/**
 * FilterPanel (FR6)
 * Dropdown control for filtering dashboard data
 * by emotional category. Triggers a new API call
 * via the onChange callback — no page reload.
 */
function FilterPanel({ categories, selected, onChange }) {
  return (
    <div style={styles.panel}>
      <label style={styles.label} htmlFor="emotion-filter">
        Filter by Emotional Category:
      </label>
      <select
        id="emotion-filter"
        value={selected}
        onChange={(e) => onChange(e.target.value)}
        style={styles.select}
      >
        {categories.map((cat) => (
          <option key={cat} value={cat}>{cat}</option>
        ))}
      </select>
    </div>
  );
}

const styles = {
  panel: {
    display: 'flex',
    alignItems: 'center',
    gap: '12px',
    marginBottom: '24px',
    flexWrap: 'wrap',
  },
  label: {
    fontSize: '0.95rem',
    fontWeight: 'bold',
    color: '#1F4E79',
  },
  select: {
    padding: '8px 12px',
    fontSize: '0.95rem',
    border: '1px solid #2E75B6',
    borderRadius: '4px',
    backgroundColor: '#ffffff',
    color: '#1a1a2e',
    cursor: 'pointer',
    minWidth: '160px',
  },
};

export default FilterPanel;
