function SkillCard({ title, items }) {
  return (
    <article className="result-card">
      <h3>{title}</h3>
      {items?.length ? (
        <ul className="skill-list">
          {items.map((item) => (
            <li key={item}>{item}</li>
          ))}
        </ul>
      ) : (
        <p>No skills listed.</p>
      )}
    </article>
  );
}

export default SkillCard;
