function Report({ report }) {
  return (
    <article className="result-card">
      <h3>Final Report</h3>
      <pre style={{ whiteSpace: 'pre-wrap', margin: 0, color: '#dce9fc' }}>{report || 'No report generated yet.'}</pre>
    </article>
  );
}

export default Report;
