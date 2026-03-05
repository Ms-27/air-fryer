const STORAGE_KEY = "airfryer_frequent_values_v1";
const FORM_ID = "convert-form";
const FIELDS = ["temperature", "time"];
const MAX_VALUES = 4;
const DEFAULT_VALUES = {
  temperature: ["180", "190", "200", "220"],
  time: ["10", "15", "20", "25"],
};

function convertForAirfryer(temperature, timeMinutes) {
  return {
    temperature: Math.max(80, Math.round(temperature - 15)),
    time: Math.max(1, Math.round(timeMinutes * 0.8)),
  };
}

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

function setupForm() {
  const form = document.getElementById(FORM_ID);
  if (!form) {
    return;
  }

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    
    const temperature = parseFloat(document.getElementById("temperature").value);
    const timeMinutes = parseFloat(document.getElementById("time").value);

    const stats = loadStats();
    FIELDS.forEach((field) => {
      const input = document.getElementById(field);
      if (input) {
        incrementValue(stats, field, input.value);
      }
    });
    saveStats(stats);

    const result = convertForAirfryer(temperature, timeMinutes);
    
    document.getElementById("result-temp").textContent = result.temperature + " °C";
    document.getElementById("result-time").textContent = result.time + " minutes";
    document.getElementById("result").classList.add("show");

    renderButtons();
  });
}

function init() {
  setupForm();
  renderButtons();
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", init);
} else {
  init();
}
