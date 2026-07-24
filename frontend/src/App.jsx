import { useState } from 'react';
import StudentForm from './components/StudentForm';
import SkillCard from './components/SkillCard';
import RoadmapCard from './components/RoadmapCard';
import ProjectCard from './components/ProjectCard';
import Report from './components/Report';
import { submitCareerRequest } from './services/api';

function App() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [result, setResult] = useState(null);

  const handleSubmit = async (formData) => {
    setLoading(true);
    setError('');
    setResult(null);

    try {
      const response = await submitCareerRequest(formData);
      setResult(response.data);
    } catch (err) {
      setError(err?.response?.data?.detail || 'Unable to submit your request right now.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-shell">
      <header className="hero-card">
        <div>
          <p className="eyebrow">CareerPilot AI</p>
          <h1>Plan your next move with confidence</h1>
          <p className="hero-copy">
            Share your background and target role to receive a tailored roadmap, skill gaps, and project ideas.
          </p>
        </div>
      </header>

      <main className="content-grid">
        <StudentForm onSubmit={handleSubmit} loading={loading} />

        <section className="results-panel">
          {error ? <div className="status-card error">{error}</div> : null}

          {!result && !loading ? (
            <div className="status-card">Your results will appear here after you submit the form.</div>
          ) : null}

          {loading ? <div className="status-card loading">Generating your career plan...</div> : null}

          {result ? (
            <>
              <div className="cards-grid">
                <SkillCard title="Required Skills" items={result.required_skills} />
                <SkillCard title="Missing Skills" items={result.missing_skills} />
              </div>
              <RoadmapCard roadmap={result.roadmap} reasoning={result.reasoning} />
              <ProjectCard projects={result.recommended_projects} />
              <Report report={result.final_report} />
            </>
          ) : null}
        </section>
      </main>
    </div>
  );
}

export default App;
