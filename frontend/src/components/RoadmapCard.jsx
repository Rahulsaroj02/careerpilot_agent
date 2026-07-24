function RoadmapCard({ roadmap, reasoning }) {
  const parseRoadmap = (text) => {
    if (!text) return [];

    const lines = text.split(/\r?\n/).filter(Boolean);
    const weeks = [];
    let currentWeek = null;

    lines.forEach((line) => {
      const weekMatch = line.match(/^Week\s+(\d+)/i);
      if (weekMatch) {
        if (currentWeek) {
          weeks.push(currentWeek);
        }
        currentWeek = { title: line.trim(), content: [] };
        return;
      }

      if (!currentWeek) {
        currentWeek = { title: 'Roadmap', content: [] };
      }

      currentWeek.content.push(line.trim());
    });

    if (currentWeek) {
      weeks.push(currentWeek);
    }

    return weeks;
  };

  const weeks = parseRoadmap(roadmap);

  return (
    <article className="result-card">
      <h3>Roadmap</h3>
      {reasoning ? <p className="roadmap-reasoning">{reasoning}</p> : null}

      {weeks.length ? (
        <div className="roadmap-list">
          {weeks.map((week, index) => (
            <section key={`${week.title}-${index}`} className="roadmap-week">
              <h4>{week.title}</h4>
              <div className="roadmap-content">
                {week.content.map((item, itemIndex) => (
                  <p key={`${week.title}-${itemIndex}`}>{item}</p>
                ))}
              </div>
            </section>
          ))}
        </div>
      ) : (
        <p>{roadmap || 'No roadmap generated yet.'}</p>
      )}
    </article>
  );
}

export default RoadmapCard;
