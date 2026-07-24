import { useState } from 'react';

function StudentForm({ onSubmit, loading }) {
  const [formData, setFormData] = useState({
    name: '',
    education: '',
    target_role: '',
    current_skills: '',
  });

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    const payload = {
      ...formData,
      current_skills: formData.current_skills
        .split(',')
        .map((skill) => skill.trim())
        .filter(Boolean),
    };
    onSubmit(payload);
  };

  return (
    <form className="form-card" onSubmit={handleSubmit}>
      <h2>Student details</h2>
      <div className="form-grid">
        <label>
          Name
          <input name="name" value={formData.name} onChange={handleChange} required />
        </label>
        <label>
          Education
          <input name="education" value={formData.education} onChange={handleChange} required />
        </label>
        <label>
          Target Role
          <input name="target_role" value={formData.target_role} onChange={handleChange} required />
        </label>
        <label>
          Current Skills
          <textarea
            name="current_skills"
            value={formData.current_skills}
            onChange={handleChange}
            placeholder="Python, SQL, React"
          />
        </label>
      </div>
      <button type="submit" disabled={loading} style={{ marginTop: 16 }}>
        {loading ? 'Submitting...' : 'Generate Career Plan'}
      </button>
    </form>
  );
}

export default StudentForm;
