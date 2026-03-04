PAGE = """
<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Convertisseur Four ➜ Airfryer</title>
  <style>
    :root {
      --bg: #f6f7f9;
      --card: #ffffff;
      --text: #1b1f24;
      --muted: #5a6470;
      --accent: #0b7a75;
      --accent-2: #0d9488;
      --border: #d8dee6;
    }

    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background: linear-gradient(160deg, #f6f7f9 0%, #eef8f8 100%);
      color: var(--text);
      min-height: 100vh;
      display: grid;
      place-items: center;
      padding: 1rem;
    }

    .card {
      width: 100%;
      max-width: 520px;
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 16px;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
      padding: 1rem;
    }

    h1 {
      font-size: 1.25rem;
      margin: 0 0 0.25rem;
    }

    p.sub {
      margin: 0 0 1rem;
      color: var(--muted);
      font-size: 0.95rem;
    }

    .grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 0.75rem;
    }

    label {
      font-size: 0.9rem;
      color: var(--muted);
      display: block;
      margin-bottom: 0.35rem;
    }

    input {
      width: 100%;
      padding: 0.75rem;
      border-radius: 10px;
      border: 1px solid var(--border);
      font-size: 1rem;
      background: #fff;
    }

    button {
      width: 100%;
      margin-top: 0.75rem;
      border: 0;
      border-radius: 10px;
      padding: 0.85rem;
      font-size: 1rem;
      color: #fff;
      background: linear-gradient(135deg, var(--accent), var(--accent-2));
      font-weight: 600;
      cursor: pointer;
    }

    .result {
      margin-top: 1rem;
      padding: 0.9rem;
      background: #f3fbfa;
      border: 1px solid #c4e9e6;
      border-radius: 12px;
    }

    .result h2 {
      margin: 0 0 0.5rem;
      font-size: 1rem;
    }

    .result ul {
      margin: 0;
      padding-left: 1.1rem;
    }

    .note {
      margin-top: 0.9rem;
      color: var(--muted);
      font-size: 0.85rem;
      line-height: 1.35;
    }

    .quick-picks {
      margin-top: 0.45rem;
      display: flex;
      flex-wrap: nowrap;
      gap: 0.4rem;
      min-height: 1.8rem;
      overflow-x: auto;
    }

    .chip {
      display: inline-flex;
      align-items: center;
      border: 1px solid #b7d9d6;
      background: #eef8f7;
      color: #0b5b56;
      border-radius: 999px;
      padding: 0.28rem 0.6rem;
      font-size: 0.82rem;
      cursor: pointer;
      white-space: nowrap;
      flex: 0 0 auto;
      width: auto;
      margin-top: 0;
    }

    .chip:hover {
      background: #def2f0;
    }

    .hint {
      margin-top: 0.35rem;
      color: var(--muted);
      font-size: 0.78rem;
    }
  </style>
</head>
<body>
  <main class="card">
    <h1>Convertisseur Four ➜ Airfryer</h1>
    <p class="sub">Saisissez les valeurs d'une recette en four traditionnel.</p>

    <form method="post" id="convert-form">
      <div class="grid">
        <div>
          <label for="temperature">Température four (°C)</label>
          <input id="temperature" name="temperature" type="number" min="30" step="1" required value="{{ values.temperature }}" />
          <div class="quick-picks" data-field="temperature"></div>
        </div>

        <div>
          <label for="time">Temps de cuisson (minutes)</label>
          <input id="time" name="time" type="number" min="1" step="1" required value="{{ values.time }}" />
          <div class="quick-picks" data-field="time"></div>
        </div>
      </div>

      <p class="hint">Les 4 valeurs les plus utilisées apparaissent en boutons sous chaque champ (stockage local du navigateur).</p>

      <button type="submit">Convertir</button>
    </form>

    {% if result %}
      <section class="result">
        <h2>Réglages conseillés pour l'airfryer :</h2>
        <ul>
          <li><strong>{{ result.temperature }} °C</strong></li>
          <li><strong>{{ result.time }} minutes</strong></li>
        </ul>
      </section>
    {% endif %}

    <p class="note">
      Règle simple utilisée : température -15°C, temps -20%.
      Ajustez selon l'épaisseur des aliments et votre modèle d'airfryer.
    </p>
  </main>

  <script>
    const STORAGE_KEY = "airfryer_frequent_values_v1";
    const FORM_ID = "convert-form";
    const FIELDS = ["temperature", "time"];
    const MAX_VALUES = 4;
    const DEFAULT_VALUES = {
      temperature: ["180", "190", "200", "220"],
      time: ["10", "15", "20", "25"],
    };

    function loadStats() {
      try {
        return JSON.parse(localStorage.getItem(STORAGE_KEY)) || {};
      } catch (error) {
        return {};
      }
    }

    function saveStats(stats) {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(stats));
    }

    function incrementValue(stats, field, value) {
      const cleanValue = String(value || "").trim();
      if (!cleanValue) {
        return;
      }

      if (!stats[field]) {
        stats[field] = {};
      }

      stats[field][cleanValue] = (stats[field][cleanValue] || 0) + 1;
    }

    function topValues(stats, field) {
      const entries = Object.entries(stats[field] || {});
      const frequentValues = entries
        .sort((a, b) => b[1] - a[1])
        .slice(0, MAX_VALUES)
        .map(([value]) => value);

      if (frequentValues.length >= MAX_VALUES) {
        return frequentValues;
      }

      const defaults = DEFAULT_VALUES[field] || [];
      const merged = [...frequentValues];
      defaults.forEach((value) => {
        if (!merged.includes(value) && merged.length < MAX_VALUES) {
          merged.push(value);
        }
      });

      return merged;
    }

    function renderButtons() {
      const stats = loadStats();

      FIELDS.forEach((field) => {
        const container = document.querySelector(`.quick-picks[data-field="${field}"]`);
        const input = document.getElementById(field);
        if (!container || !input) {
          return;
        }

        container.innerHTML = "";
        topValues(stats, field).forEach((value) => {
          const button = document.createElement("button");
          button.type = "button";
          button.className = "chip";
          button.textContent = value;
          button.addEventListener("click", () => {
            input.value = value;
            input.focus();
          });
          container.appendChild(button);
        });
      });
    }

    function setupSaveOnSubmit() {
      const form = document.getElementById(FORM_ID);
      if (!form) {
        return;
      }

      form.addEventListener("submit", () => {
        const stats = loadStats();
        FIELDS.forEach((field) => {
          const input = document.getElementById(field);
          if (input) {
            incrementValue(stats, field, input.value);
          }
        });
        saveStats(stats);
      });
    }

    setupSaveOnSubmit();
    renderButtons();
  </script>
</body>
</html>
"""
