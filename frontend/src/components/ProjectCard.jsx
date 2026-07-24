function ProjectCard({ projects }) {
  return (
    <article className="result-card">
      <h3>Recommended Projects</h3>
      {projects?.length ? (
        <ul className="project-list">
          {projects.map((project) => (
            <li key={project}>{project}</li>
          ))}
        </ul>
      ) : (
        <p>No projects recommended.</p>
      )}
    </article>
  );
}

export default ProjectCard;
